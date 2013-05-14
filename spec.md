# GeoPackage Tiles Specification

## Preamble

The following GitHub document has been extracted from the OGC GeoPackage candidate standard 
current working draft, and is a revision of the earlier (January) draft released for public 
comment. This is an open document and the OGC invites collaboration and comments directed 
at the development and enhancement of this section of the GeoPackage candidate standard. 
Please see http://www.opengeospatial.org/node/1756 for more information including instructions 
on how to provide comments on the draft specification to OGC. The contributor understands that 
any contributions, if accepted by the OGC Membership, shall be incorporated into the formal 
OGC GeoPackage standards document and that all copyright and intellectual property shall be 
vested to the OGC.


### 6.3.5	Tile Tables

The Tile table model and conventions described below support direct use of tiles in a GeoPackage in two ways. First, they specify how 
existing applications may create SQL Views of the data /metadata model on top of existing 
application tables that follow different interface conventions. Second, they include 
and expose enough metadata information at both the dataset and record levels to allow 
applications that use GeoPackage data to discover its characteristics without having to parse 
all of the stored images. Applications that store GeoPackage tile data, which are 
presumed to have this information available, SHALL store sufficient metadata to enable its 
intended use. 

The GeoPackge Tile data model may be implemented directly as SQL tables in a SQLite database for 
maximum performance, or as SQL views on top of tables in an existing SQLite Tile store
for maximum adaptability and loose coupling to enable widespread implementation. 

#### 6.3.5.1 Tiles Table Metadata

> **Requirement 13**   /gpkg/1.0/req/core/ tile_table_metadata_table:

> A GeoPackage SHALL contain a tile_table_metadata table as defined in tables 11 and xx and 
> specified in clause 6.3.5.1.


The `tile_table_metadata` table or view SHALL contain one row record describing each tile table in a 
GeoPackage.  The `t_table_name` column value SHALL be a row value of `r_table_name` in the `raster_columns` 
table, enforced by a trigger.  The `is_times_two_zoom` column value SHALL be 1 if zoom level pixel sizes 
vary by powers of 2 between adjacent zoom levels in the corresponding tile table, or 0 if not.

[[Note 4]] (#note-4) and [[Note 5]] (#note-5)

**Table 11** - `tile_table_metadata`
Table or View Name: `tile_table_metadata`

| Column Name | Column Type	| Column Description | Null	| Default	Key |
|-------------|-------------|--------------------|------|-------------|
| t_table_name | text	| {RasterLayerName}{_tiles}	| no | PK |
| is_times_two_zoom	| integer	| Zoom level pixel sizes vary by powers of 2 (0=false,1=true)	| no | 1 |

See Annex B: [Table Definition SQL clause B.9] (#clause-B9) - `tile_table_metadata`

### 6.3.5.2	Tile Matrix Metadata

> Requirement 14   /gpkg/1.0/req/core/ tile_matrix_metadata_table:

> A GeoPackage SHALL contain a tile_matrix_metadata table as defined in tables 12 and xx and specified in clause 6.3.5.2.

  
The `tile_matrix_metadata` table or view SHALL contain one row record for each zoom level that 
contains one or more tiles in each tiles table.  It may contain row records for zoom levels in 
a tiles table that do not contain tiles. 

[[Note 3]] (#note-3)

The `tile_matrix_metadata` table documents the structure of the tile matrix at each zoom level 
in each tiles table. It allows GeoPackages to contain rectangular as well as square tiles (e.g. 
for better representation of polar regions). It allows tile pyramids with zoom levels that differ 
in resolution by powers of 2, irregular intervals, or regular intervals other than powers of 2. 
When the value of the `is_times_two_zoom` column in the `tile_table_metadata` record for a tiles 
table is 1 (true) then the pixel sizes for adjacent zoom levels in the `tile_matrix_metadata` table 
for that table SHALL only vary by powers of 2.

[[Note 6]] (#note-6)  

GeoPackages SHALL follow the most frequently used conventions of a tile origin at the upper left and
a zoom-out-level of 0 for the smallest map scale “whole world” zoom level view, as specified by 
[WMTS] (http://portal.opengeospatial.org/files/?artifact_id=35326). The tile coordinate (0,0) 
SHALL always refer to the tile in the upper left corner of the tile matrix at any zoom level, 
regardless of the actual availability of that tile.  Pixel sizes for zoom levels sorted in ascending 
order SHALL be sorted in descending order.  

GeoPackages SHALL not require that tiles be provided for level 0 or any other particular zoom level. 
This means that a tile matrix set can be sparse, i.e. not contain a tile for any particular position 
at a certain tile zoom level. This does not affect the spatial extent stated by the min/max x/y columns 
values in the `geopackage_contents` record for the same `t_table_name`, or the tile matrix width and 
height at that level.

[[Note 7]] (#note-7), [[Note 8]] (#note-8), [[Note 9]] (#note-9), and [[Note 10]] (#note-10) 

**Table 12** - `tile_matrix_metadata`
+ Table or View Name: `tile_matrix_metadata`

|Column Name | Column Type | Column Description |	Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
| `t_table_name` |	text |	{RasterLayerName}_tiles |no	| | PK, FK |
| `zoom_level`	| integer |	0 <= `zoom_level` <= max_level for `t_table_name`	| no |	0 |	PK |
| `matrix_width` |	integer |	Number of columns (>= 1) in tile matrix at this zoom level | no |	1 | |	
| `matrix_height` |	integer |	Number of rows (>= 1) in tile matrix at this zoom level |	no | 1 | |	
| `tile_width` |	integer |	Tile width in pixels (>= 1)for this zoom level |	no |	256	| |
| `tile_height` |	integer |	Tile height in pixels (>= 1) for this zoom level |	no |	256	| |
| `pixel_x_size` |	double |	In `t_table_name` srid units or default meters for srid 0 (>0) |	no |	1 | |
| `pixel_y_size` |	double |	In `t_table_name` srid units or default meters for srid 0 (>0) |	no |	1	| |

See Annex B: [Table Definition SQL clause B.10] (#clause-B10) - `tile_matrix_metadata`



### 6.3.6.3	Tiles Matrix Data Tables

> **Requirement 20**   /gpkg/1.0/req/core/tiles_table

> All tile matrix sets in a GeoPackage SHALL be contained in tiles tables as defined in clause 6.3.6.3 and table 15
and exemplified by table xx.


Tiles in a tile matrix set with one or more zoom levels SHALL be stored in a GeoPackage in a tiles 
table or view with a unique name for every different tile matrix set in the GeoPackage.  Each tiles 
table or view SHALL be defined with the columns described in table 15 below.  Each tiles table or 
view SHALL contain tile matrices at one or more zoom levels of different spatial resolution (map scale).
All tiles at a particular zoom level SHALL have the same `pixel_x_size` and `pixel_y_size` values 
specified in the `tile_matrix_metadata` row record for that tiles table and zoom level.  

When the value of the `is_times_two_zoom` column in the `tile_table_metadata` record for a tiles 
table row is 1 (true) then the pixel sizes for adjacent zoom levels in the tiles table SHALL only 
vary by powers of 2.

> **Requirement 20**   /gpkg/1.0/req/core/tiles_table

> All tile matrix sets in a GeoPackage SHALL be contained in tiles tables as defined in clause 6.3.6.3 
and table 15 and exemplified by table xx.


[[Note 11]] (#note-11) and [[Note 12]] (#note-12)

GeoPackages SHALL implement appropriate SQL triggers on each tiles table by executing the 
`add_tile_triggers()` routine specified in clause 10.8 below with the tiles table as a parameter 
value to ensure that 

1.	The `zoom_level` value is specified for the tiles table in the `tile_matrix_metadata` table

2.	The tile column value is between 0 and the `matrix_height` specified for the zoom_level in the `tile_matrix_metadata` table

3.	The `tile_row value is between 0 and the `matrix_width` specified for the `zoom_level` in the `tile_matrix_metadata` table

**Table 15** – tiles table
+ Table or View Name:   {TilesTableName} tiles table

|Column Name | Column Type | Column Description |  Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
| `id` |	integer	| Autoincrement primary key |	no |	|	PK |
| `zoom_level` |	integer |	min(zoom_level) <= `zoom_level` <= max(zoom_level)  for t_table_name |	no |	0	 | UK |
| `tile_column` |	integer	| 0 to `tile_matrix_metadata` `matrix_width` – 1 |	no |	0	| UK |
| `tile_row` |	integer	| 0 to `tile_matrix_metadata` `matrix_height` - 1 |	no	| 0 |	UK |
| `tile_data` |	BLOB	| Of an image MIME type specified in clause 10.2 | no	| | |	

See Annex B: [Table Definition SQL clause B.13] (#clause-B13) - `sample_matrix_tiles`


###Annex B


##### Clause B.9

**Table 2** - `tile_table_metadata` Table Definition SQL

```SQL
CREATE TABLE
  tile_table_metadata
  (
    t_table_name TEXT NOT NULL PRIMARY KEY,
    is_times_two_zoom INTEGER NOT NULL DEFAULT 1
  )
```
###### Clause B.10

**Table 3** - `tile_matrix_metadata` Table Creation SQL

```SQL
CREATE TABLE
  tile_matrix_metadata
  (
    t_table_name TEXT NOT NULL,
    zoom_level INTEGER NOT NULL,
    matrix_width INTEGER NOT NULL,
    matrix_height INTEGER NOT NULL,
    tile_width INTEGER NOT NULL,
    tile_height INTEGER NOT NULL,
    pixel_x_size DOUBLE NOT NULL,
    pixel_y_size DOUBLE NOT NULL,
    CONSTRAINT pk_ttm PRIMARY KEY (t_table_name, zoom_level) ON CONFLICT ROLLBACK,
    CONSTRAINT fk_ttm_t_table_name FOREIGN KEY (t_table_name) REFERENCES tile_table_metadata(t_table_name
  )
```

##### Clause B.13

**Table 4** - EXAMPLE: `sample_matrix_tiles` Table Definition SQL

```SQL
CREATE TABLE
  sample_matrix_tiles
  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zoom_level INTEGER NOT NULL DEFAULT 0,
    tile_column INTEGER NOT NULL DEFAULT 0,
    tile_row INTEGER NOT NULL DEFAULT 0,
    tile_data BLOB NOT NULL DEFAULT (zeroblob(4)),
    UNIQUE (zoom_level, tile_column, tile_row)
  )
```

####Implementation Notes

######[Note 3]

A `tile_matrix_metadata` row record must be inserted for a zoom level for `t_table_name` before 
any tiles are inserted into the corresponding tiles table if there are triggers on that table as 
specified in clause 7.3.5.x below that reference `tile_matrix_metadata`  column values for that zoom 
level to reject invalid data 

######[Note 4]

A row record for a tile table must be inserted into this table before row records can be inserted 
into the tile_matrix_metadata table described in clause 10.4 due to the presence of foreign key and other 
integrity constraints on that table.

######[Note 5]

GeoPackage applications that insert, update, or delete tiles (matrix set) table tiles row records 
are responsible for maintaining the corresponding descriptive contents of the tile_table_metadata table.

######[Note 6]

Most tile pyramids have an origin at the upper left, a convention adopted by the 
OGC [Web Map Tile Service (WMTS)] (http://portal.opengeospatial.org/files/?artifact_id=35326), 
but some such as [TMS] (http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification) used by 
[MB-Tiles] (https://github.com/mapbox/mbtiles-spec) have an origin at the lower left. Most tile 
pyramids, such as [Open Street Map] (http://wiki.openstreetmap.org/wiki/Main_Page), 
[OSMDroidAtlas] (http://wiki.openstreetmap.org/wiki/Main_Page), and [FalconView] (http://www.falconview.org/trac/FalconView) 
use a zoom_out_level of 0 for the smallest map scale “whole world” zoom level view, another 
convention adopted by WMTS, but some such as [Big Planet Tracks] (http://code.google.com/p/big-planet-tracks/) 
invert this convention and use 0 or 1 for the largest map scale “local detail” zoom level view.

######[Note 7]

GeoPackage applications may query the `tile_matrix_metadata` table or the tiles (matrix set) 
table specified in clause 10.7 below to determine the minimum and maximum zoom levels for a given tile matrix table.  

######[Note 8]

GeoPackage applications may query the tiles (matrix set) table to determine which tiles are available at each zoom level.

######[Note 9]

GeoPackage applications that insert, update, or delete tiles (matrix set) table tiles row 
records are responsible for maintaining the corresponding descriptive contents of the `tile_matrix_metadata` table.

######[Note 10]

The `geopackage_contents` table (see clause 8.2 above) contains coordinates that define a
bounding box as the stated spatial extent for all tiles in a tile (matrix set) table. If the geographic 
extent of the image data contained in these tiles is within but not equal to this bounding box, then the
non-image area of matrix edge tiles must be padded with no-data values, preferably transparent ones.

######[Note 11]

The id primary key allows tiles table views to be created on [RasterLite] (https://www.gaia-gis.it/fossil/librasterlite/index) 
version 1 raster table implementations, where the tiles are selected based on a spatially indexed 
bounding box in a separate metadata table.

######[Note 12]

The zoom_level / tile_column / tile_row unique key allows tiles to be selected and accessed 
by “z, x, y”, a common convention used by [MBTiles] (https://github.com/mapbox/mbtiles-spec), 
[Big Planet Tracks] (http://code.google.com/p/big-planet-tracks/), and other implementations. 
In a SQLite implementation this unique key is automatically indexed. This table / view definition 
may also follow [RasterLite] (https://www.gaia-gis.it/fossil/librasterlite/index) version 1 conventions, 
where the tiles are selected based on a spatially indexed bounding box in a separate metadata table.

######[Note 13]

An integer column primary key is recommended for best performance.

######[Note 14]

The `sample_rasters` table created in SQL 5 above could be extended with one or more 
geometry columns by calls to the `addGeometryColumn()` routine specified in clause 9.4 to have 
both raster and geometry columns like the `sample_feature_table` shown in Figure3: GeoPackageTables above in clause 7.

######[Note 15]

This table naming convention is adopted from [RasterLite] (https://www.gaia-gis.it/fossil/librasterlite/index).

######[Note 16]

In an SQLite implementation, the rowid value is always equal to the value of a single-column 
primary key on an [integer column] (http://www.sqlite.org/lang_createtable.html#rowid).  Althought not 
stated in the SQLite documentation, testing has not revealed a case where rowed values on a table with 
any primry key column(s) defined are changed by a database reorganization performed by the VACUUM SQL command.

######[Note 17]

This data structure can be implemented as a table in the absence of geometry data types or spatial 
indexes. When implemented as a view, the min/max x/y columns could reference ordinates of a bounding box geometry 
in an underlying table when geometry data types are available, e.g. in [RasterLite] (https://www.gaia-gis.it/fossil/librasterlite/index).


####Footnotes

######[14]  OGC 06-104r4 OpenGIS® Implementation Standard for Geographic information - Simple feature 
access - Part 2: SQL option   Version: 1.2.1 2010-08-04 http://portal.opengeospatial.org/files/?artifact_id=25354 	
(also ISO/TC211 19125 Part 2)

######[15]  OGC 99-049 OpenGIS® Simple Features Specification for SQL Revision 1.1 	May 5, 1999, Clause 2.3.8  
http://portal.opengeospatial.org/files/?artifact_id=829 


######[31]  
NGA Standardization Document: Implementation Profile for Tagged Image File Format (TIFF) and Geographic Tagged Image File Format (GeoTIFF), Version 2.0,  2001-10-26  https://nsgreg.nga.mil/doc/view?i=2224  
######[32]  
IETF RFC 3986 Uniform Resource Identifier (URI): Generic Syntax http://www.ietf.org/rfc/rfc3986.txt 
######[33]  
OGC08-131r3 The Specification Model — A Standard for Modular specifications  https://portal.opengeospatial.org/files/?artifact_id=34762 

