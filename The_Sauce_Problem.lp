\* The_Sauce_Problem *\
Maximize
OBJ: 4 amount_x11 + 3.5 amount_x12 + 4 amount_x21 + 3.5 amount_x22
 + 4 amount_x31 + 3.5 amount_x32 + 4 amount_x41 + 3.5 amount_x42
Subject To
Cabagge_Total_AL: amount_x11 + amount_x12 <= 480
Cabbage_AG: - 0.35 amount_x11 + 0.65 amount_x21 + 0.65 amount_x31
 + 0.65 amount_x41 <= 0
Cabbage_AL: 0.3 amount_x11 - 0.7 amount_x21 - 0.7 amount_x31 - 0.7 amount_x41
 <= 0
Oil_AG: 0.06 amount_x11 + 0.06 amount_x21 + 0.06 amount_x31 - 0.94 amount_x41
 <= 0
Oil_AL: - 0.12 amount_x11 - 0.12 amount_x21 - 0.12 amount_x31
 + 0.88 amount_x41 <= 0
Oil_BG: 0.09 amount_x12 + 0.09 amount_x22 + 0.09 amount_x32 - 0.81 amount_x42
 <= 0
Oil_BL: - 0.12 amount_x12 - 0.12 amount_x22 - 0.12 amount_x32
 + 0.88 amount_x42 <= 0
Onion_AG: 0.05 amount_x11 + 0.05 amount_x21 - 0.95 amount_x31
 + 0.05 amount_x41 <= 0
Onion_AL: - 0.12 amount_x11 - 0.12 amount_x21 + 0.88 amount_x31
 - 0.12 amount_x41 <= 0
Onion_BG: 0.06 amount_x12 + 0.06 amount_x22 - 0.94 amount_x32
 + 0.06 amount_x42 <= 0
Onion_BL: - 0.12 amount_x12 - 0.12 amount_x22 + 0.88 amount_x32
 - 0.12 amount_x42 <= 0
Onion_Total_AL: amount_x31 + amount_x32 <= 200
Sell: - 1.4 amount_x11 + amount_x12 - 1.4 amount_x21 + amount_x22
 - 1.4 amount_x31 + amount_x32 - 1.4 amount_x41 + amount_x42 <= 0
Tomato_BG: 0.7 amount_x12 - 0.3 amount_x22 + 0.7 amount_x32 + 0.7 amount_x42
 <= 0
Tomato_BL: - 0.75 amount_x12 + 0.25 amount_x22 - 0.75 amount_x32
 - 0.75 amount_x42 <= 0
Tomato_Total_AL: amount_x21 + amount_x22 <= 470
Total_BL: amount_x11 + amount_x12 + amount_x21 + amount_x22 + amount_x31
 + amount_x32 + amount_x41 + amount_x42 <= 490
End
