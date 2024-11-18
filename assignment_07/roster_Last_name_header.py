#https://goheels.com/sports/mens-basketball/roster
import pandas as pd

lines = open('Last_Names.csv','r').readlines()
body = lines[1:]

df = pd.DataFrame(body,columns=['Last_Name'])

print(df)
