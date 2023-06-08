# Python code

#### Notes #####
#For this problem, I've uploaded 3 excel files to python dataframe
#1. Problem3_Supply -> Supply df
#2. Problem3_demand -> Demand_df
#3. Problem3_cost -> Cost_df
###############


############################ Step 1 - importing the libraries
import pulp as pl
import pandas as pd

############################ Step 2 - preparing the input data
file_name = 'LP_Assignment_Aman_Parashar_DataSet61.xlsx'

# reading supply df
supply_df = pd.read_excel(file_name, "Problem3_Supply", index_col=0)
print(supply_df)


# reading demand df
demand_df = pd.read_excel(file_name, "Problem3_demand", index_col=0)
print(demand_df)
type(demand_df)


# reading cost df
cost_df = pd.read_excel(file_name, "Problem3_cost", index_col=0)
print(cost_df)

new_frame=pd.DataFrame(
    supply_df, index=supply_df.index[0:], columns=supply_df.columns[0:-1])
print('new data frame \n',new_frame)

units_matrix = pd.DataFrame(
    supply_df, index=supply_df.index[0:], columns=supply_df.columns[0:-1]).to_dict('index')

cost_matrix = pd.DataFrame(
    cost_df, index=cost_df.index[0:], columns=cost_df.columns[0:]).to_dict('index')


demand = demand_df.loc[demand_df.index[-1], demand_df.columns[0:]].to_dict()



prod_demand = demand_df.loc[demand_df.index[:-1], demand_df.columns[0:]].to_dict()
print(prod_demand)


supply = supply_df.loc[supply_df.index[0:], supply_df.columns[-1]].to_dict()


####################################### Step 3 - model

model = pl.LpProblem("Transportation_Problem", pl.LpMinimize)


variables = pl.LpVariable.dicts('amount', (supply, demand), lowBound=0)



# Creates the objective function
model += pl.lpSum([cost_matrix[i][j]*variables[i][j] for i in supply
                    for j in demand])


# Adds a constraint to ensure no supply point delivers more than its capacity
for i in supply:
    model += pl.lpSum([variables[i][j] for j in demand]) <= supply[i]



# adds demand constraint
for j in demand:
        model += pl.lpSum([prod_demand[j][i]*variables[i][j] for i in supply
                    ]) == demand[j]
        

print(model)

# Solves the problem with the default solver
model.solve()

# The status of the solution is printed to the screen: For an LP, it can be 
# either infeasible, optimal, or unbounded
print("Status:", pl.LpStatus[model.status])

# The optimised objective function value is printed to the screen if 
# the problem is optimal
print("Total Cost = ", pl.value(model.objective), '\n\nThe allocation of units:')

# Each of the variables is printed with it's resolved optimum value, 
# if the solution is found
if (pl.LpStatus[model.status] == 'Optimal'):
    for i in supply:
        for j in demand:
            print(variables[i][j].varValue, end='   ')
        print('\n')

# The problem data is written to an .lp file
model.writeLP("TransportationProblemWithDict.lp")

