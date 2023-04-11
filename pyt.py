import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a pandas DataFrame
df = pd.read_csv('job.csv')

# drop the 'Date' column
df = df.drop('Date', axis=1)

# convert numeric columns to string type
df = df.astype(str)

# calculate the ratio of cells with * to those without for each column
ratios = df.apply(lambda x: x.str.contains('\*').value_counts(normalize=True).get(True, 0)) * 10

# plot the ratios as a horizontal bar chart
fig, ax = plt.subplots()
ratios.plot(kind='barh', ax=ax)
ax.set_xlim([0, 10])
ax.set_xticks(range(0, 11, 1))
plt.xlabel('Ratio of cells with *')
plt.ylabel('Column')

# add sad emoji if the bar is less than or equal to 5
for i, v in enumerate(ratios):
    if v < 1:
        ax.text(v + 0.2, i, u'\U0001F622', fontsize=16, color='red') # \U0001F622

plt.show()
