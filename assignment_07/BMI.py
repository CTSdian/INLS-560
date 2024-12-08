#https://goheels.com/sports/mens-basketball/roster
import pandas as pd

lines = open('Player_Data.csv','r').readlines()
body = lines[1:]

first_name = []
last_name = []
height = []
weight = []

for line in body:
    tmp = line.split(',')
    first_name.append(tmp[0])
    last_name.append(tmp[1])
    height.append(tmp[5])
    weight.append(tmp[6])

player = {"Last Name": last_name,
          "First Name": first_name,
          "Height": height,
          "Weight": weight}

data = pd.DataFrame(player)
data["Height"] = data["Height"].astype('int')
data["Weight"] = data["Weight"].astype('int')

data["BMI"] = ((data["Weight"])*703)/((data["Height"])**2)

print(data)
data.to_csv("BMI.csv")