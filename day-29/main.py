from urllib.request import urlopen
import json
import pandas as pd

response = urlopen('https://blockchain.info/ticker')
json_data = response.read().decode('utf-8', 'replace')

d = json.loads(json_data)
df = pd.json_normalize(d['ARS'])

