import requests
import sys
import json 
import pandas as pd
#response = requests.get('https://www.nature.com/articles/s41551-020-00682-w')

ma = pd.DataFrame({'V1':['a','b','c'], 'V2': ['d','e','f'], 'V3': ['g','h','i']})
lst = [True, True, False]
print(ma[lst])
