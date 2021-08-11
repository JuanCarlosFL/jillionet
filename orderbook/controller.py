from .models import Order


def get_mathing_order(order):
   if order.buy_sell == Order.SELL:
      new_orders = Order.objects.filter(status=Order.NEW, trading_pair=order.trading_pair, price=order.price, volume=order.volume, buy_sell=Order.BUY).order_by('-timestamp')
   else:
      new_orders = Order.objects.filter(status=Order.NEW, trading_pair=order.trading_pair, price=order.price, volume=order.volume, buy_sell=Order.SELL).order_by('-timestamp')
   
   buy_currency, sell_currency = order.trading_pair.pair.split('/')

   if order.buy_sell == Order.SELL:
      order_user_balance = order.user.userbalance_set.filter(currency__code=sell_currency).first()
   else:
      order_user_balance = order.user.userbalance_set.filter(currency__code=buy_currency).first()

   if new_orders.exists():
      matching_order = new_orders.first()
      if matching_order.buy_sell == Order.SELL:
         matching_user_balance = matching_order.user.userbalance_set.filter(currency__code=sell_currency).first()
         matching_user_balance.amount =  matching_user_balance.amount - order.volume
         matching_user_balance.save()
         order_user_balance.amount = order_user_balance.amount + order.volume
         order_user_balance.save()
      else:
         matching_user_balance = matching_order.user.userbalance_set.filter(currency__code=buy_currency).first()
         matching_user_balance.amount =  matching_user_balance.amount + order.volume
         matching_user_balance.save()
         order_user_balance.amount = order_user_balance.amount - order.volume
         order_user_balance.save()

      matching_order.status = Order.FILL
      matching_order.save()

      order.status = Order.FILL
      order.save()


def make_market_order(order, market_price):
   buy_currency, sell_currency = order.trading_pair.pair.split('/')
   if order.buy_sell == Order.SELL:
      order_user_balance = order.user.userbalance_set.filter(currency__code=sell_currency).first()
      order_user_balance.amount = order_user_balance.amount - order.volume
      order_user_balance.save()
   else:
      order_user_balance = order.user.userbalance_set.filter(currency__code=buy_currency).first()
      order_user_balance.amount = order_user_balance.amount + order.volume
      order_user_balance.save()

       #MAKE A MARKET SYSTEM ORDER FILL JILL/USDT
       #1 Buy order 23.6%
       #2 Buy order 38.2%
       #3 Buy order 50%
       #4 Buy order 76.4%
       #5 Buy order 100%
       #6 Sell order 23.6%
       #7 Sell order 38.2%
       #8 Sell order 50%
       #9 Sell order 76.4
       #10 Sell order 100%


##((/x+ETH/X)/2)*(Lastorderbook price)
    ##

      



      
   

      #MAKE A MARKET SYSTEM ORDER FILL


      #1PIP 0,01%
      #10PIPs 0,1% Binance
      #100PIPs 1%
      #1000PIPs 10%
      
      #JILL/BUSD 1000 JILL for 1 BUSD

      #1account>BUY
      #2account>SELL
      #3account>WIN >100PIPs>100JILL 0,1BUSD

      #Maker maker order

      #JILL asset account1.amount=account1.amount+900 ADN account2.amount=account2.amount-1000
      #BUSD asset account1.amount=account1.amount-1 ADN account2.amount=account2.amount+0,9