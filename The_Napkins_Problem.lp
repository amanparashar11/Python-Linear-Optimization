\* The_Napkins_Problem *\
Minimize
OBJ: 0.12 amount_F1 + 0.12 amount_F2 + 0.12 amount_F3 + 0.12 amount_F4
 + 0.25 amount_N1 + 0.25 amount_N2 + 0.25 amount_N3 + 0.25 amount_N4
 + 0.06 amount_S1 + 0.06 amount_S2 + 0.06 amount_S3 + 0.06 amount_S4
Subject To
day1: amount_N1 = 14
day2: amount_F2 + amount_N2 + amount_S2 = 14
day2_constraint: amount_S2 = 2
day3: amount_F3 + amount_N3 + amount_S3 = 10
day3_constraint: amount_S3 = 0
day4: amount_F4 + amount_N4 + amount_S4 = 7
day4_constraint: amount_S4 = 0
End
