import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style


# x_data = np.random.random(50) *100
# y_data = np.random.random(50) * 100

# plt.scatter(x_data, y_data , c="red", marker="*", s=100, alpha=0.3) # scatters the data i a plot 
# # (c is for color) (marker is for points) (s is for size) (alpha is for transparency)

# year = [2006 + i for i in range(16)]
# x = ["C++", "C#", "python", "Java", "Go"]
# y = [20, 50, 140, 1, 45]
# plt.bar(x, y, color = "red", align= "edge", width=0.5, edgecolor = "black", lw = 5)
# # (align) is for aligning and (width) is for bars width 
# weight = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 81, 80, 79]

# plt.plot(year, weight, c = "black", lw = 3, linestyle = "--") # plot is default for line chart
# # (lw is for line width) (linestyle is for styling)
# plt.show() # necassary for showing

# ages = np.random.normal(20, 1.5, 1000)
# plt.hist(ages)

# years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
# income = [55, 56, 62, 61, 72, 72, 73, 75]

# income_ticks =list(range(50,81 ,2))

# plt.plot(years, income)
# plt.title("income of john (in USD)",fontsize = 30, fontname = "arielblack")
# plt.xlabel("year")
# plt.ylabel("yearly income in USD")
# plt.yticks(income_ticks, [f"{x}k$" for x in income_ticks])

# stock_a = [100, 102, 99, 101, 101, 100, 102]
# stock_b = [90, 95, 102, 104, 105, 103, 109]
# stock_c = [110, 115, 99, 160, 105, 100, 90, 95]

# plt.plot(stock_a, label = "company1")
# plt.plot(stock_b, label = "company2")
# plt.plot(stock_c, label = "company3")

# plt.legend(loc = "lower center")


# style.use("ggplot")
# votes = [10, 2, 5, 16, 22]
# people = ["A", "B", "C", "D", "E"]

# plt.pie(votes, labels=None)
# plt.legend(labels=people)
#plt.show()

# x1, y1 = np.random.random(100), np.random.random(100)
# x2, y2 = np.random.random(100), np.random.random(100)

# plt.figure(1)
# plt.scatter(x1, y1)
# plt.figure(2)
# plt.scatter(x2, y2)

# plt.show()

# x = np.arange(100)
# fig, axs = plt.subplots(2,2)

# axs[0, 0].plot(x, np.sin(x))
# axs[0, 0].set_title("sin wave")

# axs[0, 1].plot(x, np.cos(x))
# axs[0, 1].set_title("cosine wave")

# axs[1, 0].plot(x, np.random.random(100))
# axs[1, 0].set_title("random function")

# axs[1, 1].plot(x, np.log(x))
# axs[1, 1].set_title("log function")
# axs[1, 1].set_xlabel("TEST")

# fig.suptitle("Four plots")

# plt.tight_layout()
# plt.savefig("fourplot.png", dpi = 300, transparent = False

# program of showing temprature of 4 cities in 1 year (12 months) in a line chart, bar chart and a pie chart


# plt.bar(city_2, temperature_2,)
# plt.xlabel("months")
# plt.ylabel("temperature and humidity")
# plt.suptitle("Average Temperature of city in 1 year")
# plt.yticks(temperature_2, [f"{x}`C" for x in temperature_2])

# plt.pie(city_3, temperature_3)
# plt.xlabel("months")
# plt.ylabel("temperature and humidity")
# plt.suptitle("Average Temperature of city in 1 year")
# plt.yticks(temperature_3, [f"{x}`C" for x in temperature_3])



city_1 = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
temperature_1 = [12, 15, 22, 29, 34, 38, 35, 34, 32, 28, 20, 14]

city_2 = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
temperature_2 = [19, 22, 26, 29, 32, 34, 32, 31, 31, 30, 26, 21]

city_3 = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
temperature_3 = [10, 13, 18, 24, 30, 34, 31, 30, 29, 25, 18, 12]

city_4 = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
temperature_4 = [23, 45, 12, 9, 13, 33, 34, 35, 20, 35, 8, 7]
fig, axs = plt.subplots(2, 2, figsize=(10,12))  

# Line graph
axs[0, 0].plot(city_1, temperature_1, c="blue", lw = 2)
axs[0, 0].set_title("Temperature of Lahore (line chart)")
axs[0, 0].set_ylabel("Temperature (°C)")
axs[0, 0].set_yticks(temperature_1)
axs[0, 0].set_yticklabels([f"{x}°C" for x in temperature_1])

# Bar graph
axs[0, 1].bar(city_2, temperature_2, color="green", width = 0.5, align = "edge", edgecolor = "black")
axs[0, 1].set_title("Temperature of karachi (bar chart)")
axs[0, 1].set_ylabel("Temperature (°C)")
axs[0, 1].set_yticks(temperature_2)
axs[0, 1].set_yticklabels([f"{x}°C" for x in temperature_2])

axs[1, 0].hist(
    temperature_3,  # Data to plot
    bins=10,         # Number of bins (adjust as needed)
    color="cyan",  # Bar color
    edgecolor="black"  # Bin edge color
)
axs[1, 0].set_title("Temperature of Islamabad (histogram)")
axs[1, 0].set_xlabel("Temperature (°C)")
axs[1, 0].set_ylabel("Number of Months")

axs[1, 1].plot(city_4, temperature_4, c = "red", lw= 2)
axs[1, 1].set_title("Temperature of Multan (line chart)")
axs[1, 1].set_ylabel("Temperature (°C)")
axs[1, 1].set_yticks(temperature_4)
axs[1, 1].set_yticklabels([f"{x}°C" for x in temperature_4])


plt.suptitle("Average Temperature of Cities in 1 Year")
plt.tight_layout()
plt.savefig("tempratures.png", dpi = 300)
plt.show()