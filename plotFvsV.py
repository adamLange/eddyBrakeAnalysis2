import pandas as pd
import matplotlib.pyplot as plt
import re
import os

exportDir = r'C:\Users\adam\Documents\eddyBrake\Analysis2\export'

pFile = re.compile(r'[0-9]*\.csv')

fvsv = pd.read_csv(exportDir+r'\legend.csv')
#fvsv = fvsv.sort(['h','v'])

for i in range(len(fvsv)):

  fname = exportDir+'\\'+str(int(fvsv.iloc[i]['name']))+'.csv'
  try:
    df = pd.read_csv(fname) #

    fx = df.iloc[-1]['Force1.Force_x [newton]']
    fy = df.iloc[-1]['Force1.Force_y [newton]']

    fvsv.loc[i,'F_x'] = fx
    fvsv.loc[i,'F_y'] = fy
  except:
    print('{} does not exist, skipping'.format(fname))


for h in fvsv['h'].unique():
  df = fvsv[fvsv['h']==h]
  df = df.sort_values(['v'])
  print(df)
  plt.plot(df['v'],df['F_x'],'-',label='h = {}'.format(h))
  plt.plot(df['v'],df['F_y'],'--',label='h = {}'.format(h))

plt.legend()
plt.title('- F_x, -- F_y\n h [m]')
plt.xlabel('Velocity [ms]')
plt.ylabel('Force [N]')
plt.grid()
plt.show()

