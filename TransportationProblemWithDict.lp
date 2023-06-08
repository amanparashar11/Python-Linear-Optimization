\* Transportation_Problem *\
Minimize
OBJ: 7 amount_supp1_site1 + 11 amount_supp1_site2 + 6 amount_supp2_site1
 + 9 amount_supp2_site2 + 8 amount_supp3_site1 + 8 amount_supp3_site2
Subject To
_C1: amount_supp1_site1 + amount_supp1_site2 <= 120
_C2: amount_supp2_site1 + amount_supp2_site2 <= 140
_C3: amount_supp3_site1 + amount_supp3_site2 <= 120
_C4: 0.9 amount_supp1_site1 + 0.6 amount_supp2_site1 + 0.7 amount_supp3_site1
 = 210
_C5: 0.8 amount_supp1_site2 + 0.7 amount_supp2_site2 + 0.7 amount_supp3_site2
 = 20
End
