# GeoPackage Tiles Specification

## 10  Raster Tile Store
### 10.1	Raster Tile Introduction
There are a wide variety of commercial and open source conventions for storing, indexing, accessing and describing individual rasters and tiles in tile matrix pyramids.   Unfortunately, no applicable existing consensus, national or international specifications have standardized practices in this domain.  In addition, various image file formats have different representational capabilities, and include different self-descriptive metadata.  

The Raster / Tile Store data / metadata model, conventions and SQL functions described below support direct use of rasters and tiles in a GeoPackage in two ways.  First, they specify how existing applications may create SQL Views of the data /metadata model on top of existing application tables that that follow different interface conventions.  Second, they include and expose enough metadata information at both the dataset and record levels to allow applications that use GeoPackage data to discover its characteristics without having to parse all of the stored images.  Applications that store GeoPackage raster and tile data, which are presumed to have this information available, SHALL store sufficient metadata to enable its intended use. 

Following a convention used by [MBTiles] (https://github.com/mapbox/mbtiles-spec), the Raster / Tile Store data model may be implemented directly as SQL tables in a SQLite database for maximum performance, or as SQL views on top of tables in an existing SQLite Raster / Tile store for maximum adaptability and loose coupling to enable widespread implementation. A GeoPackage can store multiple raster and tile pyramid data sets in different tables or views in the same container. Following a convention used by [RasterLite] (https://www.gaia-gis.it/fossil/librasterlite/index), tables or views containing record-level metadata are named with a raster or tile table name prefix and a “_rt_metadata” suffix, e.g. {RasterTableName}{_rt_metadata.  

The tables or views that implement the GeoPackage Raster / Tile Store data / metadata model are described and discussed individually in the following subsections.

> NOTE: Images of multiple MIME types may be stored in given table.  For example, in a tiles table, image/png format tiles without compression could be used for transparency where there is no data on the tile edges, and image/jpeg format tiles with compression could be used for storage efficiency where there is image data for all pixels.  Images of multiple bit depths of the same MIME type may also be stored in a given table, for example image/png tiles in both 8 and 24 bit depths.

### 10.2	Raster Columns
A GeoPackage SHALL contain a raster_columns table or view as defined in this clause.  The raster_columns table or view SHALL contain one row record describing each raster or tile column in any table in a GeoPackage.  The r_raster_column in r_table_name SHALL be defined as a BLOB data type.  

The compr_qual_ factor column value indicates the lowest image quality of any raster or tile in the associated column on a scale from 1 (lowest) to 100 (highest) for rasters compressed with a lossy compression algorithm.  It is always 100 if all rasters or tiles are compressed with a lossless compression algorithm, or are not compressed.  The value -1 indicates "unknown" and is specified as the default value.

The georectification column value indicates the minimum level of georectification to areas on the earth for all rasters or tiles in the associated column are georectified.  A value of -1 indicates "unknown" as is specified as the default value.  A value of 0 indicates that no rasters or tiles are georectified. A value of 1 indicates that all rasters or tiles are georectified (but not necessarily orthorectified). A value of 2 indicates that all rasters or tiles are orthorectified (which implies georectified) to accurately align with real world coordinates, have constant scale, and support direct measurement of distances, angles, and areas.

The srid SHALL have a value contained in the spatial_ref_sys table defined in clause 9.2 above.

All GeoPackages SHALL support image/png and image/jpeg formats for rasters and tiles. GeoPackages may support image/x-webp and image/tiff formats for rasters and tiles. GeoPackage support for the image/tiff format [31] is limted to GeoTIFF [32] images that meet the requirements of the NGA Implementation Profile [33] for coordinate transformation case 3 where the position and scale of thedata is known exactly, and no rotation of the image is required.

> NOTE 1:  A feature type may be defined to have 0..n raster attributes, so the corresponding feature table may contain from 0..n raster columns.

> NOTE 2:  A raster tile layer table has only one raster column named “tile_data”.

**Table 21** -- raster_columns 

 + Table or View Name:   raster_columns

| Column Name | ColumnType | Column Description | Null | Default | Key |
| ----------- | ---------- | ------------------ | ---- | ------- | --- | 
| r_table_name | text |	Name of the table containing the raster column, e.g. {FeatureTableName} OR {RasterLayerName}_tiles | no	|	| PK FK |
| r_raster_column | text | Name of a column in a table that is a raster column with a BLOB data type | no | |	PK |
| compr_qual_factor |	integer |	Compression quality factor: 1 (lowest) to 100 (highest) for lossy compression; always 100 for lossless or no compression, -1 if unknown. | no |	-1 | |
| georectification |	integer |	Is the raster georectified; 1=unknown, 0=not georectified, 1=georectified, 2=orthorectified |	no | -1 | |
| srid |	integer |	Spatial Reference System ID: spatial_ref_sys.srid |	no | | FK |

*Table 22* -- raster_columns Table Definition SQL

```SQL
CREATE TABLE raster_columns (
r_table_name TEXT NOT NULL,
r_raster_column TEXT NOT NULL,
compr_qual_factor INTEGER NOT NULL DEFAULT -1,
georectification INTEGER NOT NULL DEFAULT -1,
srid INTEGER NOT NULL DEFAULT 0,
CONSTRAINT pk_rc PRIMARY KEY (r_table_name, r_raster_column)
ON CONFLICT ROLLBACK,
CONSTRAINT fk_rc_r_srid FOREIGN KEY (srid)
REFERENCES spatial_ref_sys(srid),
CONSTRAINT fk_rc_r_gc FOREIGN KEY (r_table_name) REFERENCES geopackage_contents(table_name))
```

The raster_columns table or view in a GeoPackage SHALL have the triggers defined in Table 23 below.

**Table 23 -- raster_columns Trigger Definition SQL**

```SQL
CREATE TRIGGER 'raster_columns_r_raster_column_insert' 
BEFORE INSERT ON 'raster_columns'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK,'insert on raster_columns violates constraint: r_raster_column value must not contain a single quote')
WHERE NEW.r_raster_column LIKE ('%''%');
SELECT RAISE(ROLLBACK,'insert on raster_columns violates constraint: r_raster_column value must not contain a double quote')
WHERE NEW.r_raster_column LIKE ('%"%');
SELECT RAISE(ROLLBACK,'insert on raster_columns violates constraint: r_raster_column value must be lower case')
WHERE NEW.r_raster_column <> lower(NEW.r_raster_column);
END

CREATE TRIGGER 'raster_columns_r_raster_column_update' 
BEFORE UPDATE OF r_raster_column ON 'raster_columns'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK,'update on raster_columns violates constraint: r_raster_column value must not contain a single quote')
WHERE NEW.r_raster_column LIKE ('%''%');
SELECT RAISE(ROLLBACK,'update on raster_columns violates constraint: r_raster_column value must not contain a double quote')
WHERE NEW.r_raster_column LIKE ('%"%');
SELECT RAISE(ROLLBACK,'update on raster_columns violates constraint: r_raster_column value must be lower case')
WHERE NEW.r_raster_column <> lower(NEW.r_raster_column);
END

CREATE TRIGGER 'raster_columns_georectification_insert'
BEFORE INSERT ON 'raster_columns'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''raster_columns'' violates constraint: georectification must be -1, 0, 1 or 2')
WHERE (NOT (NEW.georectification IN (-1, 0, 1, 2)));
END 

CREATE TRIGGER 'raster_columns_georectification_update'
BEFORE UPDATE OF georectification ON 'raster_columns'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''raster_columns'' violates constraint: georectification must be -1, 0, 1 or 2')
WHERE (NOT (NEW.georectification IN (-1, 0, 1, 2)));
END

CREATE TRIGGER 'raster_columns_compr_qual_factor_insert' 
BEFORE INSERT ON 'raster_columns'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''raster_columns'' violates constraint: compr_qual_factor < 1, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor < -1;
SELECT RAISE(ROLLBACK, 'insert on table ''raster_columns'' violates constraint: compr_qual_factor = 0, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor = 0;
SELECT RAISE(ROLLBACK, 'insert on table ''raster_columns'' violates constraint: compr_qual_factor > 100, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor > 100;
END

CREATE TRIGGER 'raster_columns_compr_qual_factor_update' 
BEFORE UPDATE OF compr_qual_factor ON 'raster_columns'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''raster_columns'' violates constraint: compr_qual_factor < 1, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor < -1;
SELECT RAISE(ROLLBACK, 'update on table ''raster_columns'' violates constraint: compr_qual_factor = 0, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor = 0;
SELECT RAISE(ROLLBACK, 'update on table ''raster_columns'' violates constraint: compr_qual_factor > 100, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor > 100;
END
```

**Table 24 -  EXAMPLE: raster_columns INSERT Statement**

```SQL
INSERT INTO raster_columns VALUES (
"sample_matrix_tiles",
"tile_data",
90,
2,
4326)
```
| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_columns_table |
|REQ 38 | A GeoPackage SHALL include a raster_columns table or updateable view that includes the columns and foreign key constraint defined in Table 22 and clause 10.2, and containing data described in clause 10.2.|

| **Requirement: Extension** | |  
|-------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_columns_table/triggers |
|REQ 39 | A GeoPackage SHALL include SQL triggers on the raster_columns table or updateable view as defined in Table 23 and clause 10.2.|

| **Requirement: Core** | |
|------------------------|----|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/core  |
| REQ 40 | A GeoPackage SHALL support storage and use of MIME types image/jpeg [24][25][26]and image/png [27][28] as defined in clause 10.2. |

| **Requirement: Extension** | |  
|-------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/extension/webp |
| REQ 41 | A GeoPackage SHALL support storage and use of MIME type image/x-webp [29] as defined in clause 10.2 |

| **Requirement: Extension** | |  
|-------|------|
| | http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/mime_types/extension/ geotiff |
| REQ 42 | A GeoPackage SHALL support storage and use of MIME type image/tiff [30] for GeoTIFF images [32][33] as defined in clause 10.2 |

### 10.3	Tile Table Metadata
A GeoPackage SHALL contain a tile_table_metadata table or view as defined in this clause. The tile_table_metadata table or view SHALL contain one row record describing each tile table in a GeoPackage.  The t_table_name column value SHALL be a row value of r_table_name in the raster_columns table, enforced by a trigger.  The is_times_two_zoom column value SHALL be 1 if zoom level pixel sizes vary by powers of 2 between adjacent zoom levels in the corresponding tile table, or 0 if not.

> NOTE 1:  A row record for a tile table must be inserted into this table before row records can be inserted into the tile_matrix_metadata table described in clause 10.4 due to the presence of foreign key and other integrity constraints on that table.  

> NOTE 2:  GeoPackage applications that insert, update, or delete tiles (matrix set) table tiles row records are responsible for maintaining the corresponding descriptive contents of the tile_table_metadata table.  

Table 25 -- tile_table_metadata
Table or View Name:   tile_table_metadata

| Column Name | Column Type	| Column Description | Null	| Default	Key |
|-------------|-------------|--------------------|------|-------------|
| t_table_name | text	| {RasterLayerName}{_tiles}	| no | PK |
| is_times_two_zoom	| integer	| Zoom level pixel sizes vary by powers of 2 (0=false,1=true)	| no | 1 |

**Table 26 -- tile_table_metadata Table Definition SQL**

```SQL
CREATE TABLE tile_table_metadata (
  t_table_name TEXT NOT NULL PRIMARY KEY,
  is_times_two_zoom INTEGER NOT NULL DEFAULT 1
)
```

**Table 27 -- tile_table_metadata Trigger Definition SQL**

```SQL
CREATE TRIGGER 'tile_table_metadata_t_table_name_insert' 
BEFORE INSERT ON 'tile_table_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''tile_table_metadata'' violates constraint: t_table_name not in raster_columns.r_table_name values')
WHERE NOT (NEW.t_table_name IN 
  (SELECT DISTINCT r_table_name FROM raster_columns));
END

CREATE TRIGGER 'tile_table_metadata_t_table_name_update' 
BEFORE UPDATE OF t_table_name ON 'tile_table_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''tile_table_metadata'' violates constraint: t_table_name not in raster_columns.r_table_name values')
WHERE NOT (NEW.t_table_name IN 
  (SELECT DISTINCT r_table_name FROM raster_columns));
END

CREATE TRIGGER 'tile_table_metadata_is_times_two_zoom_insert' 
BEFORE INSERT ON 'tile_table_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on tile_table_metadata violates constraint: is_time_two_zoom must be one of 0|1')
WHERE NOT(NEW.is_times_two_zoom IN (0,1));
END
  
CREATE TRIGGER 'tile_table_metadata_is_times_two_zoom_update' 
BEFORE UPDATE OF is_times_two_zoom ON 'tile_table_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update of tile_table_metadata violates constraint: is_time_two_zoom must be one of 0|1')
WHERE NOT(NEW.is_times_two_zoom IN (0,1));
END
```

**Table 28 -- EXAMPLE: tile_table_metadata Insert Statement**

```SQL
INSERT INTO tile_table_metadata VALUES (
"sample_matrix_tiles",
1);
```

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/table 
REQ 43.
A GeoPackage SHALL include a tile_table_metadata table as defined in clause 10.3 and table 26.

Requirement: Extension
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/triggers
REQ 44.
A GeoPackage SHALL have tile_table_metadata table triggers as defined in clause 10.3 and table 27.

Requirement:Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_table_metadata/data
REQ 45.
A GeoPackage tile_table_metadata table SHALL contain a row record for each tile table in the GPKG as specified in clause 10.3.

### 10.4	Tile Matrix Metadata
A GeoPackage SHALL contain a tile_matrix_metadata table or view as defined in this clause.  The tile_matrix_metadata table or view SHALL contain one row record for each zoom level that contains one or more tiles in each tiles table.  It may contain row records for zoom levels in a tiles table that do not contain tiles.  A tile_matrix_metadata row record SHALL be inserted for a zoom level for t_table_name before any tiles are inserted into the corresponding tiles table, so that triggers on that table specified in clause 10.5 below may reference tile_matrix_metadata column values for that zoom level to reject invalid data. 

The tile_matrix_metadata table documents the structure of the tile matrix at each zoom level in each tiles table.  It allows GeoPackages to contain rectangular as well as square tiles (e.g. for better representation of polar regions).  It allows tile pyramids with zoom levels that differ in resolution by powers of 2, irregular intervals, or regular intervals other than powers of 2.  When the value of the is_times_two_zoom column in the tile_table_metadata record for a tiles table is 1 (true) then the pixel sizes for adjacent zoom levels in the tile_matrix_metadata table for that table SHALL only vary by powers of 2.

> NOTE 1:  Most tile pyramids have an origin at the upper left, a convention adopted by the OGC Web Map Tile Service (WMTS) [25], but some such as [TMS] (http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification) used by [MB-Tiles] (https://github.com/mapbox/mbtiles-spec) have an origin at the lower left.  Most tile pyramids, such as [Open Street Map] (http://wiki.openstreetmap.org/wiki/Main_Page), [OSMDroidAtlas] (http://wiki.openstreetmap.org/wiki/Main_Page), and [FalconView] (http://www.falconview.org/trac/FalconView) use a zoom_out_level of 0 for the smallest map scale “whole world” zoom level view, another convention adopted by WMTS, but some such as [Big Planet Tracks] http://code.google.com/p/big-planet-tracks/ invert this convention and use 0 or 1 for the largest map scale “local detail” zoom level view.   

GeoPackages SHALL follow the most frequently used conventions of a tile origin at the upper left and a zoom-out-level of 0 for the smallest map scale “whole world” zoom level view, as specified by [WMTS] (http://portal.opengeospatial.org/files/?artifact_id=35326).  The tile coordinate (0,0) SHALL always refer to the tile in the upper left corner of the tile matrix at any zoom level, regardless of the actual availability of that tile.  Pixel sizes for zoom levels sorted in ascending order SHALL be sorted in descending order.  

GeoPackages SHALL not require that tiles be provided for level 0 or any other particular zoom level.  This means that a tile matrix set can be sparse, i.e. not contain a tile for any particular position at a certain tile zoom level. This does not affect the spatial extent stated by the min/max x/y columns values in the geopackage_contents record for the same t_table_name, or the tile matrix width and height at that level.

> NOTE 2:  GeoPackage applications may query the tile_matrix_metadata table or the tiles (matrix set) table specified in clause 10.7 below to determine the minimum and maximum zoom levels for a given tile matrix table.  

> NOTE 3:  GeoPackage applications may query the tiles (matrix set) table to determine which tiles are available at each zoom level.

> NOTE 4:  GeoPackage applications that insert, update, or delete tiles (matrix set) table tiles row records are responsible for maintaining the corresponding descriptive contents of the tile_matrix_metadata table.  

> NOTE 5:  The geopackage_contents table (see clause 8.2 above) contains coordinates that define a bounding box as the stated spatial extent for all tiles in a tile (matrix set) table.  If the geographic extent of the image data contained in these tiles is within but not equal to this bounding box, then the non-image area of matrix edge tiles must be padded with no-data values, preferably transparent ones.

**Table 29 -- tile_matrix_metadata**
+ Table or View Name:  tile_matrix_metadata

|Column Name | Column Type | Column Description |	Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
|t_table_name |	text |	{RasterLayerName}_tiles |no	| | PK, FK |
| zoom_level	| integer |	0 <= zoom_level <= max_level for t_table_name	| no |	0 |	PK |
| matrix_width |	integer |	Number of columns (>= 1) in tile matrix at this zoom level | no |	1 | |	
| matrix_height |	integer |	Number of rows (>= 1) in tile matrix at this zoom level |	no | 1 | |	
| tile_width |	integer |	Tile width in pixels (>= 1)for this zoom level |	no |	256	| |
| tile_height |	integer |	Tile height in pixels (>= 1) for this zoom level |	no |	256	| |
| pixel_x_size |	double |	In t_table_name srid units or default meters for srid 0 (>0) |	no |	1 | |
| pixel_y_size |	double |	In t_table_name srid units or default meters for srid 0 (>0) |	no |	1	| |

**Table 30 -- tile_matrix_metadata Table Creation SQL**

```SQL
CREATE TABLE tile_matrix_metadata (
t_table_name TEXT NOT NULL,
zoom_level INTEGER NOT NULL,
matrix_width INTEGER NOT NULL,
matrix_height INTEGER NOT NULL,
tile_width INTEGER NOT NULL,
tile_height INTEGER NOT NULL,
pixel_x_size DOUBLE NOT NULL,
pixel_y_size DOUBLE NOT NULL,
CONSTRAINT pk_ttm PRIMARY KEY (t_table_name, zoom_level) ON CONFLICT ROLLBACK,
CONSTRAINT fk_ttm_t_table_name FOREIGN KEY (t_table_name) REFERENCES tile_table_metadata(t_table_name))
```

**Table 31 -- tile_matrix_metadata Trigger Definition SQL**

```SQL
CREATE TRIGGER 'tile_matrix_metadata_zoom_level_insert'
BEFORE INSERT ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''tile_matrix_metadata'' violates constraint: zoom_level cannot be less than 0')
WHERE (NEW.zoom_level < 0);
END

CREATE TRIGGER 'tile_matrix_metadata_zoom_level_update'
BEFORE UPDATE of zoom_level ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''tile_matrix_metadata'' violates constraint: zoom_level cannot be less than 0')
WHERE (NEW.zoom_level < 0);
END

CREATE TRIGGER 'tile_matrix_metadata_matrix_width_insert'
BEFORE INSERT ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''tile_matrix_metadata'' violates constraint: matrix_width cannot be less than 1')
WHERE (NEW.matrix_width < 1);
END

CREATE TRIGGER 'tile_matrix_metadata_matrix_width_update'
BEFORE UPDATE OF matrix_width ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''tile_matrix_metadata'' violates constraint: matrix_width cannot be less than 1')
WHERE (NEW.matrix_width < 1);
END

CREATE TRIGGER 'tile_matrix_metadata_matrix_height_insert'
BEFORE INSERT ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''tile_matrix_metadata'' violates constraint: matrix_height cannot be less than 1')
WHERE (NEW.matrix_height < 1);
END

CREATE TRIGGER 'tile_matrix_metadata_matrix_height_update'
BEFORE UPDATE OF matrix_height ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''tile_matrix_metadata'' violates constraint: matrix_height cannot be less than 1')
WHERE (NEW.matrix_height < 1);
END

CREATE TRIGGER 'tile_matrix_metadata_pixel_x_size_insert'
BEFORE INSERT ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''tile_matrix_metadata'' violates constraint: pixel_x_size must be greater than 0')
WHERE NOT (NEW.pixel_x_size > 0);
END

CREATE TRIGGER 'tile_matrix_metadata_pixel_x_size_update'
BEFORE UPDATE OF pixel_x_size ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''tile_matrix_metadata'' violates constraint: pixel_x_size must be greater than 0')
WHERE NOT (NEW.pixel_x_size > 0);
END

CREATE TRIGGER 'tile_matrix_metadata_pixel_y_size_insert'
BEFORE INSERT ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''tile_matrix_metadata'' violates constraint: pixel_y_size must be greater than 0')
WHERE NOT (NEW.pixel_y_size > 0);
END

CREATE TRIGGER 'tile_matrix_metadata_pixel_y_size_update'
BEFORE UPDATE OF pixel_y_size ON 'tile_matrix_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''tile_matrix_metadata'' violates constraint: pixel_y_size must be greater than 0')
WHERE NOT (NEW.pixel_y_size > 0);
END
```


**Table 32 -- EXAMPLE: tile_matrix_metadata Insert Statement**

```SQL
INSERT INTO tile_matrix_metadata VALUES (
"sample_matrix_tiles",
0,
1,
1,
512,
512,
2.0,
2.0)
```


Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/table 
REQ 46.
A GeoPackage SHALL include a tile_matrix_metadata table as defined in clause 10.4 and table 30.

Requirement: Extension
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/triggers
REQ 47.
A GeoPackage SHALL have triggers on the tile_matrix_metadata table as defined in clause 10.4 and table 31.

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_metadata/data
REQ 48.
A GeoPackage tile_matrix_metadata table SHALL contain one row record for each zoom level that contains one or more tiles in each tiles table.

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_zoom_levels/powers_of_two
REQ 49.
A GeoPackage SHALL support tile matrix set zoom levels for pixel sizes that differ by powers of two between adjacent zoom levels.

Requirement: Extension
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tile_matrix_zoom_levels/other_intervals
REQ 50.
A GeoPackage SHALL support tile matrix set zoom levels for pixel sizes that differ by irregular intervals or by regular intervals other than powers of two between adjacent zoom levels.

### 10.5	Tiles Table
Tiles in a tile matrix set with one or more zoom levels SHALL be stored in a GeoPackage in a tiles table or view with a unique name for every different tile matrix set in the GeoPackage.  Each tiles table or view SHALL be defined with the columns described in table 35 below.  Each tiles table or view SHALL contain tile matrices at one or more zoom levels of different spatial resolution (map scale).  All tiles at a particular zoom level must have the same pixel_x_size and pixel_y_size values specified in the tile_matrix_metadata row record for that tiles table and zoom level.  

When the value of the is_times_two_zoom column in the tile_table_metadata record for a tiles table row is 1 (true) then the pixel sizes for adjacent zoom levels in the tiles table SHALL only vary by powers of 2.

> NOTE 1:  The id primary key allows tiles table views to be created on RasterLite [B13] version 1 raster table implementations, where the tiles are selected based on a spatially indexed bounding box in a separate metadata table.  

> NOTE 2:  The zoom_level / tile_column / tile_row unique key allows tiles to be selected and accessed by “z, x, y”, a common convention used by MB-Tiles [B12], Big Planet [B17], and other implementations.  In a SQLite implementation this unique key is automatically indexed.  This table / view definition may also follow RasterLite [B13] version 1 conventions, where the tiles are selected based on a spatially indexed bounding box in a separate metadata table.

GeoPackages SHALL implement appropriate SQL triggers on each tiles table by executing the add_tile_triggers() routine specified in clause 10.8 below with the tiles table as a parameter value to ensure that 

1.	The zoom_level value is specified for the tiles table in the tile_matrix_metadata table

2.	The tile column value is between 0 and the matrix_height specified for the zoom_level in the tile_matrix_metadata table

3.	The tile _row value is between 0 and the matrix_width specified for the zoom_level in the tile_matrix_metadata table

**Table 33 – tiles table** 
+ Table or View Name:   {TilesTableName} tiles table

|Column Name | Column Type | Column Description |  Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
|id	integer	 | Autoincrement primary key |	no |	|	PK |
|zoom_level |	integer	min(zoom_level) <= zoom_level <= max(zoom_level)  for t_table_name |	no |	0	 | UK |
|tile_column |	integer	0 to tile_matrix_metadata matrix_width – 1 |	no |	0	| UK |
|tile_row |	integer	0 to tile_matrix_metadata matrix_height - 1 |	no	| 0 |	UK |
|tile_data |	BLOB	Of an image MIME type specified in clause 10.2 | no	| | |	

**Table 34 -- EXAMPLE: tiles table Create Table SQL**

```SQL
CREATE TABLE sample_matrix_tiles (
id INTEGER PRIMARY KEY AUTOINCREMENT,
zoom_level INTEGER NOT NULL DEFAULT 0,
tile_column INTEGER NOT NULL DEFAULT 0,
tile_row INTEGER NOT NULL DEFAULT 0,
tile_data BLOB NOT NULL DEFAULT (zeroblob(4)),
UNIQUE (zoom_level, tile_column, tile_row))
```


> NOTE 3:  zeroblob(n) is an SQLite function.


**Table 35 – EXAMPLE: tiles table Trigger Definition SQL**

```SQL
SELECT add_tile_triggers(‘sample_matrix_tiles’)
/* creates the following triggers */

CREATE TRIGGER "sample_matrix_tiles_zoom_insert"
BEFORE INSERT ON "sample_matrix_tiles"
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''sample_matrix_tiles'' violates constraint: zoom_level not specified for table in tile_matrix_metadata')
WHERE NOT (NEW.zoom_level IN (SELECT zoom_level FROM tile_matrix_metadata WHERE t_table_name = 'sample_matrix_tiles')) ;
END

CREATE TRIGGER "sample_matrix_tiles_zoom_update"
BEFORE UPDATE OF zoom_level ON "sample_matrix_tiles"
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''sample_matrix_tiles'' violates constraint: zoom_level not specified for table in tile_matrix_metadata')
WHERE NOT (NEW.zoom_level IN (SELECT zoom_level FROM tile_matrix_metadata WHERE t_table_name = 'sample_matrix_tiles')) ;
END

CREATE TRIGGER "sample_matrix_tiles_tile_column_insert"
BEFORE INSERT ON "sample_matrix_tiles"
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''sample_matrix_tiles'' violates constraint: tile_column cannot be < 0')
WHERE (NEW.tile_column < 0) ;
SELECT RAISE(ROLLBACK, 'insert on table ''sample_matrix_tiles'' violates constraint: tile_column must by < matrix_width specified for table and zoom level in tile_matrix_metadata')
WHERE NOT (NEW.tile_column < (SELECT matrix_width FROM tile_matrix_metadata WHERE t_table_name = 'sample_matrix_tiles' AND zoom_level = NEW.zoom_level));
END

CREATE TRIGGER "sample_matrix_tiles_tile_column_update"
BEFORE UPDATE OF tile_column ON "sample_matrix_tiles"
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''sample_matrix_tiles'' violates constraint: tile_column cannot be < 0')
WHERE (NEW.tile_column < 0) ;
SELECT RAISE(ROLLBACK, 'update on table ''sample_matrix_tiles'' violates constraint: tile_column must by < matrix_width specified for table and zoom level in tile_matrix_metadata')
WHERE NOT (NEW.tile_column < (SELECT matrix_width FROM tile_matrix_metadata WHERE t_table_name = 'sample_matrix_tiles' AND zoom_level = NEW.zoom_level));
END

CREATE TRIGGER "sample_matrix_tiles_tile_row_insert"
BEFORE INSERT ON "sample_matrix_tiles"
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''sample_matrix_tiles'' violates constraint: tile_row cannot be < 0')
WHERE (NEW.tile_row < 0) ;
SELECT RAISE(ROLLBACK, 'insert on table ''sample_matrix_tiles'' violates constraint: tile_row must by < matrix_height specified for table and zoom level in tile_matrix_metadata')
WHERE NOT (NEW.tile_row < (SELECT matrix_height FROM tile_matrix_metadata WHERE t_table_name = 'sample_matrix_tiles' AND zoom_level = NEW.zoom_level));
END

CREATE TRIGGER "sample_matrix_tiles_tile_row_update"
BEFORE UPDATE OF tile_row ON "sample_matrix_tiles"
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''sample_matrix_tiles'' violates constraint: tile_row cannot be < 0')
WHERE (NEW.tile_row < 0) ;
SELECT RAISE(ROLLBACK, 'update on table ''sample_matrix_tiles'' violates constraint: tile_row must by < matrix_height specified for table and zoom level in tile_matrix_metadata')
WHERE NOT (NEW.tile_row < (SELECT matrix_height FROM tile_matrix_metadata WHERE t_table_name = 'sample_matrix_tiles' AND zoom_level = NEW.zoom_level));
END
```
 

**Table 36 -- EXAMPLE:  tiles table Insert Statement**
```SQL
INSERT INTO sample_matrix_tiles VALUES (
1,
1,
1,
1,
"BLOB VALUE")
```

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/table 
REQ 51.
All tile matrix sets in a GeoPackage SHALL be contained in tiles tables defined as specified in clause 10.5 and table 33and exemplified by table 34.

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/raster_column
REQ 52.
All tile table tile_data raster columns in a GeoPackage SHALL be defined with a BLOB data type that is an image mime type as specified in clause 10.2. 

Requirement: Extension
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/tiles_table/triggers
REQ 53.
All tile matrix set tables in a GeoPackage SHALL have triggers defined by executing the add_tile_triggers() routine specified in clause 10.8 as exemplified by table 35.

### 10.6 Raster Tables

Raster tables have raster columns defined as BLOB data types that contain rasters that are not part of tile matrix sets.  Every table in a GeoPackage that is not a tiles tables as as described in clause 9.5 and that includes one or more raster columns is a raster table.  Raster tables are also feature tables as specified in clause 8.4 above that may or may not have geometry columns in addition to raster columns.

Every raster table in a GeoPackage shall have a primary key defined on one or more columns so that row level metadata records may be linked to the rasters in it by rowid as described in clauses 10.7 and 11.3 below.

NOTE1: An integer column primary key is recommended for best performance.

**Table 39 -- EXAMPLE: sample_rasters Table or View**
+ Table or View Name:   {TilesTableName} sample_rasters

|Column Name | Column Type | Column Description |  Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
|id integer	 | Autoincrement primary key |	no |	|	PK |
|elevation  | BLOB | Elevation coverage; of type raster_format_metadata.mime_type | no | | |
|description | text | Description of the area | no | 'no desc' | |
|photo | BLOB | Photograph of the area; of type_raster_format_metadata.mime_type | no | |

**Table 40 -- EXAMPLE: sample_rasters Table Definition SQL**

```SQL
CREATE TABLE sample_rasters (
id INTEGER PRIMARY KEY AUTOINCREMENT,
elevation BLOB NOT NULL,
description TEXT NOT NULL DEFAULT 'no_desc',
photo BLOB NOT NULL)
```

NOTE2: The sample_rasters table created in Table 40 above could be extended with one or more geometry columns by calls to the addGeometryColumn() routine specified in clause 9.4 to have both raster and geometry columns like the sample_feature_table shown in Figure3: GeoPackageTables above in clause 7.

**Table 41 -- EXAMPLE: sample_rasters Insert Statement
```SQL
INSERT INTO sample_rasters VALUES (
1,
{Elevation Raster},
'rough terrain',
{Area Photo} )
```

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/table
REQ 64.
All raster images in a GeoPackage that are not tiles in a tiles table shall be contained in rasters tables that are defined as specified by clause 10.6 and exemplified by tables 39 and 40.

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/primary_key
REQ 65.
Every raster table in a GeoPackage shall have a primary key defined on one or more columns as specified by clause 10.6

Requirement: Core
http://www.opengis.net/spec/GPKG/1.0/req/rasters_tiles/raster_table/raster_column
REQ 66.
All raster table raster columns in a GeoPackage shall be defined with a BLOB data type that is an image mime type as specified in clause 10.2.

