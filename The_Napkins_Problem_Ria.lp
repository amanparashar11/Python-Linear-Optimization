\* The_Napkins_Problem *\
Minimize
OBJ: 0.16 amount_F1 + 0.16 amount_F2 + 0.16 amount_F3 + 0.16 amount_F4
 + 0.26 amount_N1 + 0.26 amount_N2 + 0.26 amount_N3 + 0.26 amount_N4
 + 0.09 amount_S1 + 0.09 amount_S2 + 0.09 amount_S3 + 0.09 amount_S4
Subject To
day1: amount_N1 = 17
day2: amount_F2 + amount_N2 + amount_S2 = 17
day2_constraint: amount_S2 = 1
day3: amount_F3 + amount_N3 + amount_S3 = 16
day4: amount_F4 + amount_N4 + amount_S4 = 15
End
