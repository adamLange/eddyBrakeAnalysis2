import pandas as pd

df = pd.read_csv('./export/legend.csv')

def averageOhmicLoss(df):
  print(df)

for i in range(len(df)):
  loadCaseName = str(int(df.loc[i,'name']))
  try:
    forceDf = pd.read_csv('./export/{}.csv'.format(loadCaseName))
    fDrag = forceDf.iloc[-1]['Force1.Force_x [newton]']
    fLift = forceDf.iloc[-1]['Force1.Force_y [newton]']
    
  except:
    fDrag = None
    fLift = None

  try:
    i2rDf = pd.read_csv('./export/{}_q.csv'.format(loadCaseName))
    tfCol = i2rDf.columns[-1]
    q_mean = i2rDf[i2rDf.columns[-1]].mean()
    q_max = i2rDf[i2rDf.columns[-1]].max()

  except:
    q = None

  df.loc[i,'F_drag'] = fDrag
  df.loc[i,'F_lift'] = fLift

  df.loc[i,'q_ibeam_surface_mean'] = q_mean
  df.loc[i,'q_ibeam_surface_max'] = q_max


df.to_csv('./export/eddyBrakeData.csv')
