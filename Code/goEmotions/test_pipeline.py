from multilabel_pipeline import MultiLabelPipeline
from transformers import ElectraTokenizer
from model import ElectraForMultiLabelClassification
from pprint import pprint
import pandas as pd


tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-v3-goemotions")
model = ElectraForMultiLabelClassification.from_pretrained("monologg/koelectra-base-v3-goemotions")

goemotions = MultiLabelPipeline(
    model=model,
    tokenizer=tokenizer,
    threshold=0.3
)

def survey_load(path):
    global s_result
    s_result=pd.read_excel('../../Data/User_Raw_Data/'+path+'.xlsx', engine='openpyxl')

user_config="YGN01"
survey_load(user_config)

def result_adding(target, content):
    temp=goemotions(content)
    labels=[]
    scores=[]
    for senti in temp:
        labels.append(senti['labels'])
        scores.append(senti['scores'])
    s_result[target+'label']=labels
    s_result[target+'score']=scores

answer_list=s_result['Answer'].tolist()
question_list=s_result['Question'].tolist()
full_list=[]
for i in range(len(answer_list)):
    full_list.append(str(answer_list[i]+question_list[i]))


result_adding('Question', question_list)
result_adding('Answer', answer_list)
result_adding('Full', full_list)

    
writer=pd.ExcelWriter('../../Data/User_Raw_Data/'+user_config+'_senti_result_v3.xlsx', engine='openpyxl')
s_result.to_excel(writer, "Result")
writer.close()

# pprint(goemotions(texts))