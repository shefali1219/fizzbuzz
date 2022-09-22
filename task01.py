# -*- coding: utf-8 -*-
"""task01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ByiXZ5RlhEvazo3Pcdwp23_lqW0ve6p
"""

import pandas as CSVreader
rdata = CSVreader.read_csv("Trails.csv")
#print(rdata)
#rdata.sort_values(rdata.columns[0], axis=0,inplace=True)

name_good = rdata[(rdata['CONDITION'] == 'GOOD')]
name_nan = rdata[(rdata['CONDITION'] == ' ')]
name_marginal = rdata[(rdata['CONDITION'] == 'MARGINAL')]
name_poor = rdata[(rdata['CONDITION'] == 'POOR')]

good_list = name_good["TRAIL_NAME"]
poor_list = name_poor["TRAIL_NAME"]
marginal_list = name_marginal["TRAIL_NAME"]
blank_list = name_nan["TRAIL_NAME"]

type(good_list)

#print(good_list)
#print(poor_list)
#print(marginal_list)
#print(blank_list)

installation_year = rdata[(rdata['INST_YEAR'] > 2000)]
count = len(installation_year)
print("The number of trail greater than 2000 is ",count)
print(installation_year)



active_trails = rdata[(rdata['STATUS'] ==  "ACTIVE")]
print("Active trails are:", len(active_trails))

lighting = rdata[(rdata['LIGHT'] == "Yes")]
print("Trails with light:", len(lighting))

walking = rdata[(rdata['WALKING'] == "Yes")]
walkingandbiking =  walking[(walking['BIKING']) == "Yes"]

print("Trails with walking and biking",len(walkingandbiking))



rdata = CSVreader.read_csv("Trails.csv")
hike = rdata[(rdata['HIKING'] == "Yes")]
hikeandbike = hike[(hike['BIKING'] == "Yes")]

resultTuple = ()

for i, row in hikeandbike.iterrows():
  resultTuple = resultTuple + ((row["TRAIL_NAME"],row["CONDITION"],row["LIGHT"],row["STATUS"],row["HIKING"],row["BIKING"],row["ATV"]))

print(resultTuple)

#mytuple = hikeandbike(hikeandbike["Trail Name", "General Condition", "Lighting", "Status", "Hiking", "Biking", "ATV)"])

