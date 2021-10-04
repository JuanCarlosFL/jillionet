let app = Vue.createApp({
    data: function () {
        return {
            myFunds: myFunds,
            totalAssets: totalAssets
        }
    },
    methods: {
        getMyFunds() {
            console.log(this.totalAssets)
        }
    }
})

app.component('fund-component', {
    data: function () {
        return {
            allFunds: allFunds
        }
    },
    template:`
        <div v-for="(fund, i) in allFunds" :key="i" class="col-xl-8 col-md-6">
            <div class="card Recent-Users">
                <div class="card-header">
                    <h5>{{ fund.name }}</h5>
                </div>
                <div class="card-block px-0 py-3">
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <tbody>
                            
                                <tr v-for="asset in fund.funds" :key="asset.id" class="unread">
                                    <td><img class="rounded-circle" style="width:40px;"
                                             v-bind:src="'/static/img/currency_icons/'+asset.currency_code+'.svg'"
                                             alt="activity-user"></td>
                                    <td>
                                        <h6 class="mb-1">{{ asset.currency_code }}</h6>
                                        
                                    </td>
                                    <td>
                                        <h6 class="text-muted">{{ asset.amount }}</h6>
                                        <p class="m-0 small">€ 0.00</p>
                                    </td>
                                    <td>
                                        <template v-if="asset.balance_name=='spot'">
                                            <button data-toggle="modal"
                                                    :data-target="'#withdrawModal'+asset.id"
                                                    type="button"
                                                    class="label theme-bg2 text-white f-12">Withdraw
                                            </button>
                                            <button
                                                    type="button" data-toggle="modal"
                                                    :data-target="'#depositModal'+asset.id"
                                                    class="label theme-bg text-white f-12">Deposit
                                            </button>
                                        </template>
                                        <template v-else>
                                            <button
                                                    type="button" data-toggle="modal"
                                                    :data-target="'#transferModal'+asset.id"
                                                    class="label theme-bg text-white f-12">Transfer
                                            </button>
                                        </template>
                                    </td>
                                </tr>
                            
    
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            
            <div v-for="(asset, i) in fund.funds" :key="i">
                <template  v-if="asset.balance_name=='spot'">
                    <!-- Withdraw Modal -->
                    <div class="modal fade" :id="'withdrawModal'+asset.id" tabindex="-1" role="dialog"
                         :aria-labelledby="'withdrawModal+asset.id+Label'" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" :id="'withdrawModal'+asset.id+'Label'">
                                        Withdraw {{ asset.currency_code }}
                                        from {{ asset.balance_name }}</h5>
                                    <button type="button" class="close" data-dismiss="modal"
                                            aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    ...
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">
                                        Close
                                    </button>
                                    <button type="button" class="btn btn-primary">Save changes</button>
                                </div>
                            </div>
                        </div>
                    </div>
        
                    <!-- Deposit Modal -->
                    <div class="modal fade" :id="'depositModal'+asset.id" tabindex="-1" role="dialog"
                 aria-labelledby="'depositModal'+asset.id+'Label'" aria-hidden="true">
                    <div class="modal-dialog" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" :id="'depositModal'+asset.id+'Label'">
                                    Deposit {{ asset.currency_code }}
                                    to {{ asset.balance_name }}</h5>
                                <button type="button" class="close" data-dismiss="modal"
                                        aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                ...
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">
                                    Close
                                </button>
                                <button type="button" class="btn btn-primary">Save changes</button>
                            </div>
                        </div>
                    </div>
                </div>
                </template>
                <template v-else>
                    <!-- tranfer Modal -->
                    <div class="modal fade" :id="'transferModal'+asset.id" tabindex="-1" role="dialog" :aria-labelledby="'transferModal'+asset.id+'Label'" aria-hidden="true">
                      <div class="modal-dialog" role="document">
                        <div class="modal-content">
                          <div class="modal-header">
                            <h5 class="modal-title" :id="'transferModal'+asset.id+'Label'">Transfer {{asset.currency_code}} from {{asset.balance_name}}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                            </button>
                          </div>
                          <div class="modal-body">
                            <form>
                            <h3 class="text-center">{{asset.amount}} {{asset.currency_code}}</h3>
                                <div><input :id="'tranfer-amount'+asset.id" type="number" class="form-control" placeholder="Amount"></div>
                                <div class="form-group mt-1">
                                    
                                    <input type="range" class="custom-range" min="0" max="{{numberFormatter.format(amount)}}" step="0.5" >
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
                </template>
            </div>
        </div>
    `
})

app.component('all-assets', {
    template: `
    <div class="card-block px-0 py-3">
        <div class="card Recent-Users">
    
            <div class="card-header">
                <h5>All asset</h5>
            </div>
            <div class="card-block px-0 py-3">
                <div class="table-responsive">
                    <table class="table table-hover">
                        <tbody>
                            <tr v-for="(asset, i) in totalAssets" :key="i" class="unread">
                                <td><img class="rounded-circle" style="width:40px;"
                                         v-bind:src="'/static/img/currency_icons/'+asset.symbol+'.svg'"
                                         alt="activity-user"></td>
                                <td>
                                    <h6 class="mb-1">{{asset.symbol}}</h6>
                                    
                                </td>
                                <td>
                                    <h6 id="fund-main-{{asset.symbol}}" class="fund-amount text-muted">{{asset.amount}}</h6>
                                    <p id="fund-main-{{asset.symbol}}-euro" class="m-0 small">€ 0.00</p>
                                </td>
                                
                            </tr>    
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    `,
    data: function () {
        return {
            totalAssets: totalAssets
        }
    }
})

app.component('donut-chart', {
    template: `
    <div class="card-block px-0 py-3">
        <div class="card">
            <div class="card-header">
                <h5>Overview</h5>
            </div>
            <div class="card-block">
                <div id="morris-donut-chart" style="height:400px"></div>
            </div>
        </div>
    </div>
    `,
    data: function () {
        return {
            myFunds: myFunds,
        }
    },
    methods: {
        async displayDonutChart() {
            let myFunds = this.myFunds.map(async (fund) => {

                let totalFunds = await fund.funds.reduce(async (sum, currentValue) => {
                    let price = await (currentValue.currency_code.includes('USD') ?
                        getCurrentPrice('EUR' + currentValue.currency_code) :
                        getCurrentPrice(currentValue.currency_code + 'EUR'))

                    return await sum + ((parseFloat(currentValue.amount) + parseFloat(currentValue.staked)) * price.price)
                }, 0)

                return {
                    value: totalFunds,
                    label: fund.balance_name
                }
            })
            const totalFundsSet = await Promise.all(myFunds)
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
                formatter: function (x) {
                    return currencyFormatter.format(x)
                }
            });
        }
    },
    created() {
        //console.log(this.totalAssets, 'created')
    },
    mounted() {
        this.displayDonutChart()
    }
})

app.mount('#main-body')