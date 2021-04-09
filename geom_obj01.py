import os
import sys
from time import perf_counter

def main():
    if len(sys.argv) != 3:
        print('Usage geom_obj01.py <input text file path> <output shapefile>')
        sys.exit(0)

import arcpy

t1_start = perf_counter()

sf = sys.argv[2]
path = os.path.dirname(sf)
fc = os.path.basename(sf)

arcpy.env.workspace = path
arcpy.env.overwriteOutput = True

arcpy.CreateFeatureclass_management(path, fc, 'Polyline', spatial_reference = 4269)
with open(sys.argv[1], mode = 'r') as in_file, \
     arcpy.da.InsertCursor(sf, ["SHAPE@"]) as cursor:
    #for line in textfile
    #if line.split > 1:
    #add point object to line list
    #else
    #start new line list
    
    point_list = []
    next(in_file)
    for row in in_file:
  
        

        row = row.strip('\n')

        if len(row.split(' ')) > 1:
            longitude, latitude = [float(n) for n in row.split(' ')]
            point_list.append(arcpy.Point(longitude, latitude))
        
        else:
            
            array = arcpy.Array(point_list)
            spatial_reference = arcpy.SpatialReference(4269)
            polyline = arcpy.Polyline(array, spatial_reference)

            cursor.insertRow([polyline])
            point_list = []
        
    array = arcpy.Array(point_list)
    spatial_reference = arcpy.SpatialReference(4269)
    polyline = arcpy.Polyline(array, spatial_reference)

    cursor.insertRow([polyline])
    point_list = []

t2_stop = perf_counter()
print('\n')
print('Elapsed time: ' + str(t2_stop - t1_start ))
print('\n')
    
                    
            

if __name__ == '__main__':
    main()

#python geom_obj01.py E:\Documents\acgis\data\Canada\CanadaTest.txt E:\Documents\acgis\data\Canada\Test.shp