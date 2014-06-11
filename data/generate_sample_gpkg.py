# -*- coding: utf-8 -*-
###############################################################################
#
# Purpose:  Generate GPKG sample file
# Author:   Even Rouault <even dot rouault at mines dash paris dot org>
# 
###############################################################################
# Copyright (c) 2014, Even Rouault <even dot rouault at mines-paris dot org>
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################

import sys
from osgeo import gdal
from osgeo import ogr
from osgeo import osr

if int(gdal.VersionInfo('VERSION_NUM')) < 2000000:
    print('Requires GDAL >= 2.0(dev)')
    sys.exit(1)

sr4326 = osr.SpatialReference()
sr4326.SetFromUserInput('WGS84')

sr32631 = osr.SpatialReference()
sr32631.ImportFromEPSG(32631)

ds = ogr.GetDriverByName('GPKG').CreateDataSource('gdal_sample.gpkg')

lyr = ds.CreateLayer('point2d', geom_type = ogr.wkbPoint)
lyr.CreateField(ogr.FieldDefn('intfield', ogr.OFTInteger))
lyr.CreateField(ogr.FieldDefn('strfield', ogr.OFTString))
lyr.CreateField(ogr.FieldDefn('realfield', ogr.OFTReal))
lyr.CreateField(ogr.FieldDefn('datetimefield', ogr.OFTDateTime))
lyr.CreateField(ogr.FieldDefn('datefield', ogr.OFTDate))
lyr.CreateField(ogr.FieldDefn('binaryfield', ogr.OFTBinary))
feat = ogr.Feature(lyr.GetLayerDefn())
feat['intfield'] = 1
feat['strfield'] = 'foo'
feat['realfield'] = 1.23456
feat['datetimefield'] = '2014/06/07 14:20:00'
feat['datefield'] = '2014/06/07'
feat.SetFieldBinaryFromHexString('binaryfield', '007FFF')
feat.SetGeometry(ogr.CreateGeometryFromWkt('POINT(1 2)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('linestring2d', geom_type = ogr.wkbLineString, srs = sr4326)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('LINESTRING(1 2,3 4)'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('polygon2d', geom_type = ogr.wkbPolygon, srs = sr32631)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('POLYGON((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('multipoint2d', geom_type = ogr.wkbMultiPoint, options = ['SPATIAL_INDEX=NO'])
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOINT(0 1,2 3)'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('multilinestring2d', geom_type = ogr.wkbMultiLineString)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTILINESTRING((0 1,2 3),(4 5,6 7))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('multipolygon2d', geom_type = ogr.wkbMultiPolygon)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOLYGON(((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1)),((-9 0,-9 10,-1 10,-1 0,-9 0)))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('geomcollection2d', geom_type = ogr.wkbGeometryCollection)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('GEOMETRYCOLLECTION(POINT(0 1),LINESTRING(2 3,4 5),POLYGON((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1)),MULTIPOINT(0 1,2 3),MULTILINESTRING((0 1,2 3),(4 5,6 7)),MULTIPOLYGON(((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1)),((-9 0,-9 10,-1 10,-1 0,-9 0))))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOINT(0 1,2 3)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTILINESTRING((0 1,2 3),(4 5,6 7))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOLYGON(((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1)),((-9 0,-9 10,-1 10,-1 0,-9 0)))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('geometry2d', geom_type = ogr.wkbUnknown)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('POINT(1 2)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('LINESTRING(1 2,3 4)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('POLYGON((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOINT(0 1,2 3)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTILINESTRING((0 1,2 3),(4 5,6 7))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOLYGON(((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1)),((-9 0,-9 10,-1 10,-1 0,-9 0)))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('GEOMETRYCOLLECTION(POINT(0 1),LINESTRING(2 3,4 5),POLYGON((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1)),MULTIPOINT(0 1,2 3),MULTILINESTRING((0 1,2 3),(4 5,6 7)),MULTIPOLYGON(((0 0,0 10,10 10,10 0,0 0),(1 1,1 9,9 9,9 1,1 1)),((-9 0,-9 10,-1 10,-1 0,-9 0))))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)


lyr = ds.CreateLayer('point3d', geom_type = ogr.wkbPoint25D)
feat.SetGeometry(ogr.CreateGeometryFromWkt('POINT(1 2 3)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('linestring3d', geom_type = ogr.wkbLineString25D)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('LINESTRING(1 2 3,4 5 6)'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('polygon3d', geom_type = ogr.wkbPolygon25D)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('POLYGON((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('multipoint3d', geom_type = ogr.wkbMultiPoint25D)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOINT(0 1 2,3 4 5)'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('multilinestring3d', geom_type = ogr.wkbMultiLineString25D)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTILINESTRING((0 1 2,3 4 5),(6 7 8,9 10 11))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('multipolygon3d', geom_type = ogr.wkbMultiPolygon25D)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOLYGON(((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100)),((-9 0 50,-9 10 50,-1 10 50,-1 0 50,-9 0 50)))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)


lyr = ds.CreateLayer('geomcollection3d', geom_type = ogr.wkbGeometryCollection25D)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('GEOMETRYCOLLECTION(POINT(1 2 3),LINESTRING(1 2 3,4 5 6),POLYGON((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100)),MULTIPOINT(0 1 2,3 4 5),MULTILINESTRING((0 1 2,3 4 5),(6 7 8,9 10 11)),MULTIPOLYGON(((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100)),((-9 0 50,-9 10 50,-1 10 50,-1 0 50,-9 0 50))))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOINT(0 1 2,3 4 5)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTILINESTRING((0 1 2,3 4 5),(6 7 8,9 10 11))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOLYGON(((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100)),((-9 0 50,-9 10 50,-1 10 50,-1 0 50,-9 0 50)))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

lyr = ds.CreateLayer('geometry3d', geom_type = ogr.wkbUnknown | ogr.wkb25DBit)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('POINT(1 2 3)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('LINESTRING(1 2 3,4 5 6)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('POLYGON((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOINT(0 1 2,3 4 5)'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTILINESTRING((0 1 2,3 4 5),(6 7 8,9 10 11))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('MULTIPOLYGON(((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100)),((-9 0 50,-9 10 50,-1 10 50,-1 0 50,-9 0 50)))'))
lyr.CreateFeature(feat)
feat = ogr.Feature(lyr.GetLayerDefn())
feat.SetGeometry(ogr.CreateGeometryFromWkt('GEOMETRYCOLLECTION(POINT(1 2 3),LINESTRING(1 2 3,4 5 6),POLYGON((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100)),MULTIPOINT(0 1 2,3 4 5),MULTILINESTRING((0 1 2,3 4 5),(6 7 8,9 10 11)),MULTIPOLYGON(((0 0 100,0 10 100,10 10 100,10 0 100,0 0 100),(1 1 100,1 9 100,9 9 100,9 1 100,1 1 100)),((-9 0 50,-9 10 50,-1 10 50,-1 0 50,-9 0 50))))'))
lyr.CreateFeature(feat)

# Null geometry
feat = ogr.Feature(lyr.GetLayerDefn())
lyr.CreateFeature(feat)

ds = None
