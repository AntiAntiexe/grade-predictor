import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy import stats

x = np.random.normal(16.0, 5.0, 200)

y = np.random.normal(76, 15.0, 200)

plt.scatter(x, y)
plt.show()

print(x)
print(y)
