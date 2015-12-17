import pandas as pd

df = pd.read_csv('./export/legend.csv')

def averageOhmicLoss(df):
  print(df)

for i in range(len(df)):
  loadCaseName = str(int(df.loc[i,'name']))
  try:
    forceDf = pd.read_csv('./export/{}.csv'.format(loadCaseName))
    fLift = forceDf.iloc[-1]['Force1.Force_x [newton]']
    fDrag = forceDf.iloc[-1]['Force1.Force_y [newton]']
    
  except:
    fDrag = None
    fLift = None

  try:
    i2rDf = pd.read_csv('./export/{}_q.csv'.format(loadCaseName))
    tfCol = i2rDf.columns[-1]
    q = i2rDf[i2rDf.columns[-1]].mean()

  except:
    q = None

  df.loc[i,'F_drag'] = fDrag
  df.loc[i,'F_lift'] = fLift

  df.loc[i,'dT_ibeamSurf/dt'] = q


df.to_csv('./export/eddyBrakeData.csv')
