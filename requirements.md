# GeoPackage Tiles Specification Requirements

### Introduction

This document is a complementary document to the main [GeoPackage Tiles Spec] (spec.md). 
It contains all the requirements of the specification, in a single document, instead of
mixed through out the main specification. The conformance classes could also go here.

### Requirements

| Requirement Number | Type | Requirement |
|--------------------|------|-------------|
| REQ 38 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_columns_table <br/><br/> A GeoPackage SHALL include a `raster_columns` table or updateable view that includes the columns and foreign key constraint defined in Table 22 and clause 10.2, and containing data described in clause 10.2.|
| REQ 39 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_columns_table/triggers  <br/><br/> A GeoPackage SHALL include SQL triggers on the `raster_columns` table or updateable view as defined in Table 23 and clause 10.2.|
| REQ 40 | **Core**|  http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/core <br/><br/> A GeoPackage SHALL support storage and use of MIME types image/jpeg [[24]] (#24) [[25]] (#25) [[26]] (#26) and image/png [[27]] (#27) [[28]] (#28) as defined in clause 10.2. |
| REQ 41 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/extension/webp  <br/><br/> A GeoPackage SHALL support storage and use of MIME type image/x-webp [[29]] (#29) as defined in clause 10.2 |
| REQ 42 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/extension/geotiff <br/><br/> A GeoPackage SHALL support storage and use of MIME type image/tiff [[30]] (#30) for GeoTIFF images [[32]] (#31) [[33]] (#33) as defined in clause 10.2 |
| REQ 43 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/table <br/><br/> A GeoPackage SHALL include a tile_table_metadata table as defined in clause 10.3 and table 26.|
| REQ 44 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/triggers <br/><br/> A GeoPackage SHALL have tile_table_metadata table triggers as defined in clause 10.3 and table 27.|
| REQ 45 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/data <br/><br/> A GeoPackage tile_table_metadata table SHALL contain a row record for each tile table in the GPKG as specified in clause 10.3.|
| REQ 46 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/table <br/><br/> A GeoPackage SHALL include a tile_matrix_metadata table as defined in clause 10.4 and table 30.|
| REQ 47 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/triggers <br/><br/> A GeoPackage SHALL have triggers on the tile_matrix_metadata table as defined in clause 10.4 and table 31.|
| REQ 48 | **Core**| http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/data <br/><br/> A GeoPackage tile_matrix_metadata table SHALL contain one row record for each zoom level that contains one or more tiles in each tiles table.|
| REQ 49 | **Core**| http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_zoom_levels/powers_of_two <br/><br/> A GeoPackage SHALL support tile matrix set zoom levels for pixel sizes that differ by powers of two between adjacent zoom levels.|
| REQ 50 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_zoom_levels/other_intervals<br/><br/> A GeoPackage SHALL support tile matrix set zoom levels for pixel sizes that differ by irregular intervals or by regular intervals other than powers of two between adjacent zoom levels.|
| REQ 51 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/table  <br/><br/> All tile matrix sets in a GeoPackage SHALL be contained in tiles tables defined as specified in clause 10.5 and table 33and exemplified by table 34|
| REQ 52 | **Core**| http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/raster_column <br/><br/> All tile table tile_data raster columns in a GeoPackage SHALL be defined with a BLOB data type that is an image mime type as specified in clause 10.2.|
| REQ 53 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/triggers<br/><br/> All tile matrix set tables in a GeoPackage SHALL have triggers defined by executing the add_tile_triggers() routine specified in clause 10.8 as exemplified by table 35.|
| REQ 54 | **Core**| http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/table<br/><br/> All raster images in a GeoPackage that are not tiles in a tiles table shall be contained in rasters tables that are defined as specified by clause 10.6 and exemplified by tables 39 and 40.|
| REQ 55 | **Core**| http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/primary_key<br/><br/> Every raster table in a GeoPackage shall have a primary key defined on one or more columns as specified by clause 10.6|
| REQ 56 | **Core**|  http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/raster_column<br/><br/> All raster table raster columns in a GeoPackage shall be defined with a BLOB data type that is an image mime type as specified in clause 10.2.|
| REQ 57 | **Core**|	http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/rt_metadata_table <br/><br/> There SHALL be a {Raster|Tile TableName}{_rt_metadata} table as specified in clause 10.7 with the columns described in table 40 and exemplified by table 41 for every tile and raster table in a GeoPackage.|
| REQ 58 | **Core**|http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/rt_metadata_table/data <br/><br/> Each {Raster|Tile TableName}{_rt_metadata} table specified in clause 10.7 for every tile and raster table in a GeoPackage SHALL have a row record describing each raster and tile in a GeoPackage.|
| REQ 59 | **Extension** | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/rt_metadata_table/triggers <br/><br/> All raster table raster columns in a GeoPackage SHALL have triggers defined by executing the add_rt_metadata_triggers() routine specified in clause 10.8, as exemplified by table 42.|


####Notes

######[24]
JPEG File Interchange Format Version 1.02, September 1, 1992   http://www.jpeg.org/public/jfif.pdf 
######[25]
IETF RFC 2046 Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types http://www.ietf.org/rfc/rfc2046.txt 
######[26]  
Portable Network Graphics http://libpng.org/pub/png/
######[27]
MIME Media Types http://www.iana.org/assignments/media-types/index.html 
######[28]
WebP  https://developers.google.com/speed/webp/
######[29]  
TIFF – Tagged Image File Format, Revision 6.0, Adobe Systems Inc., June 1992   	http://partners.adobe.com/public/developer/en/tiff/TIFF6.pdf 
######[30]  
GeoTIFF Format Specification, Revision 1.0, 10 November 1995; version 1.8.2  http://www.remotesensing.org/geotiff/spec/geotiffhome.html 
######[31]  
NGA Standardization Document: Implementation Profile for Tagged Image File Format (TIFF) and Geographic Tagged Image File Format (GeoTIFF), Version 2.0,  2001-10-26  https://nsgreg.nga.mil/doc/view?i=2224  
######[32]  
IETF RFC 3986 Uniform Resource Identifier (URI): Generic Syntax http://www.ietf.org/rfc/rfc3986.txt 
######[33]  
OGC08-131r3 The Specification Model — A Standard for Modular specifications  https://portal.opengeospatial.org/files/?artifact_id=34762 


