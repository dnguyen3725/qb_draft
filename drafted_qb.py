from IPython.core.debugger import Tracer
import numpy as np
import pandas as pd
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")
sns.set_context("poster")

# Read in data
qb_data = pd.read_csv('drafted_qb.csv')

g = (sns.jointplot('Pick', 'CarAV', data=qb_data,
    #kind="hex", color='m',
    kind="kde", shade=True, shade_lowest=False, color='#fa9fb5',
    xlim=(0,300), ylim=(0,180), stat_func=None)
    .set_axis_labels("Draft Position", "Career Weighted Approximate Value"))

# Show plots
plt.show()