import matplotlib.pyplot as plt
import sys
import pandas as pd
from plotnine import ggplot, aes, geom_line, geom_histogram, geom_point, geom_col
import numpy as np



if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [filename.csv]")
    exit()


df = pd.read_csv(sys.argv[1])

df_byHouse = df.groupby(df["Hogwarts House"])

means = df_byHouse.mean(numeric_only=True).reset_index()
median = df_byHouse.median(numeric_only=True).reset_index()
std = df_byHouse.std(numeric_only=True).reset_index()
# u.drop(index='Hogwarts House',inplace=True)

data = pd.DataFrame(means,median,std)
print(data)
p = (
        ggplot(data)
        + aes(x="Hogwarts House", y = "Astronomy")
        + geom_col()
    )
print(p)
plt.show()