let currencyFormatter = new Intl.NumberFormat(Intl.locale, {
    maximumFractionDigits: 2,
    style: 'currency',
    currency: 'EUR',
})

let jillEuroCurrencyFormatter = new Intl.NumberFormat(Intl.locale, {
    maximumFractionDigits: 8,
    style: 'currency',
    currency: 'EUR',
})

let numberFormatter = new Intl.NumberFormat(Intl.locale, {
    maximumFractionDigits: 2,

})

function groupBy(objectArray, property) {
  return objectArray.reduce(function (acc, obj) {
    let key = obj[property]
    if (!acc[key]) {
      acc[key] = []
    }
    acc[key].push(obj)
    return acc
  }, {})
}

const fundsContainer = async (funds) => {

    let initialCont = document.getElementById('my-funds-dom');
    initialCont.innerHTML = ''
    let mainFunds = [];
    let totalFundsSet = [];
    let totalFundsSet2 = [];

    for (const fundName in funds){

        initialCont.innerHTML += currencyCont(fundName, funds[fundName])


        let initialValue = 0;
        let totalFunds = await funds[fundName].reduce(async (previousValue, currentValue) => {
            totalFundsSet2.push(currentValue)
            //console.log(`qrcode-${currentValue.id}`)
            if (currentValue.balance_for__name == 'spot'){
              generateQrCode(`qrcode-${currentValue.id}`, currentValue.public_key==''?currentValue.currency__default_public_key:currentValue.public_key)
            }
            let price = await (currentValue.currency__code.includes('USD')? getCurrentPrice('EUR'+currentValue.currency__code): getCurrentPrice(currentValue.currency__code+'EUR'))
            //console.log(price)
            return await previousValue + ((parseFloat(currentValue.amount) + parseFloat(currentValue.staked)) * price.price)
        }, initialValue)

        totalFundsSet.push({
            value: totalFunds,
            label: fundName
        })
    }

    let groupedFundsSet = groupBy(totalFundsSet2, 'currency__code')

    for (const currency in groupedFundsSet) {
      let p_key, d_key
        let currencyTotal = await groupedFundsSet[currency].reduce((sum, currentItem) => {
          p_key = currentItem.public_key
          d_key = currentItem.currency__default_public_key
            return sum + parseFloat(currentItem.amount) + parseFloat(currentItem.staked)
        }, 0)

        let obj = {
            total: currencyTotal,
            currency: currency,
            public_key: p_key,
            default_public_key: d_key
        };

        mainFunds.push(obj)
    }


    var graph = Morris.Donut({
        element: 'morris-donut-chart',
        data: totalFundsSet,
        colors: [
            '#1de9b6',
            '#A389D4',
            '#04a9f5',
            '#1dc4e9',
        ],
        resize: true,
        formatter: function(x) {
            return currencyFormatter.format(x)
        }
    });

    //document.getElementById('my-funds-dom').innerHTML = initialCont;
    document.getElementById('main-funds').innerHTML = mainComponent(mainFunds);
    $(".js-range-slider").ionRangeSlider();

    for (const fund in mainFunds) {
      generateQrCode(`qrcode-${mainFunds[fund].currency}`, mainFunds[fund].public_key==''?mainFunds[fund].default_public_key:mainFunds[fund].public_key)
    }

    //let fundAmount = document.getElementsByClassName('fund-amount')
    [...document.getElementsByClassName('fund-amount')].map(async item => {
      let amount = parseFloat(item.innerText)
      let itemId = item.id
      var price
        var currencyCode = itemId.split('-').pop()


      if (itemId.includes('USD')){
        streamFundPrice(`EUR${currencyCode}`.toLocaleLowerCase(), itemId, amount)
        //getCurrentPrice('EUR'+itemId.split('-').pop())
        //.then((price) =>{
        //  var el = document.createElement("small");
        //  el.innerText = price.price * amount;
        //  item.parentNode.insertBefore(el, item.nextSibling)
        //})

      }else {
          //console.log(currencyCode, 'kkk')
        streamFundPrice(currencyCode=='JILL'? 'btcusdt':`${currencyCode}EUR`.toLocaleLowerCase(), itemId, amount)
      //  getCurrentPrice(itemId.split('-').pop()+'EUR')
      //  .then((price) => {
      //    var el = document.createElement("small");
      //    el.innerText = price.price * amount;
      //    item.parentNode.insertBefore(el, item.nextSibling)
      //  })
      }
      console.log(price)
    })

}

const currencyCont = (name, bal) => {
    let currencyRows = '';
    let currencyModals = '';
    let rows = bal.forEach(item => {
        currencyRows += availableCurrency(item.currency__code, item.amount, item.id, name)
        currencyModals += item.balance_for__name==="spot" || item.balance_for__name==="main"? depositWithdrawModalComponent(item.id, item.currency__code, item.amount, name, item.public_key, item.currency__default_public_key): tranferModalComponent(item.id, item.currency__code, item.amount, name)

    })

    return `
    <div class="col-xl-8 col-md-6">
        <div class="card Recent-Users">
            <div class="card-header">
                <h5>${name}</h5>
            </div>
            <div class="card-block px-0 py-3">
                <div class="table-responsive">
                    <table class="table table-hover">
                        <tbody>
                        ${currencyRows}
    
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        ${currencyModals}
    </div>
    `
}

var availableCurrency = (code, amount, id, name) => {
    let btn;
    if (name === "main" || name === "spot"){
        btn = `<button data-toggle="modal" data-target="#withdrawModal${id}" type="button" class="label theme-bg2 text-white f-12">Withdraw</button>
                <button type="button" data-toggle="modal" data-target="#depositModal${id}" class="label theme-bg text-white f-12">Deposit</button>`
    }else {
        btn = `<button data-toggle="modal" data-target="#transferModal${id}" type="button" class="label theme-bg2 text-white f-12">Transfer</button>`
    }

    //let euroAmount = await (code.includes('USD')? getCurrentPrice('EUR'+code): getCurrentPrice(code+'EUR'))
    //console.log(euroAmount)
    let currencyRow = `    
        <tr class="unread">
            <td><img class="rounded-circle" style="width:40px;"
                     src="/static/img/currency_icons/${code}.svg"
                     alt="activity-user"></td>
            <td>
                <h6 class="mb-1">${code}</h6>
                
            </td>
            <td>
                <h6 id="fund-${name}-${code}" class="fund-amount text-muted">${amount}</h6>
                <p id="fund-${name}-${code}-euro" class="m-0 small">€ 0.00</p>
            </td>
            <td>
                ${btn}
            </td>
        </tr>    
    `
    return currencyRow
}

let depositWithdrawModalComponent = (id, code, amount, name, public_key, default_key) => {
    return `<!-- Withdraw Modal -->
                                <div class="modal fade" id="withdrawModal${id}" tabindex="-1" role="dialog" aria-labelledby="withdrawModal${id}Label" aria-hidden="true">
                                  <div class="modal-dialog" role="document">
                                    <div class="modal-content">
                                      <div class="modal-header">
                                        <h5 class="modal-title" id="withdrawModal${id}Label">Withdraw ${code} from ${name}</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                          <span aria-hidden="true">&times;</span>
                                        </button>
                                      </div>
                                      <div class="modal-body">
                                        <form>
                                        <h3 class="text-center">${numberFormatter.format(amount)} ${code}</h3>
                                            <div><input type="number" class="form-control" placeholder="Amount"></div>
                                            <div class="mt-2">
                                                
                                               <input type="text" class="js-range-slider" name="my_range" data-max="${amount}" value="" />
                                            </div> 
                                            <div class="mt-3">
                                                <input type="text" class="form-control" placeholder="Pulic key">
                                            </div>                                                                               
                                        </form>
                                      </div>
                                      <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary">Withdraw</button>
                                      </div>
                                    </div>
                                  </div>
                                </div>

                                <!-- Deposit Modal -->
                                <div class="modal fade" id="depositModal${id}" tabindex="-1" role="dialog" aria-labelledby="depositModal${id}Label" aria-hidden="true">
                                  <div class="modal-dialog" role="document">
                                    <div class="modal-content">
                                      <div class="modal-header">
                                        <h5 class="modal-title" id="depositModal${id}Label">Deposit ${code} to ${name}</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                          <span aria-hidden="true">&times;</span>
                                        </button>
                                      </div>
                                      <div class="modal-body">
                                        <form>
                                                                                    
                                            <div>
                                                <p><b>Public key</b></p>
                                                <p>${public_key==''?default_key:public_key}</p>
                                                <div id="qrcode-${id}" class="qrcode"></div>
                                            </div>                                                                                
                                        </form>
                                      </div>
                                      <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary">Save changes</button>
                                      </div>
                                    </div>
                                  </div>
                                </div>`
}


let tranferModalComponent = (id, code, amount, name) => {
    return `<!-- tranfer Modal -->
            <div class="modal fade" id="transferModal${id}" tabindex="-1" role="dialog" aria-labelledby="transferModal${id}Label" aria-hidden="true">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="transferModal${id}Label">Transfer ${code} from ${name}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <form>
                    <h3 class="text-center">${numberFormatter.format(amount)} ${code}</h3>
                        <div><input id="tranfer-amount${id}" type="number" class="form-control" placeholder="Amount"></div>
                        <div class="form-group mt-1">
                            
                            <input type="range" class="custom-range" min="0" max="${numberFormatter.format(amount)}" onchange="updateAmount(this.value, 'tranfer-amount${id}')" step="0.5" id="customRange${id}">
                        </div>
                        <div class="">
                        
                            <select class="form-control custom-select">
                                <option value='spot'>Spot</option>
                                <option value='jillbot'>Jillbot</option>
                                <option value='jillfarm'>Jillfarm</option>
                            </select>                            
                            
                        </div>
                                                                                                        
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                  </div>
                </div>
              </div>
            </div>
`
}


const mainComponent = (mainFunds) => {

    let currencyRows = '';
    let currencyModals = '';
    let rows = mainFunds.forEach(item => {
        currencyRows += availableCurrency(item.currency, item.total, item.currency, "main")
        currencyModals += depositWithdrawModalComponent(item.currency, item.currency, item.total, "main", item.public_key, item.default_public_key)
    })

    return `
        <div class="card-block px-0 py-3">
            <div class="card Recent-Users">
        
                <div class="card-header">
                    <h5>Main</h5>
                </div>
                <div class="card-block px-0 py-3">
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <tbody>
                            ${currencyRows}
        
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        ${currencyModals}
    
    `
}

function updateAmount(val, elmId) {
  var volumeElement
  volumeElement = document.getElementById(elmId);

  volumeElement.value = val;
}

const generateQrCode = (id, publicKey) => {
  let qrcodeContainer = document.getElementById(id);
  //console.log(qrcodeContainer);
  qrcodeContainer.innerHTML = "";
  new QRCode(qrcodeContainer, publicKey);
}

fundsContainer(myFunds)

