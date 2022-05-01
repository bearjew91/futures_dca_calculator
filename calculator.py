from prettytable import PrettyTable
from pycoingecko import CoinGeckoAPI
import requests
import urllib3
import json

urllib3.disable_warnings()

 
# # # # # # # # # # CONFIGURATION # # # # # # # # # #


coin = "bitcoin"                  #coin name for dca simualtion
static_price = None             #static price instead of price lookup from coingecko, if set as number, script wont execute price lookup, set to None to disable
leverage = 20                     #leverage used
base_order = 105                  #base order
safety_order = 35                #first safety order
safety_order_step_scale = 1.15    #safety order steps will grow by this multiplier
safety_order_volume_scale = 1.6   #safety order volumes will grow by this multiplier
max_safety_orders = 10            #maximum amount of safety orders
price_deviation = 1               #starting price deviation, will trigger the first safety order
additionnal_dump = 4.7            #extra dump after the last safety order was filled (%)

 
# # # # # # # # # # CONFIGURATION # # # # # # # # # #


def get_price(coin):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids={},tether&vs_currencies=usd'.format(coin)
    headers = {"accept": "application/json"}
    resp = requests.get(url, headers=headers, verify=False)
    data = json.loads(resp.text)
    price = data[coin]["usd"]/data["tether"]["usd"]
    return price
 

x = PrettyTable()
x.field_names = ["Safety Order #", "Price Deviation", "Price", "Avarage Price",
                 "Order Size", "PnL", "QTY", "Total QTY", "Total Volume", "Required Funds"]

 

sum_price_deviation = 0
sum_volume = base_order

if static_price is not None:
    base_price = static_price
else:
    base_price = get_price(coin)
sum_qty = base_order / base_price
avg_price = base_price
total_funds = sum_volume / leverage
 
x.add_row(["BO", 0, round(base_price, 2), round(avg_price, 2), base_order, 0, round(sum_qty, 2), round(sum_qty, 2), base_order, total_funds])


for i in range(max_safety_orders):   
    sum_price_deviation = price_deviation + sum_price_deviation
    sum_volume = safety_order + sum_volume
    price = (base_price / 100) * (100 - sum_price_deviation)
    qty = safety_order / price
    sum_qty = sum_qty + qty
    avg_price = sum_volume / sum_qty
    pnl = (price * sum_qty) - sum_volume
    total_funds = (sum_volume / leverage) + abs(pnl)
   

    x.add_row([i+1, round(sum_price_deviation, 2), round(price, 2), round(avg_price, 2),
               round(safety_order, 2), round(pnl, 2), round(qty, 2), round(sum_qty, 2),
               round(sum_volume, 2), round(total_funds, 2)])
 
    # UPDATE VALUES #

    if i !=9:
        price_deviation = price_deviation * safety_order_step_scale
        safety_order = safety_order * safety_order_volume_scale
 

sum_price_deviation = additionnal_dump + sum_price_deviation
price = (base_price / 100) * (100 - sum_price_deviation)
pnl = (price * sum_qty) - sum_volume
total_funds = (sum_volume / leverage) + abs(pnl)
x.add_row(["Additional Price Dump({}%)".format(additionnal_dump), round(sum_price_deviation, 2), round(price, 2), round(avg_price, 2),
               " - - - ", round(pnl, 2), " - - - ", round(sum_qty, 2),
               round(sum_volume, 2), round(total_funds, 2)])
 

print(x)
