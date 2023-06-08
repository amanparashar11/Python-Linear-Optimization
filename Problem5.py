# Python code

# Step 1 - importing pandas and pulp library

import pandas as pd
import pulp as pl

# Step 2 - Prepare the input data

file_name = 'LP_Assignment_Aman_Parashar_DataSet61.xlsx'


df = pd.read_excel(file_name, "Problem5",
                   index_col=0)

product = df.loc[df.index[0], df.columns[0:-1]].to_dict()

constraint_matrix = pd.DataFrame(df, index=df.index[1:],
                                 columns=df.columns[0:-1]).to_dict('index')


rhs_coefficients = df.loc[df.index[1:], df.columns[-1]].to_dict()

# step 3 - lp model

model1 = pl.LpProblem("The_Napkins_Problem", pl.LpMinimize)

variables = pl.LpVariable.dicts('amount', product, lowBound=0)

model1 += pl.lpSum([product[i]*variables[i] for i in product])
print(model1)
# add constraints to the model; format like Ax<=b
for c in rhs_coefficients:
    model1 += pl.lpSum(constraint_matrix[c][u]*variables[u]for u in product
                       ) == rhs_coefficients[c], c  # c is constraint name
print(model1)

model1.solve()  # solve the problem with the default solver

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[model1.status])

# The optimised objective function value is printed to the screen
print("Total Revenue = ", pl.value(model1.objective))
# Each of the variables is printed with it's resolved optimum value
if (pl.LpStatus[model1.status] == 'Optimal'):
    for v in model1.variables():
        print(v.name, "=", v.varValue)

model1.writeLP("The_Napkins_Problem.lp")



