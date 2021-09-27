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