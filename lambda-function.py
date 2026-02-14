import json
import pandas as pd
import requests


def lambda_handler(event,context):
    
    print('event data ->',event)
    response = requests.get('https://google.com/')
    print(response.text)

    d = {'col1':[1,2], 'col2':[3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Demo Completed !!!')

    return response.text