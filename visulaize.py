import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('ggplot')

list_file = ["EUR","CAD","CHF","GBP"]

data = pd.read_csv("CUR-AUD.csv",parse_dates=['DATE'])
data.rename(columns={'RATE':'AUD'},inplace=True)

for a in list_file:
	sample = pd.read_csv("CUR-"+a+".csv")
	data[a] = sample['RATE']

data.set_index('DATE',inplace=True)

fig, ax = plt.subplots(figsize=(5,5))

for label in ax.xaxis.get_ticklabels():
	label.set_rotation(45)

ax.xaxis.label.set_color('b')
ax.yaxis.label.set_color('b')

data.plot(ax=ax,linewidth = 0.85)

#ax.grid(True, color='black', linestyle='-', alpha=0.1)

plt.ylabel('EXCHANGE RATES (in USD)')

plt.show()