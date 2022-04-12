import pandas as pd
import datetime

df = pd.read_csv('project2.csv')

####### count column value----------
# df['type'].value_counts()
# df.type.value_counts().saveings

#####remove unwanted columns fromdataframe
df.drop(['repeipt', 'type','before_available_ammount','ammount','card_type'], axis=1, inplace=True)

############ change date formet--------------
df['date']=pd.to_datetime(df['date'], format='%d/%m/%Y')
######## check day from date
df['day'] = df['date'].dt.day_name()     

##### delete column-------------------
# del df['day']

######## show only that data which have sbi_bank in column = atm
# df = df[df.atm =='sbi_bank']

#####short data by date--------------
# df =df.sort_values(by='date', ascending=False)

### get data by year----------------
### method 1
#  df['year'] = pd.DatetimeIndex(df['date']).year
#  df = df[df['year']==2018]

### method 2
# df = df[df['date'].dt.year == 2018]

########### replace account no X with space
#### method 1
df["account_no"]=df["account_no"].str.replace("X","")
df["transtation_no"]=df["transtation_no"].str.replace("#","")
#method 2
# df['account_no'] = df['account_no'].map(lambda x: x.replace('X',''))

df.rename(columns = {'after_available_amount':'current_balance'}, inplace = True)

print(df)