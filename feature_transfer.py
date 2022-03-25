# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:34:19 2022

@author: MPatton
"""

import arcpy
import pandas as pd
import numpy

#arcpy.management.CreateDatabaseConnection("C:\test", "test.sde", "ORACLE", "sde:oracle$sde:oracle11g:water49db", "DATABASE_AUTH", "gisuser", "gisuser49")

arcpy.env.workspace = r"C:\Users\MPatton\AppData\Roaming\ESRI\Desktop10.6\ArcCatalog\Connection to water49db.sde"
#arcpy.env.workspace = r"C:\test\test2.sde"

features = arcpy.ListFeatureClasses(feature_type='point')


for fc in features:
	print(fc)


stations = r"C:\Station_Association\model_run.gdb\IR_Stations_0325"
arcpy.management.CopyFeatures("CALWQA.IR_Stations", stations)

StationCode = STATIONCODE, StationName = STATIONNAME, WBID, Waterbody = WBNAME,SPATIALLY_DEPENDENT,FreshMarine = FRESHMARINE,Regional_Board = IR_REGIONALBOARD, STATUS, Comments = STATION_COMMENT)


table = arcpy.da.TableToNumPyArray(stations, ('STATIONCODE', 'STATIONNAME', 'WBID', 'WBNAME', 'SPATIALLY_DEPENDENT', 'FRESHMARINE', 'IR_REGIONALBOARD', 'STATUS', 'STATION_COMMENT'))

table = pd.DataFrame(table)

table = table.rename(columns={'STATIONCODE' : 'StationCode', 'STATIONNAME' : 'StationName', 'FRESHMARINE' : 'FreshMarine', 'IR_REGIONALBOARD' : 'Regional_Board','STATION_COMMENT' : 'Comments'})

table.columns

table.head()

regions = ['2', '4', '5SR', '8']

for rb in regions:
	print(rb)
	region = table[table['Regional_Board'] == rb]
	region.to_csv(index=False)




