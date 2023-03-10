import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('sample.csv')
json_data = data.to_json()
print(json_data)
