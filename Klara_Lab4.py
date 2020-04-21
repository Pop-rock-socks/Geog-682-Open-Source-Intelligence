# Robert Klara
# April 20th, 2020
# Lab 4
# GEOG 682

print("Good morning Starshine, the earth says Hello!")
# get the path to the shapefiles for Crimes and Dsitricts
Crime = "S:/682/Spring20/rklara/Lab4/Crime_Incidents_in_2017/Crime_Incidents_in_2017.shp"
Districts = "S:/682/Spring20/rklara/Lab4/Police_Districts/Police_Districts.shp"

# The format is:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

CrimeDC = iface.addVectorLayer(Crime, "DC", "ogr") #loads crime into QGIS
if not CrimeDC.isValid():
    print("Layer failed to load!") #catch my errors
    
DistrictDC = iface.addVectorLayer(Districts, "DC", "ogr") #loads Police Districts into GIS
if not DistrictDC.isValid():
    print("Layer failed to load!") #catch my erros

    
processing.run("qgis:joinbylocationsummary",{'INPUT':DistrictDC,'JOIN':CrimeDC,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/rklara/Lab4/join.shp"})

join = "S:/682/Spring20/rklara/Lab4/join.shp"
join1 = iface.addVectorLayer(join, "Join", "ogr") #loads crime into QGIS
if not join1.isValid():
    print("Layer failed to load!") #catch my errors
#
#Which police district had the most crimes in 2017? 
# The 3rd Distrct had the most crimes in 2017
#
#How many crimes occurred there?
# 5970 total crimes occured here.
#
#processing.algorithmHelp("qgis:joinbylocationsummary")