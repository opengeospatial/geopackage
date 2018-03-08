## Getting Started

### Identifying a GeoPackage
A [GeoPackage](http://geopackage.org) is an [SQLite Database](http://sqlite.org/index.html) file with a [`.gpkg` extension](http://www.geopackage.org/spec120/#r3). 
If you are unsure whether a file is an SQLite database, a binary or text editor should reveal that its starting bytes are [`SQLite format 3`](http://www.geopackage.org/spec120/#r1).

### Opening a GeoPackage
There are a number of ways to open a GeoPackage. 
* For a direct SQL interface, consider [DB Browser for SQLite](http://sqlitebrowser.org/)
* For a web application, consider [NGA's application](http://ngageoint.github.io/geopackage-js/) as long as the file isn't too big
* For a desktop application, consider [QGIS](https://qgis.org/en/site/)
* Many more options are listed on the [implementations page](http://www.geopackage.org/implementations.html)

### Creating a GeoPackage
Similarly, to create a new GeoPackage from scratch or from an existing file (e.g., a shapefile or .csv):
* For direct SQL access, start with the [empty geopackage template](http://www.geopackage.org/data/empty.gpkg)
* For a desktop application, consider [QGIS](https://qgis.org/en/site/)
* For a command line program, consider [GDAL](http://www.gdal.org) vector and raster utilities 
* This [blog post](http://www.fulcrumapp.com/blog/working-with-geodata/) provides an example that steps through creating a geopackage using ogr2ogr, as well as how to add the [spatialite](https://www.gaia-gis.it/fossil/libspatialite/index) extension to enable further spatial analysis in SQLite.

### Checking a GeoPackage Version
The easiest way to check a GeoPackage version is using a direct SQL interface such as DB Browser. SQLite uses [`pragma` statements](https://www.sqlite.org/pragma.html) to implement non-standard SQL functions. 
These can be executed just like any other SQL statement and where relevant, they return a result set. The two pragmas you need to know are:
* `PRAGMA application_id`
   * 1196444487 (the 32-bit integer value of 0x47504B47 or `GPKG` in ASCII) for GPKG 1.2 and greater 
   * 1196437808 (the 32-bit integer value of 0x47503130 or `GP10` in ASCII) for GPKG 1.0 or 1.1
* `PRAGMA user_version`
   * For versions 1.2 and later, this returns an integer representing the version number in the form MMmmPP (MM = major version, mm = minor version, PP = patch). Therefore 1.2 is 10200.
   
### What is in a GeoPackage
GeoPackage tables fall into two categories, metadata tables and user-defined (content) tables. 
There are two required metadata tables, [`gpkg_contents`](#gpkg_contents) and [`gpkg_spatial_ref_sys`](#gpkg_spatial_ref_sys). 
The name of the user-defined table is generally the key for the metadata tables. 
The structure of user-defined tables and the presence of other metadata tables are dictated by the content being stored (see [Content Types](#content-types)).

#### [`gpkg_contents`](http://www.geopackage.org/spec120/#_contents)
This table is the table of contents for a GeoPackage. 
The columns:
* `table_name`: the actual name of the user-defined table containing the data (this is also the primary key for this table)
* `data_type`: the data type, e.g., "tiles", "features", "attributes" or some other type provided by an extension
* `identifier` and `description`: human-readable text ("identifier" is analogous to "title")
* `last_change`: the informational date of last change, in ISO 8601 format (for practical purposes, [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) applies)
* `min_x`, `min_y`, `max_x`, and `max_y`: the spatial extents of the content. This is informational and often used by clients to provide a default view window
* `srs_id`: spatial reference system (see next subsection)

#### [`gpkg_spatial_ref_sys`](http://www.geopackage.org/spec120/#spatial_ref_sys)
For content that has spatial reference (including but not limited to tiles and features), each row in contents must reference a coordinate reference system which is stored in the `gpkg_spatial_ref_sys` table. 
The columns:
* `srs_name`, `description`: a human readable name and description for the SRS 
* `srs_id`: a unique identifier for the SRS; also the primary key for the table
* `organization`: Case-insensitive name of the defining organization e.g., `EPSG` or `epsg`
* `organization_coordsys_id`: Numeric ID of the SRS assigned by the organization
* `definition`: Well Known Text definition of the SRS

At least three rows must be in this table; there must be one row for each of the following `srs_id` column values:
* 4326: latitude and longitude coordinates on the WGS84 reference ellipsoid
* 0: undefined geographic coordinate reference systems
* -1: undefined Cartesian coordinate reference systems

However, many more are possible. 
Using coordinate reference systems incorrectly is one of the most common ways to break GeoPackage interoperability. 
When in doubt, discuss with a geospatial expert to ensure that you are using an appropriate coordinate reference system for your situation.

### Content Types

#### [Features](http://www.geopackage.org/spec120/#features)
Vector feature data represents geolocated entities including conceptual ones such as districts, real world objects such as roads and rivers, and observations thereof. 
There is one additional required table, `gpkg_geometry_columns`. 
Features are stored in the user data tables identified by the `table_name` values in `gpkg_contents` (one table per row). 

<img src="http://www.geopackage.org/spec120/geopackage-features.png"/>
> Figure 1: UML Diagram of Features tables

##### [`gpkg_geometry_columns`](http://www.geopackage.org/spec120/#_geometry_columns)
This table describes the geometry for a particular Features table. 
Each feature table must have a corresponding row in this table. The columns:
* `table_name` and `column_name` where the geometries are stored
* [`geometry_type_name`](http://www.geopackage.org/spec120/#geometry_types_core) 
* `srs_id` the spatial reference system (see above)
* `z` and `m` are flags to indicate 3D/4D applications (Z values are for height/elevation/depth and M values are reserved for other types of domain-specific measurements)

##### [User Data Tables](http://www.geopackage.org/spec120/#feature_user_tables)
Features are stored in user-defined data tables. Each features table has exactly one geometry column, a BLOB. 
(The structure of this BLOB is described [here](http://www.geopackage.org/spec120/#gpb_format).) 
The supported geometry types are the [OGC Simple Features geometry types](http://www.geopackage.org/spec120/#geometry_types_core). 
Other than the geometry column and a primary key, the schema of a features table is up to the implementer. 
Properties (text, integer, or real) provide additional information about each feature. 
The specification has an [example schema](http://www.geopackage.org/spec120/#example_feature_table_cols).

#### [Tiles](http://www.geopackage.org/spec120/#tiles)
The Tiles option specifies a mechanism for storing raster data in tile pyramids. 
"Tile pyramid" refers to the concept of pyramid structure of tiles of different spatial extent and resolution at different zoom levels, and the tile data itself. 
"Tile" refers to an individual raster image such as a PNG or JPEG that covers a specific geographic area. 
"Tile matrix" refers to rows and columns of tiles that all have the same spatial extent and resolution at a particular zoom level. 
"Tile matrix set" refers to the definition of a tile pyramid’s tiling structure. 
This mechanism is based on the model for tile matrix sets described in Section 6 of the [WMTS Implementation Specification](http://www.opengeospatial.org/standards/wmts).

There are two additional required tables, [`gpkg_tile_matrix_set`](#gpkg_tile_matrix_set) and [`gpkg_tile_matrix`](#gpkg_tile_matrix). 
In addition, each tile pyramid requires a [user defined table](http://www.geopackage.org/spec120/#tiles_user_tables) that contains the actual tiles.

<img src="http://www.geopackage.org/spec120/geopackage-tiles.png"/>
> Figure 2: UML Diagram of Tiles tables

##### [`gpkg_tile_matrix_set`](http://www.geopackage.org/spec120/#_tile_matrix_set)
This table describes names a tile matrix set (pyramid). The columns:
* `table_name` and `srs_id` match the entries in `gpkg_contents`
* `min_x`, `min_y`, `max_x`, and `max_y`: the actual spatial extents of the tile pyramid. 
This is must be exact so that applications can use this information to geolocate tiles correctly. 
(This is in contrast with the extents in `gpkg_contents` which are informative.)

##### [`gpkg_tile_matrix`](http://www.geopackage.org/spec120/#tile_matrix)
Each tile matrix set is composed of one or more tile matrices, each identified by its zoom level. 
The columns:
* `table_name` matches the entry in `gpkg_contents` and elsewhere
* `zoom_level` indicates the zoom levels present in the file.
* `matrix_width` and `matrix_height` describe the size of the tile matrix in tiles
* `tile_width` and `tile_height` describe the size of each tile in pixels
* `pixel_x_size` and `pixel_y_size` describe the size of each pixel 

By default, zoom levels are separated by powers of two, but if this is inappropriate for your scenario, other multiples are possible with the [Zoom Other Levels](http://www.geopackage.org/spec120/#extension_zoom_other_intervals) extension.

##### [User Data Tables](http://www.geopackage.org/spec120/#tiles_user_tables)
Actual tiles are stored in user data tables with a specific schema. 
The columns:
* `id` is a primary key
* `zoom_level` indicates which tile matrix this tile is part of
* `tile_column` and `tile_row` are the zero-indexed tile number
* `tile_data` is the BLOB containing the tile image

Unless you use an extension, PNG and JPG are the two supported file types for the tiles. 
PNG is generally better for synthetic data (i.e., digital maps) because it is lossless and its compression codec compresses synthetic data fairly well. 
JPG is generally better for natural data (i.e., satellite or aerial imagery) due to its superior (though lossy) compression. 
However, since PNG supports alpha transparency and JPG does not, it is common to use PNG tiles around the boundary of a tile pyramid. 
This allows users to see the data underneath the tile boundaries. 
JPG files have an adjustable compression rating. 
We have found that a ratings in the range 50-75 (out of 100) work best for imagery. 
Ratings that are too high use too much space and ratings that are too low have too many visible artifacts. 
Within the 50-75 range it is a reasonable tradeoff between file size and image quality.

Tile pyramids may be sparsely populated. 
This is a good way to manage GeoPackage size. 
Applications should be aware of this possibility and if possible, drop to the next zoom level to render that part of the map. 

#### [Attributes](http://www.geopackage.org/spec120/#attributes)
Attributes are tables that solely contain non-spatial data. 
This data is commonly joined with spatial data as required by an application. The rules for this data are pretty wide open. 
