# GeoPackage Tiles Specification Requirements

### Introduction

This document is a complementary document to the main [GeoPackage Tiles Spec] (spec.md). 
It contains all the requirements of the specification, in a single document, instead of
mixed through out the main specification. The conformance classes could also go here.

### Requirements

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_columns_table |
|REQ 38 | A GeoPackage SHALL include a `raster_columns` table or updateable view that includes the columns and foreign key constraint defined in Table 22 and clause 10.2, and containing data described in clause 10.2.|

| **Requirement: Extension** | |  
|-----------------------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_columns_table/triggers |
|REQ 39 | A GeoPackage SHALL include SQL triggers on the `raster_columns` table or updateable view as defined in Table 23 and clause 10.2.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/core  |
| REQ 40 | A GeoPackage SHALL support storage and use of MIME types image/jpeg [[24]] (#24) [[25]] (#25) [[26]] (#26) and image/png [[27]] (#27) [[28]] (#28) as defined in clause 10.2. |

| **Requirement: Extension** | |  
|-------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/extension/webp |
| REQ 41 | A GeoPackage SHALL support storage and use of MIME type image/x-webp [[29]] (#29) as defined in clause 10.2 |

| **Requirement: Extension** | |  
|-------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/extension/ geotiff |
| REQ 42 | A GeoPackage SHALL support storage and use of MIME type image/tiff [[30]] (#30) for GeoTIFF images [[32]] (#31) [[33]] (#33) as defined in clause 10.2 |

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/table |
| REQ 43 | A GeoPackage SHALL include a tile_table_metadata table as defined in clause 10.3 and table 26.|

| **Requirement: Extension** | |  
|-----------------------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/triggers |
|REQ 44 | A GeoPackage SHALL have tile_table_metadata table triggers as defined in clause 10.3 and table 27.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/data |
|REQ 45 | A GeoPackage tile_table_metadata table SHALL contain a row record for each tile table in the GPKG as specified in clause 10.3.|


| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/table |
|REQ 46 | A GeoPackage SHALL include a tile_matrix_metadata table as defined in clause 10.4 and table 30.|

| **Requirement: Extension** | |  
|-----------------------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/triggers|
|REQ 47| A GeoPackage SHALL have triggers on the tile_matrix_metadata table as defined in clause 10.4 and table 31.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/data|
|REQ 48| A GeoPackage tile_matrix_metadata table SHALL contain one row record for each zoom level that contains one or more tiles in each tiles table.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_zoom_levels/powers_of_two|
REQ 49|A GeoPackage SHALL support tile matrix set zoom levels for pixel sizes that differ by powers of two between adjacent zoom levels.|

| **Requirement: Extension** | |  
|-----------------------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_zoom_levels/other_intervals|
|REQ 50|A GeoPackage SHALL support tile matrix set zoom levels for pixel sizes that differ by irregular intervals or by regular intervals other than powers of two between adjacent zoom levels.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/table |
|REQ 51 | All tile matrix sets in a GeoPackage SHALL be contained in tiles tables defined as specified in clause 10.5 and table 33and exemplified by table 34|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/raster_column|
|REQ 52| All tile table tile_data raster columns in a GeoPackage SHALL be defined with a BLOB data type that is an image mime type as specified in clause 10.2.|

| **Requirement: Extension** | |  
|-----------------------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/triggers|
|REQ 53|All tile matrix set tables in a GeoPackage SHALL have triggers defined by executing the add_tile_triggers() routine specified in clause 10.8 as exemplified by table 35.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/table|
|REQ 64|All raster images in a GeoPackage that are not tiles in a tiles table shall be contained in rasters tables that are defined as specified by clause 10.6 and exemplified by tables 39 and 40.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/primary_key|
|REQ 65|Every raster table in a GeoPackage shall have a primary key defined on one or more columns as specified by clause 10.6|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/raster_column|
|REQ 66|All raster table raster columns in a GeoPackage shall be defined with a BLOB data type that is an image mime type as specified in clause 10.2.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/rt_metadata_table|
|REQ 67|	There SHALL be a {Raster|Tile TableName}{_rt_metadata} table as specified in clause 10.7 with the columns described in table 40 and exemplified by table 41 for every tile and raster table in a GeoPackage.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/rt_metadata_table/data|
|REQ 68|Each {Raster|Tile TableName}{_rt_metadata} table specified in clause 10.7 for every tile and raster table in a GeoPackage SHALL have a row record describing each raster and tile in a GeoPackage.|

| **Requirement: Extension** | |  
|-----------------------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/rt_metadata_table/triggers|
|REQ 69 | All raster table raster columns in a GeoPackage SHALL have triggers defined by executing the add_rt_metadata_triggers() routine specified in clause 10.8, as exemplified by table 42.|


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


