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

def result_adding(target, content):
    temp=goemotions(content)
    labels=[]
    scores=[]
    for senti in temp:
        labels.append(senti['labels'])
        scores.append(senti['scores'])
    s_result[target+'label']=labels
    s_result[target+'score']=scores

# testing=["마트에서 물고기를 샀다. ",
# "먹는 고기가 아니고 열대어다. ",
# "살때, 너무 설레고 기뻤다. ",
# "열대어는 물을 따뜻하게 해줘야한다.",
# "먹이는 3일 후부터 줄 수 있다. ",
# "열대어는 배가 고파서 한마리가 ",
# "죽으면 다른 열대어를 잡아먹는다고 한다.",
# "그런 점은 조금 끔찍하다.",
# "밥을 꾸준히 줘야겠다. ",
# "관찰 일기도 써보면 좋겠다." ]
testing="이 사진은 휴가 삼아 다녀온 제주도 야  아름다운 가을 풍경을 감상할 수 있었어 여행코스는 한라산 오도 호수 너무너무 행복해"
print(goemotions(testing))
user_config="YGN01"
survey_load(user_config)


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