import pandas as pd
import matplotlib.pyplot as plt
import re
import os

exportDir = r'C:\Users\adam\Documents\eddyBrake\Analysis2\export'

pFile = re.compile(r'[0-9]*\.csv')

fvsh = pd.read_csv(exportDir+r'\legend.csv')

for i in range(len(fvsh)):

  fname = exportDir+'\\'+str(fvsh.iloc[i].name)+'.csv'
  try:
    df = pd.read_csv(fname) #'

    fx = df.iloc[-1]['Force1.Force_x [newton]']
    fy = df.iloc[-1]['Force1.Force_y [newton]']

    fvsh.loc[i,'F_x'] = fx
    fvsh.loc[i,'F_y'] = fy
  except:
    print('{} does not exist, skipping'.format(fname))


plt.scatter(fvsh['v'],fvsh['F_x'],label='F_x')

"""

plt.xlabel('time [s]')
plt.ylabel('Force [n]')
plt.show()

"""
