# futures_dca_calculator
Binance Futures Anti-Liquidation Bot Calculator.

#Idea from https://www.3cstats.com/leverage-bot-calculator/

Edit the fields in the configuration section:

# # # # # # # # # # CONFIGURATION # # # # # # # # # #


coin = "bitcoin"                  #coin name for dca simualtion<br/>
static_price = None               #static price instead of price lookup from coingecko, if set as number, script wont execute price lookup, set to None to disable<br/>
leverage = 20                     #leverage used<br/>
base_order = 105                  #base order<br/>
safety_order = 35                 #first safety order<br/>
safety_order_step_scale = 1.15    #safety order steps will grow by this multiplier<br/>
safety_order_volume_scale = 1.6   #safety order volumes will grow by this multiplier<br/>
max_safety_orders = 10            #maximum amount of safety orders<br/>
price_deviation = 1               #starting price deviation, will trigger the first safety order<br/>
additionnal_dump = 4.7            #extra dump after the last safety order was filled (%)<br/>

 
# # # # # # # # # # CONFIGURATION # # # # # # # # # #

Output:<br/>

![image](https://user-images.githubusercontent.com/49832565/166158905-a80cdf9c-2769-42fc-b34a-a74915f21e6b.png)
