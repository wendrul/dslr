#!/usr/bin/env python

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

mmethi = df_byHouse.agg(['mean', 'median', 'std']).reset_index()

# mean(numeric_only=True).reset_index()
# means = means.assign(summary = "mean")
# median = df_byHouse.median(numeric_only=True).reset_index()
# median.assign(summary = "median")
# std = df_byHouse.std(numeric_only=True).reset_index()
# std.assign(summary = "std")
# u.drop(index='Hogwarts House',inplace=True)



def houseDistributionOn(course):
    mmethi = df_byHouse.agg({f"{course}": ['mean', 'median', 'std']})
    # mmethi.columns = [f'{course}_mean', f'{course}_median', f'{course}_std']
    mmethi = mmethi.reset_index()
    print(mmethi[course])
    return (
        ggplot(mmethi)
        + aes(x="summary", y=course, fill="Hogwarts House")
        + geom_col()
    )

print(houseDistributionOn("Astronomy"))
plt.show()