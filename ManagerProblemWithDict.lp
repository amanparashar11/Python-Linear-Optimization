\* Manager_Problem *\
Maximize
OBJ: 50 score_b1_p1 + 50 score_b1_p2 + 60 score_b1_p3 + 80 score_b1_p4
 + 70 score_b2_p1 + 80 score_b2_p2 + 80 score_b2_p3 + 70 score_b2_p4
 + 50 score_b3_p1 + 20 score_b3_p2 + 30 score_b3_p3 + 50 score_b3_p4
Subject To
_C1: score_b1_p1 + score_b1_p2 + score_b1_p3 + score_b1_p4 <= 89
_C2: score_b2_p1 + score_b2_p2 + score_b2_p3 + score_b2_p4 <= 89
_C3: score_b3_p1 + score_b3_p2 + score_b3_p3 + score_b3_p4 <= 89
_C4: score_b1_p1 + score_b2_p1 + score_b3_p1 = 70
_C5: score_b1_p2 + score_b2_p2 + score_b3_p2 = 55
_C6: score_b1_p3 + score_b2_p3 + score_b3_p3 = 75
_C7: score_b1_p4 + score_b2_p4 + score_b3_p4 = 60
End
