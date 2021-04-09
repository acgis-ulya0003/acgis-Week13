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
    
    
    point_list = []
    wk_string = 'LINESTRING ('

    next(in_file)
    for row in in_file:
  
        

        row = row.strip('\n')
        

        if len(row.split(' ')) > 1:
            
            longitude, latitude = row.split(' ')
            wk_string += longitude + ' ' + latitude + ', '
        
        else:
            wk_string = wk_string[:-2] + ')'                       
            spatial_reference = arcpy.SpatialReference(4269)
            polyline = arcpy.FromWKT(wk_string, spatial_reference)            
            cursor.insertRow([polyline])
            wk_string = 'LINESTRING ('
            
            
    wk_string = wk_string[:-2] + ')'
    spatial_reference = arcpy.SpatialReference(4269)
    polyline = arcpy.FromWKT(wk_string, spatial_reference)            
    cursor.insertRow([polyline])
    
    

t2_stop = perf_counter()
print('\n')
print('Elapsed time: ' + str(t2_stop - t1_start ))
print('\n')
    
                    
            

if __name__ == '__main__':
    main()

#python geom_obj02.py E:\Documents\acgis\data\Canada\canada.txt E:\Documents\acgis\data\Canada\Canada_lines_wkt.shp