# --------------


# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
#bank_data = pd.read_csv(path)
bank = pd.read_csv(path)

#Step 1
categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var)


# STEP 2
#Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them.

banks = pd.DataFrame(bank.drop('Loan_ID',axis=1))
#print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode,inplace=True)

print(banks.shape)
print(banks.isnull().sum().values.sum())

#STEP 3
#Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person.

avg_loan_amount = pd.pivot_table(banks, index =['Gender', 'Married', 'Self_Employed'], values='LoanAmount',aggfunc='mean')
avg_loan_amount

#STEP 4
#Now let's check the percentage of loan approved based on a person's employment type.

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]

count = banks['Loan_Status'].count()
percentage_se = (loan_approved_se['Loan_Status'].count()/count)*100
percentage_nse = (loan_approved_nse['Loan_Status'].count()/count)*100

print(percentage_se)
print(percentage_nse)


#STEP 5
#A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.

banks['loan_term'] = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = banks['loan_term'][banks['loan_term']>=25].count()

print(big_loan_term)

#STEP 6
#Now let's check the average income of an applicant and the average loan given to a person based on their income

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)
#Code starts here




