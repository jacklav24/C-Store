import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

constructor_standings = pd.read_csv('./c_store.csv')

sns.swarmplot(x="Item", y="Price", data=constructor_standings);

plt.show()