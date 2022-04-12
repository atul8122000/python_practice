import pandas as pd


df = pd.read_csv("project1.csv")
df.head(2)

def operations( row: pd.Series) -> tuple:
    name = row["first_name"] +" "+ row["last_name"]
    Adderess = row['address'] +", "+row["city"]
    phone = row["phone1"] +", "+ row["phone1"]
    return name, Adderess, phone

list_of_columns = ['name', 'Adderess', 'phone']
df[list_of_columns]=df.apply(operations,axis=1,result_type='expand')
df =df.drop(['first_name','address', 'last_name','city','phone1','phone2'], axis=1)

df = df[[
    'name',
    'Adderess',
    'county',
    'postal',
    'phone',
    'company_name',
    'email',
    'web'  
]]

print(df)

