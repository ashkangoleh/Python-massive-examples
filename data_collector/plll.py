import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import os
file = os.path.join(os.path.dirname(__file__))
data = pd.read_csv(file+"/09.csv")

x = data['output_value'][:10]
y = data['block_timestamp'][:10]
# trb = data['block_timestamp']
# ax = tr.plot()
# ax.set_xticks(range(len(tr)))
# ax.set_xticklabels(["%s-%02d" % item for item in tr.index.tolist()],
# rotation=45, ha='center')

# plt.title("Daily Number of Bitcoin Transcations in 2017")
# plt.show()
# plt.savefig("Playground/Daily Bitcoin Transcations 2017.png")

fig, ax = plt.subplots()
ax.plot(x,y)
start, end = ax.get_xlim()
# ax.xaxis.set_ticks(np.arange(start, end, 0.712123))
# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
plt.show()