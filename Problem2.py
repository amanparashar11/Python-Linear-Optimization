# Python code﻿

# step # 1 - importing pulp and pandas

import pulp as pl
import pandas as pd

# step 2 - preparing the input data

file_name = 'LP_Assignment_Aman_Parashar_DataSet61.xlsx'
df = pd.read_excel(file_name, "Problem2", index_col=0)
print(df)


# data frame excluding all the demand and maximum avail hours

new_frame=pd.DataFrame(
    df, index=df.index[0:-1], columns=df.columns[0:-1])
print('new data frame \n',new_frame)

# manager score matrix

score_matrix = pd.DataFrame(
    df, index=df.index[0:-1], columns=df.columns[0:-1]).to_dict('index')

print(score_matrix)

# creating demand matrix

demand = df.loc[df.index[-1], df.columns[0:-1]].to_dict()
print(demand)


# creating maximum avail hours matrix

avail_hrs = df.loc[df.index[0:-1], df.columns[-1]].to_dict()
print(avail_hrs)

# step 3 - model

model = pl.LpProblem("Manager_Problem", pl.LpMaximize)

# Creates a dictionary of variables. There is a continuous variable 
# for each max_avail_hrs_demand pair
variables = pl.LpVariable.dicts('score', (avail_hrs, demand), lowBound=0)

print(variables)

# Creates the objective function
model += pl.lpSum([score_matrix[i][j]*variables[i][j] for i in avail_hrs
                    for j in demand])
print(model)
# Adds a constraint to ensure no supply point delivers more than its capacity
for i in avail_hrs:
    model += pl.lpSum([variables[i][j] for j in demand]) <= avail_hrs[i]
print(model)

# Adds a constraint to ensure each demand point receives exactly as much 
# as its demand
for j in demand:
    model += pl.lpSum([variables[i][j] for i in avail_hrs]) == demand[j]
print(model)
# Solves the problem with the default solver
model.solve()

# The status of the solution is printed to the screen: For an LP, it can be 
# either infeasible, optimal, or unbounded
print("Status:", pl.LpStatus[model.status])

# The optimised objective function value is printed to the screen if 
# the problem is optimal
print("Total Score = ", pl.value(model.objective), '\n\nThe allocation of score:')

# Each of the variables is printed with it's resolved optimum value, 
# if the solution is found
if (pl.LpStatus[model.status] == 'Optimal'):
    for i in avail_hrs:
        for j in demand:
            print(variables[i][j].varValue, end='   ')
        print('\n')

# The problem data is written to an .lp file
model.writeLP("ManagerProblemWithDict.lp")
