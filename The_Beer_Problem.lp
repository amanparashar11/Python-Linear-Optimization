\* The_Beer_Problem *\
Maximize
OBJ: 0.95 amount_beer1 + 1.45 amount_beer2 + 1.15 amount_beer3
Subject To
budget(£/pint): 1.3 amount_beer1 + 0.8 amount_beer2 + 1.1 amount_beer3 <= 2100
demand_1: amount_beer1 <= 500
demand_2: amount_beer2 <= 600
demand_3: amount_beer3 <= 450
stock_capacity: amount_beer1 + amount_beer2 + amount_beer3 <= 1240
End
