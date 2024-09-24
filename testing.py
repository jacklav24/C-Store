import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

c_store_prices = pd.read_csv('./c_store.csv')

prices = c_store_prices[c_st]
sns.scatterplot(x="Item", y="Price", data=c_store_prices)

plt.show()