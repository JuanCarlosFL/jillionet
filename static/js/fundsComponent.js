let currencyFormatter = new Intl.NumberFormat("en-EN", {
    maximumFractionDigits: 2,
    style: 'currency',
    currency: 'EUR',
})

let numberFormatter = new Intl.NumberFormat(Intl.locale, {
    maximumFractionDigits: 2,

})

const fundsContainer = async (funds) => {

    let initialCont = '';
    let fundsdata;
    let totalFundsSet = []

    for (const fundName in funds){
        initialCont += currencyCont(fundName, funds[fundName])
        //total[fundName] = 0;
        // fundsdata = funds[fundName].map(item => {
        //
        //     return {
        //         [fundName]: parseFloat(item.amount) + parseFloat(item.staked)
        //     }
        // })

        let initialValue = 0;
        let totalFunds = await funds[fundName].reduce(async (previousValue, currentValue) => {
            //console.log(previousValue, currentValue)
            let price = await (currentValue.currency__code.includes('USD')? getCurrentPrice('EUR'+currentValue.currency__code): getCurrentPrice(currentValue.currency__code+'EUR'))
            //console.log(price)
            return await previousValue + ((parseFloat(currentValue.amount) + parseFloat(currentValue.staked)) * price.price)
        }, initialValue)

        totalFundsSet.push({
            value: totalFunds,
            label: fundName
        })
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

    document.getElementById('my-funds-dom').innerHTML = initialCont
}

const currencyCont = (name, bal) => {
    let initialCont = '';
    let initialModals = '';
    let rows = bal.forEach(item => {
        initialCont += availableCurrency(item.currency__code, item.amount, item.id)
        initialModals += modalComponent(item.id, item.currency__code, item.amount, name)
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
                        ${initialCont}
    
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        ${initialModals}
    </div>
    `
}

var availableCurrency = (code, amount, id) => {
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
            <td><button data-toggle="modal" data-target="#withdrawModal${id}" type="button" class="label theme-bg2 text-white f-12">Withdraw</button><button
                    type="button" data-toggle="modal" data-target="#depositModal${id}"
                    class="label theme-bg text-white f-12">Deposit</button></td>
        </tr>    
    `
    return currencyRow
}

let modalComponent = (id, code, amount, name) => {
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
                                </div>`
}

fundsContainer(myFunds)