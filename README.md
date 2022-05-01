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

Output:

+-----------------------------+-----------------+----------+---------------+------------+---------+---------+-----------+--------------+----------------+
|        Safety Order #       | Price Deviation |  Price   | Avarage Price | Order Size |   PnL   |   QTY   | Total QTY | Total Volume | Required Funds |
+-----------------------------+-----------------+----------+---------------+------------+---------+---------+-----------+--------------+----------------+
|              BO             |        0        | 38418.58 |    38418.58   |    105     |    0    |   0.0   |    0.0    |     105      |      5.25      |
|              1              |        1        | 38034.4  |    38321.81   |     35     |  -1.05  |   0.0   |    0.0    |     140      |      8.05      |
|              2              |       2.15      | 37592.58 |    38110.59   |    56.0    |  -2.66  |   0.0   |    0.01   |    196.0     |     12.46      |
|              3              |       3.47      | 37084.5  |    37782.62   |    89.6    |  -5.28  |   0.0   |    0.01   |    285.6     |     19.56      |
|              4              |       4.99      | 36500.2  |    37344.12   |   143.36   |  -9.69  |   0.0   |    0.01   |    428.96    |     31.14      |
|              5              |       6.74      | 35828.25 |    36801.62   |   229.38   |  -17.41 |   0.01  |    0.02   |    658.34    |     50.33      |
|              6              |       8.75      | 35055.52 |    36156.99   |   367.0    |  -31.24 |   0.01  |    0.03   |   1025.34    |      82.5      |
|              7              |      11.07      | 34166.87 |    35406.01   |   587.2    |  -56.44 |   0.02  |    0.05   |   1612.54    |     137.06     |
|              8              |      13.73      | 33144.93 |    34538.61   |   939.52   | -102.98 |   0.03  |    0.07   |   2552.06    |     230.58     |
|              9              |      16.79      | 31969.7  |    33539.59   |  1503.24   | -189.82 |   0.05  |    0.12   |    4055.3    |     392.58     |
|              10             |       20.3      | 30618.18 |    32389.07   |  2405.18   | -353.23 |   0.08  |    0.2    |   6460.48    |     676.25     |
| Additional Price Dump(4.7%) |       25.0      | 28812.51 |    32389.07   |   - - -    |  -713.4 |  - - -  |    0.2    |   6460.48    |    1036.42     |
+-----------------------------+-----------------+----------+---------------+------------+---------+---------+-----------+--------------+----------------+
