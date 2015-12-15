import sys
sys.path.append(r'C:\Users\adam\Documents\eddyBrake')

import ScriptEnv
ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")

import Autobot
import os
import csv

oProject = oDesktop.GetActiveProject()
pName = oProject.GetName()

f = open(r'C:\Users\adam\Documents\eddyBrake\Analysis2\export\legend.csv','w')
writer = csv.writer(f)

writer.writerow(['name','v','h'])

models = []
for design in oProject.GetDesigns():

  model = Autobot.EddyBrakeModel(oDesktop,pName,design.GetName())
  v = model.v
  h = model.h
  name = design.GetName()
  writer.writerow([name,v,h])
  oDesktop.CloseAllWindows()
f.close()
