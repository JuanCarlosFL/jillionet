let currencyFormatter = new Intl.NumberFormat("en-EN", {
    maximumFractionDigits: 2,
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

    let initialCont = '';
    let mainFunds = [];
    let totalFundsSet = [];
    let totalFundsSet2 = [];

    for (const fundName in funds){
        initialCont += currencyCont(fundName, funds[fundName])


        let initialValue = 0;
        let totalFunds = await funds[fundName].reduce(async (previousValue, currentValue) => {
            totalFundsSet2.push(currentValue)
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
        let currencyTotal = await groupedFundsSet[currency].reduce((sum, currentItem) => {
            return sum + parseFloat(currentItem.amount) + parseFloat(currentItem.staked)
        }, 0)

        let obj = {
            total: currencyTotal,
            currency: currency
        };

        mainFunds.push(obj)
    }
    //console.log(mainFunds)


    //console.log(groupBy(totalFundsSet2, 'currency__code'))

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

    document.getElementById('my-funds-dom').innerHTML = initialCont;
    document.getElementById('main-funds').innerHTML = mainComponent(mainFunds);
}

const currencyCont = (name, bal) => {
    let currencyRows = '';
    let currencyModals = '';
    let rows = bal.forEach(item => {
        currencyRows += availableCurrency(item.currency__code, item.amount, item.id, name)
        currencyModals += item.balance_for__name==="spot" || item.balance_for__name==="main"? depositWithdrawModalComponent(item.id, item.currency__code, item.amount, name): tranferModalComponent(item.id, item.currency__code, item.amount, name)
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
    let currencyRow = `    
        <tr class="unread">
            <td><img class="rounded-circle" style="width:40px;"
                     src="https://cryptoicon-api.vercel.app/api/icon/${code.toLowerCase()}"
                     alt="activity-user"></td>
            <td>
                <h6 class="mb-1">${code}</h6>
                
            </td>
            <td>
                <h6 class="text-muted">${amount}</h6>
                <p class="m-0 small">€ 0.00</p>
            </td>
            <td>
                ${btn}
            </td>
        </tr>    
    `
    return currencyRow
}

let depositWithdrawModalComponent = (id, code, amount, name) => {
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
                                            <div>
                                                <label for="customRange3">Example range</label>
                                                <input type="range" class="custom-range" min="0" max="5" step="0.5" id="customRange3">
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
                                                <p>lnhbfcrtfchgxfxjbcxftkhgg</p>
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
        currencyModals += depositWithdrawModalComponent(item.currency, item.currency, item.total, "main")
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

fundsContainer(myFunds)