import pandas as pd
import matplotlib.pyplot as plt
import re
import os

exportDir = r'C:\Users\adam\Documents\eddyBrake\Analysis2\export'

pFile = re.compile(r'[0-9]*\.csv')

for directory,dirs,files in os.walk(exportDir):
  for f in files:
    if pFile.match(f):
      df = pd.read_csv(directory+'/'+f)
      plt.plot(df['Time [ms]'],df['Force1.Force_x [newton]'],'b')
      plt.plot(df['Time [ms]'],df['Force1.Force_y [newton]'],'b--')

plt.xlabel('time [s]')
plt.ylabel('Force [n]')
plt.show()
