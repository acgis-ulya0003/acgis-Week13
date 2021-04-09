import os
import sys

def main():
    if len(sys.argv) != 3:
        print('Usage geom_obj01.py <input text file path> <output shapefile>')
        sys.exit(0)

import arcpy

sf = sys.argv[2]
path = os.path.dirname(sf)
fc = os.path.basename(sf)

arcpy.env.workspace = path
arcpy.env.overwriteOutput = True

arcpy.CreateFeatureclass_management(path, fc, 'Polyline', spatial_reference = 4269)

with open(sys.argv[1], mode = 'r') as in_file, \
     arcpy.da.InsertCursor(sf, ["SHAPE@"]) as cursor:

if __name__ == '__main__':
    main()