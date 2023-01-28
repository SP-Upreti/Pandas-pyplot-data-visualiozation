import pandas as pd
from matplotlib import pyplot as pp
import numpy as np

data = pd.read_csv("National_Population_data.csv")
# print(data)


labell = data["Local Level Name"]

# pp.bar(labell, male)
# pp.show()

mimimum = data["Total population"].min()
mini = data[data["Total population"] == mimimum]
# print(mini)

max = data[data["Total population"] == data["Total population"].max()]
maxx = max["District"]
print(f"The maximum population is  {max}")

# print(data[data["District"] == "Kathmandu"])

ktm_population = data[data["District"] == "Kathmandu"]["Total population"].sum()

print(ktm_population)

male = data[data["District"] == "Kathmandu"]["Total Male"].to_list()
print(male)

female = data[data["District"] == "Kathmandu"]["Total Female"].to_list()
print(female)


municipality = data[data["District"] == "Kathmandu"]["Local Level Name"].to_list()
print(municipality)


#showing population of male and female in multiple bar graph

width = 0.4

bar1 = np.arange(len(municipality))

bar2 = [x+width for x in bar1]
pp.bar(bar1, male,width, label = "Boys")
pp.bar(bar2, female,width, label = "Girls")
pp.xticks(bar1, municipality,rotation = 10, fontsize = 8)


pp.legend()
pp.title("Bar graph showing male/female population of different municipality of Kathmandu")
pp.xlabel("Municipality")
pp.ylabel("Population")



pp.show()