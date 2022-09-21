# -*- coding:utf-8 -*-

import json
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

a_list=[]
targets=['Mother', 'Father', 'Family', 'Female', 'Male', 'Marriage', 'Friend', 'Authority', 'Fear', 'Guilty', 'SelfAbility', 'Past', 'Future', 'Goal']


def survey_load():
    global q_list
    q_list=pd.read_excel('../Data/Survey_List.xlsx')

user_result=dict()
user_result['name']="노여경"
user_result["number"]="01"


survey_load()

# print(q_list)
for i, question in enumerate(q_list['Question']):
    answer=input("Q"+str(i+1)+":"+question)
    a_list.append(" "+answer)

q_list['Answer']=a_list

for tar in targets:
    temp_pd=q_list[(q_list['Target']==tar)]
    print(temp_pd)

writer=pd.ExcelWriter('../Data/User_Raw_Data/'+user_result['name']+user_result['number']+'.xlsx', engine='openpyxl')
q_list.to_excel(writer, "Result")
writer.close()