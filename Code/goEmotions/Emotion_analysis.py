# -*- coding:utf-8 -*-

import json
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
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


for i in range(10):
    answer=input("user>")
    res=goemotions(answer)
    print(res)
    print("\n")
