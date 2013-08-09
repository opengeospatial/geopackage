The optional capabilities specified in this section depend on the required capabilities specified in the [Base section](1_base.md).

## 2.2. Tiles

The optional capabilities defined in sub-clauses and requirement statements of this clause MAY be implemented by any GeoPackage file.

#### 2.2.1. Tile Matrix Introduction

There are a wide variety of commercial and open source conventions for storing, indexing, accessing
and describing tiles in tile matrix pyramids. Unfortunately, no applicable existing consensus,
national or international specifications have standardized practices in this domain. In addition,
various image file formats have different representational capabilities, and include different self-
descriptive metadata.  The tile store data / metadata model and conventions described below support
direct use of tiles in a GeoPackage in two ways. First, they specify how existing applications MAY
create SQL Views of the data /metadata model on top of existing application tables that that follow
different interface conventions. Second, they include and expose enough metadata information at both
the dataset and record levels to allow applications that use GeoPackage data to discover its
characteristics without having to parse all of the stored images. Applications that store GeoPackage
tile data, which are presumed to have this information available, SHALL store sufficient metadata to
enable its intended use.

The GeoPackage tile store data model MAY be implemented directly as SQL tables in a SQLite database
for maximum performance, or as SQL views on top of tables in an existing SQLite tile store for
maximum adaptability and loose coupling to enable widespread implementation.

A GeoPackage CAN store multiple raster and tile pyramid data sets in different tables or views in the same container.[^1]

The tables or views that implement the GeoPackage tile store data / metadata model are described and discussed individually in the following subsections.

#### 2.2.2. Contents
##### 2.2.2.1 Data
##### 2.2.2.1.1. Contents Table – Tiles Row

> **Req 28:** A `gpkg_contents` table or updateable view SHALL contain a row with a `data_type` column value of “tiles” for each tile matrix user data table.

#### 2.2.3. Zoom Levels
##### 2.2.3.1. Data
##### 2.2.3.1.1. Zoom Times Two

> **Req 29:** In a GeoPackage file that contains a tile matrix user data table that contains tile data, by default [^2], zoom level pixel sizes for that table SHALL vary by powers of 2 between adjacent zoom levels in the tile matrix metadata table.

#### 2.2.4. Tile Encoding PNG 
##### 2.2.4.1. Data
##### 2.2.4.1.1. MIME Type PNG

> **Req 30:** In a GeoPackage file that contains a tile matrix user data table that contains tile data that is not [MIME type](http://www.ietf.org/rfc/rfc2046.txt) [image/jpeg](http://www.jpeg.org/public/jfif.pdf), by default SHALL store that tile data in [MIME type](http://www.iana.org/assignments/media-types/index.html) [image/png](http://libpng.org/pub/png/).[^3] 

#### 2.2.5. Tile Encoding JPEG
##### 2.2.5.1. Data
##### 2.2.5.1.1. MIME Type JPEG

> **Req 31:** In a GeoPackage file that contains a tile matrix user data table that contains tile data that is not [MIME type](http://www.iana.org/assignments/media-types/index.html) [image/png](http://libpng.org/pub/png/), by default SHALL store that tile data in [MIME type](http://www.ietf.org/rfc/rfc2046.txt) [image/jpeg](http://www.jpeg.org/public/jfif.pdf), [^4]

#### 2.2.6. Tile Matrix Metadata
##### 2.2.6.1. Data
##### 2.2.6.1.1. Table Definition

> **Req 32:** A GeoPackage that contains a tile matrix user data table SHALL contain a `gpkg_tile_matrix_metadata` table per clause 2.2.6.1.1, Table 7 and 28.** 

|Column Name | Column Type | Column Description |	Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
| `t_table_name` |	text |	\{RasterLayerName\}_tiles |no	| | PK, FK |
| `zoom_level`	| integer |	0 <= `zoom_level` <= max_level for `t_table_name`	| no |	0 |	PK |
| `matrix_width` |	integer |	Number of columns (>= 1) in tile matrix at this zoom level | no |	1 | |	
| `matrix_height` |	integer |	Number of rows (>= 1) in tile matrix at this zoom level |	no | 1 | |	
| `tile_width` |	integer |	Tile width in pixels (>= 1)for this zoom level |	no |	256	| |
| `tile_height` |	integer |	Tile height in pixels (>= 1) for this zoom level |	no |	256	| |
| `pixel_x_size` |	double |	In `t_table_name` srid units or default meters for srid 0 (>0) |	no |	1 | |
| `pixel_y_size` |	double |	In `t_table_name` srid units or default meters for srid 0 (>0) |	no |	1	| |


The `gpkg_tile_matrix_metadata` table documents the structure of the tile matrix at each zoom level
in each tiles table. It allows GeoPackages to contain rectangular as well as square tiles (e.g. for
better representation of polar regions). It allows tile pyramids with zoom levels that differ in
resolution by powers of 2, irregular intervals, or regular intervals other than powers of 2.

See Annex C: Table Definition SQL clause C.6 `gpkg_tile_matrix_metadata`

##### 2.2.6.1.2. Table Data Values
> **Req 33:** Values of the `gpkg_tile_matrix_metadata` `table_name` column SHALL reference values in the `gpkg_contents` `table_name` column for rows with a `data_type` of “tiles”.

> **Req 34:** A `gpkg_tile_matrix_metadata` table SHALL contain one row record for each zoom level that contains one or more tiles in each tile matrix user data table.

The `gpkg_tile_matrix_metadata` table or view MAY contain row records for zoom levels in a tiles
table that do not contain tiles. GeoPackages follow the most frequently used conventions of a tile
origin at the upper left and a zoom-out-level of 0 for the smallest map scale “whole world” zoom
level view[^5], as specified by [WMTS](http://portal.opengeospatial.org/files/?artifact_id=35326).
The tile coordinate (0,0) always refers to the tile in the upper left corner of the tile matrix at
any zoom level, regardless of the actual availability of that tile.

> **Req 35:** The `zoom_level` column value in a `gpkg_tile_matrix_metadata` table row SHALL not be negative.

> **Req 36:** The `matrix_width` column value in a `gpkg_tile_matrix_metadata` table row SHALL be greater than 0.

> **Req 37:** The `matrix_height` column value in a `gpkg_tile_matrix_metadata` table row SHALL be greater than 0.

> **Req 38:** The `tile_width` column value in a `gpkg_tile_matrix_metadata` table row SHALL be greater than 0. 

> **Req 39:** The `tile_height` column value in a `gpkg_tile_matrix_metadata` table row SHALL be greater than 0.

> **Req 40:** The `pixel_x_size` column value in a `gpkg_tile_matrix_metadata` table row SHALL be greater than 0.

> **Req 41:** The `pixel_y_size` column value in a `gpkg_tile_matrix_metadata` table row SHALL be greater than 0.

> **Req 42:** The `pixel_x_size` and `pixel_y_size` column values for `zoom_level` column values in a `gpkg_tile_matrix_metadata` table sorted in ascending order SHALL be sorted in descending order.

Tiles MAY or MAY NOT be provided for level 0 or any other particular zoom level.[^6] This means that a
tile matrix set can be sparse, i.e. not contain a tile for any particular position at a certain tile
zoom level.[^7] This does not affect the spatial extent stated by the min/max x/y columns values in the
`gpkg_contents` record for the same `table_name`, or the tile matrix width and height at that
level.[^8]

#### 2.2.7. Tile Matrix User Data
##### 2.2.7.1. Data
##### 2.2.7.1.1. Table Definition

> **Req 43:** Each tile matrix set in a GeoPackage file SHALL be stored in a different tiles table or updateable view with a unique name per clause 2.2.7.1.1, 8and 31.

|Column Name | Column Type | Column Description |  Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
| `id` |	integer	| Autoincrement primary key |	no |	|	PK |
| `zoom_level` |	integer |	min(zoom_level) <= `zoom_level` <= max(zoom_level)  for `t_table_name` |	no |	0	 | UK |
| `tile_column` |	integer	| 0 to `gpkg_tile_matrix_metadata` `matrix_width` – 1 |	no |	0	| UK |
| `tile_row` |	integer	| 0 to `gpkg_tile_matrix_metadata` `matrix_height` - 1 |	no	| 0 |	UK |
| `tile_data` |	BLOB	| Of an image MIME type specified in clause 10.2 | no	| | |	


See Annex C: Table Definition SQL clause C.7 `sample_matrix_tiles` 

##### 2.2.7.1.2. Table Data Values

Each tiles table or view[^9] MAY contain tile matrices at zero or more zoom levels of different spatial resolution (map scale).

> **Req 44:** For each distinct `table_name` from the `gpkg_tile_matrix_metadata` (tmm) table, the tile matrix set (tms) user data table `zoom_level` column value in a GeoPackage file SHALL be in the range min(tmm.zoom\_level) <= tms.zoom\_level <= max(tmm.zoom\_level).

> **Req 45:** For each distinct `table_name` from the `gpkg_tile_matrix_metadata` (tmm) table, the tile matrix set (tms) user data table `tile_column` column value in a GeoPackage file SHALL be in the range 0 <= tms.tile\_column <= tmm.matrix\_width – 1 where the tmm and tms `zoom_level` column values are equal.

> **Req 46:** For each distinct `table_name` from the `gpkg_tile_matrix_metadata` (tmm) table, the tile matrix set (tms) user data table `tile_row` column value in a GeoPackage file SHALL be in the range 0 <= tms.tile_row <= tmm.matrix_height – 1 where the tmm and tms `zoom_level` column values are equal.

All tiles at a particular zoom level have the same `pixel_x_size` and `pixel_y_size` values specified in the `gpkg_tile_matrix_metadata` row record for that tiles table and zoom level.[^10] 


[^1]: Images of multiple MIME types MAY be stored in given table. For example, in a tiles table, image/png format tiles without compression could be used for transparency where there is no data on the tile edges, and image/jpeg format tiles with compression could be used for storage efficiency where there is image data for all pixels. Images of multiple bit depths of the same MIME type MAY also be stored in a given table, for example image/png tiles in both 8 and 24 bit depths.

[^2]: See clause 3.2.1.1.1 for use of other zoom levels as a registered extensions.

[^3]: See Clauses 3.2.2, 3.2.3, 3.2.4 and 3.2.5 regarding use of alternative tile MIME types as registered extensions. 

[^4]: See Clauses 3.2.2, 3.2.3, 3.2.4 and 3.2.5 regarding use of alternative tile MIME types as registered extensions.

[^5]: GeoPackage applications MAY query the `gpkg_tile_matrix_metadata` table or the tile matrix user data table to determine the minimum and maximum zoom levels for a given tile matrix table.

[^6]: GeoPackage applications MAY query the tiles (matrix set) table to determine which tiles are available at each zoom level.

[^7]: GeoPackage applications that insert, update, or delete tiles (matrix set) table tiles row records are responsible for maintaining the corresponding descriptive contents of the `gpkg_tile_matrix_metadata` table.

[^8]: The `gpkg_contents` table contains coordinates that define a bounding box as the stated spatial extent for all tiles in a tile (matrix set) table. If the geographic extent of the image data contained in these tiles is within but not equal to this bounding box, then the non-image area of matrix edge tiles must be padded with no-data values, preferably transparent ones.

[^9]: 1 A GeoPackage is not required to contain any tile matrix data tables. Tile matrix user data tables in a GeoPackage MAY be empty.

[^10]: The `zoom_level` / `tile_column` / `tile_row` unique key is automatically indexed, and allows tiles to be selected and accessed by “z, x, y”, a common convention used by some implementations. This table / view definition MAY also allow tiles to be selected based on a spatially indexed bounding box in a separate metadata table.
