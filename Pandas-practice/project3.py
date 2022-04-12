import pandas as pd

### Read CSV --------------
csv1 = pd.read_csv("project1.1.csv")
csv2 = pd.read_csv("project1.2.csv")

## merge both 2 Csv by inner join-----------
df = pd.merge(csv1, csv2, how="inner", on=["Customer ID"])

### Drop Duplicates---------------
df = df.drop_duplicates(subset=['Customer ID'], keep='last')

###### to remove NaN value------------
df = df.dropna()

#####remove unwanted columns fromdataframe
df.drop(['Term_x','Years in current job_x',
       'Home Ownership_x', 'Purpose_x', 'Monthly Debt_x',
       'Years of Credit History_x', 'Months since last delinquent_x',
       'Number of Open Accounts_x', 'Number of Credit Problems_x',
       'Current Credit Balance_x', 'Maximum Open Credit_x', 'Bankruptcies_x',
       'Tax Liens_x', 'Loan ID_y', 'Loan Status', 'Current Loan Amount_y',
       'Term_y', 'Credit Score_y', 'Annual Income_y', 'Years in current job_y',
       'Home Ownership_y', 'Purpose_y', 'Monthly Debt_y',
       'Years of Credit History_y', 'Months since last delinquent_y',
       'Number of Open Accounts_y', 'Number of Credit Problems_y', 'Bankruptcies_y',
       'Tax Liens_y'], axis=1, inplace=True)

########## Rename column Name
df.rename(columns = {'Loan ID_x':'Loan ID','Current Loan Amount_x':'Loan Amount','Credit Score_x':'Credit Score',
                    'Annual Income_x':'Annual Income','Current Credit Balance_y':'Current Credit Balance'
                    ,'Maximum Open Credit_y':'Maximum Open Credit'}, inplace = True)

print(df)