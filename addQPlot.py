import sys
sys.path.append(r'C:\Users\adam\Documents\eddyBrake')

import Autobot

import ScriptEnv
ScriptEnv.Initialize("AnsoftMaxwell.MaxwellScriptInterface")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("eddyBrake002")

import os

exportFiles = os.listdir(r'C:\Users\adam\Documents\eddyBrake\Analysis2\export')

for oDesign in oProject.GetDesigns():

  if '{}_q.csv'.format(oDesign.GetName()) in exportFiles:
    print('{}_q.csv'.format(oDesign.GetName())+' ... Done')
    continue

  print('{}_q.csv'.format(oDesign.GetName())+' ... Postprocessing')

  oDesktop.RestoreWindow()
  model = Autobot.EddyBrakeModel(oDesktop,oProject.GetName(),oDesign.GetName())
  stopTime = 4*0.10795/model.v
  oEditor = oDesign.SetActiveEditor("3D Modeler")
  oEditor.CreatePolyline(
    [
      "NAME:PolylineParameters",
      "IsPolylineCovered:="  , True,
      "IsPolylineClosed:="  , False,
      [
        "NAME:PolylinePoints",
        [
          "NAME:PLPoint",
          "X:="      , "0mm",
          "Y:="      , "3.9751mm",
          "Z:="      , "0mm"
        ],
        [
          "NAME:PLPoint",
          "X:="      , "107.95mm",
          "Y:="      , "3.9751mm",
          "Z:="      , "0mm"
        ]
      ],
      [
        "NAME:PolylineSegments",
        [
          "NAME:PLSegment",
          "SegmentType:="    , "Line",
          "StartIndex:="    , 0,
          "NoOfPoints:="    , 2
        ]
      ],
      [
        "NAME:PolylineXSection",
        "XSectionType:="  , "None",
        "XSectionOrient:="  , "Auto",
        "XSectionWidth:="  , "0mm",
        "XSectionTopWidth:="  , "0mm",
        "XSectionHeight:="  , "0mm",
        "XSectionNumSegments:="  , "0",
        "XSectionBendType:="  , "Corner"
      ]
    ], 
    [
      "NAME:Attributes",
      "Name:="    , "SurfaceLine",
      "Flags:="    , "NonModel#",
      "Color:="    , "(132 132 193)",
      "Transparency:="  , 0,
      "PartCoordinateSystem:=", "Global",
      "UDMId:="    , "",
      "MaterialValue:="  , "\"vacuum\"",
      "SolveInside:="    , True
    ])
  oModule = oDesign.GetModule("ReportSetup")
  oModule.CreateReport("QPlot", "Fields", "Rectangular Plot", "Setup1 : Transient", 
    [
      "Context:="    , "SurfaceLine",
      "PointCount:="    , 1001,
      "Domain:="    , "Sweep"
    ], 
    [
      "Distance:="    , ["All"],
      "Time:="    , ["All"],
      "v:="      , ["Nominal"],
      "h:="      , ["Nominal"]
    ], 
    [
      "X Component:="    , "Distance",
      "Y Component:="    , ["Ohmic_Loss"]
    ], [])
  oModule.ExportToFile("QPlot", "C:/Users/adam/Documents/eddyBrake/Analysis2/export/{}_q.csv".format(oDesign.GetName()))
  oDesktop.CloseAllWindows()

# "Time:="    , ["{}ns".format(int(stopTime*1e9))],
