import sys
sys.path.append(r'C:\Users\adam\Documents\eddyBrake')

import ScriptEnv
ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")

import Autobot
import os
import re

"""
gap_min = 0.005
gap_max = 0.020
gap_n_pts = 4

v_min = 10.0
v_max = 40.0
v_n_pts = 4

gap_delta = (gap_max-gap_min)/(gap_n_pts-1.0)
h_array = []
for i in range(gap_n_pts):
  h_array.append(gap_min+gap_delta*i)

v_array = []
v_delta = (v_max-v_min)/(v_n_pts-1.0)
for i in range(gap_n_pts):
  v_array.append(v_min+v_delta*i)
"""

h_array = [0.005,0.006,0.007,0.008,0.009,0.010,0.015,0.020,0.050,0.100]
v_array = [1,10.0,20.0,30.0,40.0,50.0,100.0]

master = Autobot.EddyBrakeModel(oDesktop,"eddyBrake002","0")

loadPoints = []
for h in h_array:
  for v in v_array:
    loadPoints.append([h,v])

doneLoadPoints = []
oProject = oDesktop.GetActiveProject()
designs = oProject.GetDesigns()
p = re.compile(r'[0-9]*\.*[0-9]*')
for design in designs:
  vStr = design.GetVariableValue('v')
  hStr = design.GetVariableValue('h')
  mv = p.match(vStr)
  v = float(mv.group(0))
  mh = p.match(hStr)
  h = float(mh.group(0))
  doneLoadPoints.append([h,v])
  

for loadPoint in loadPoints:
  h = loadPoint[0]
  v = loadPoint[1]
  
  done = False
  for doneLoadPoint in doneLoadPoints:
    vdone = doneLoadPoint[1]
    hdone = doneLoadPoint[0]
    if (v==vdone) and (h==hdone):
      print('Load case v={}, h={} ... Done'.format(v,h))
      done = True
      break

  if not done:
    print('Load case v={}, h={} ... Analyzing'.format(v,h))
    m = master.copy()
    m.setVelocity(v)
    m.setGap(h)
    m.runAnalysis()
    m.oProject.Save()
    m.exportForcePlot(os.getcwd()+"\\export\\{}.csv".format(m.oDesign.GetName()))
    oDesktop.CloseAllWindows()