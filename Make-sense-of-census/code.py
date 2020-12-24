# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

#Step 1
census = np.concatenate((data,new_record))
#print(census.shape)

#Step 2
age = census[:,0]

max_age = age.max()
min_age = age.min()
age_mean = round(age.mean(),2)
age_std = round(age.std(),2)

print(age.max())
print(age.min())
print(round(age.mean(),2))
print(round(age.std(),2))


#Step-3

race_0 = census[:,2][census[:,2]==0]
race_1 = census[:,2][census[:,2]==1]
race_2 = census[:,2][census[:,2]==2]
race_3 = census[:,2][census[:,2]==3]
race_4 = census[:,2][census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

races = [race_0,race_1,race_2,race_3,race_4]
race_lengths = [len_0,len_1,len_2,len_3,len_4]

min_length = min(race_lengths)

min_length_index = race_lengths.index(min_length)
#print(min_length_index)
minority_race = races[min_length_index]
print(minority_race)


#Step 4

senior_citizens = census[:,:][census[:,0]>60]
#print(senior_citizens)
#print(senior_citizens.shape)
working_hours_sum = senior_citizens[:,6].sum()

senior_citizens_len = len(senior_citizens)

avg_working_hours = round((working_hours_sum/senior_citizens_len),2)

print(working_hours_sum)
print(avg_working_hours)


#Step 5

high = census[:,:][census[:,1]>10]
low = census[:,:][census[:,1]<=10]

avg_pay_high = round((high[:,7].mean()),2)
avg_pay_low = round((low[:,7].mean()),2)

print(avg_pay_high)
print(avg_pay_low)







