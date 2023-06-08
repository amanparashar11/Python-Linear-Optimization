# Python code

#### Notes #####

#1. Variables - Xij [ i- ingrediant (1 = cabbage, 2 = Tomato, 3 = onion, 4 = oil), j - (1 = Sauce A, 2= Sauce B)] 
#2. Col A - it lists the item_sauce combination ( at-least and at-max combinations)

###############

# Step 1 - importing pandas and pulp library

import pandas as pd
import pulp as pl

# Step 2 - Prepare the input data

file_name = 'Input_Linear_Optimization.xlsx'


df = pd.read_excel(file_name, "Problem4",
                   index_col=0)
print(df)


product = df.loc[df.index[0], df.columns[0:-1]].to_dict()
print(product)


constraint_matrix = pd.DataFrame(df, index=df.index[1:],
                                 columns=df.columns[0:-1]).to_dict('index')
print(constraint_matrix)


rhs_coefficients = df.loc[df.index[1:], df.columns[-1]].to_dict()
print(rhs_coefficients)


# step 3 - lp model

model1 = pl.LpProblem("The_Sauce_Problem", pl.LpMaximize)

variables = pl.LpVariable.dicts('amount', product, lowBound=0)

model1 += pl.lpSum([product[i]*variables[i] for i in product])
print(model1)

# add constraints to the model; format like Ax<=b

for c in rhs_coefficients:
    model1 += pl.lpSum(constraint_matrix[c][u]*variables[u]for u in product
                       ) <= rhs_coefficients[c], c  # c is constraint name
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
        
model1.writeLP("The_Sauce_Problem.lp")




