import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

college = pd.read_csv("College.csv", delimiter = ',', index_col = 0, header = 0)
print(college.describe())

plt.subplot(1, 2, 1)
plt.boxplot(college["Outstate"])
plt.subplot(1, 2, 2)
plt.boxplot(college["Enroll"])
#plt.show()

Elite = pd.Series(["No"]*(college.shape[0]), index = college.index)
Elite[college["Top10perc"] > 50] = "Yes"
college["Elite"] = Elite.astype('category')

print(college.describe())

plt.clf()
college.boxplot(column = "Outstate", by = "Elite")
#plt.show()

Auto = pd.read_csv("Auto.csv", delimiter = ',')
print(Auto.describe())

Auto = Auto.drop(Auto.index[list(range(10, 86))])
print(Auto.describe())
