# Safe GeoPackage Tiles

### Introduction

This file will eventually be a complementary specification to the GeoPackage Tiles
Specification, that has the triggers and table creation SQL to create a GeoPackage
that will maintain its consistency.

For the immediate term, however, it will just be a spot for the big long SQL blocks
in the specification to live, so they don't clutter it up.

## SQL Tables

### 1.0 raster_columns SQL

**Table 1.1** - `raster_columns` Table Definition SQL

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

The `raster_columns` table or view in a GeoPackage SHALL have the triggers defined in *Table 1.2* below.

**Table 1.2** - `raster_columns` Trigger Definition SQL

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

**Table 1.3** - EXAMPLE: `raster_columns` INSERT Statement

```SQL
INSERT INTO raster_columns VALUES (
"sample_matrix_tiles",
"tile_data",
90,
2,
4326)
```

-
### 2.0 tile_table_metadata SQL

**Table 2.1** - `tile_table_metadata` Table Definition SQL

```SQL
CREATE TABLE tile_table_metadata (
  t_table_name TEXT NOT NULL PRIMARY KEY,
  is_times_two_zoom INTEGER NOT NULL DEFAULT 1
)
```

**Table 2.2** - `tile_table_metadata` Trigger Definition SQL

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

**Table 2.3** - EXAMPLE: `tile_table_metadata` Insert Statement

```SQL
INSERT INTO tile_table_metadata VALUES (
"sample_matrix_tiles",
1);
```

-
### 3.0 tile_matrix_metadata SQL

**Table 3.1** - `tile_matrix_metadata` Table Creation SQL

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

**Table 3.2** - `tile_matrix_metadata` Trigger Definition SQL

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

**Table 3.3** - EXAMPLE: `tile_matrix_metadata` Insert Statement

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

-
### 4.0 sample_matrix_tiles SQL

**Table 4.1** - EXAMPLE: `sample_matrix_tiles` Table Definition SQL

```SQL
CREATE TABLE sample_matrix_tiles (
id INTEGER PRIMARY KEY AUTOINCREMENT,
zoom_level INTEGER NOT NULL DEFAULT 0,
tile_column INTEGER NOT NULL DEFAULT 0,
tile_row INTEGER NOT NULL DEFAULT 0,
tile_data BLOB NOT NULL DEFAULT (zeroblob(4)),
UNIQUE (zoom_level, tile_column, tile_row))
```

> NOTE 4.1:  zeroblob(n) is an SQLite function.

**Table 4.2** – EXAMPLE: `sample_matrix_tiles` Trigger Definition SQL

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
 
**Table 4.3** - EXAMPLE:  `sample_matrix_tiles` Insert Statement

```SQL
INSERT INTO sample_matrix_tiles VALUES (
1,
1,
1,
1,
"BLOB VALUE")
```
-
### 5.0 sample_rasters SQL

**Table 5.1** - EXAMPLE: `sample_rasters` Table Definition SQL

```SQL
CREATE TABLE sample_rasters (
id INTEGER PRIMARY KEY AUTOINCREMENT,
elevation BLOB NOT NULL,
description TEXT NOT NULL DEFAULT 'no_desc',
photo BLOB NOT NULL)
```

> NOTE 5.1: The `sample_rasters` table created in Table 40 above could be extended with one or more 
geometry columns by calls to the `addGeometryColumn()` routine specified in clause 9.4 to have 
both raster and geometry columns like the `sample_feature_table` shown in Figure3: GeoPackageTables above in clause 7.

**Table 5.2** - EXAMPLE: `sample_rasters` Insert Statement

```SQL
INSERT INTO sample_rasters VALUES (
1,
{Elevation Raster},
'rough terrain',
{Area Photo} )
```

-
### 6.0 {RasterLayerName}_rt_metadata SQL

**Table 6.1** - EXAMPLE: `{RasterLayerName}_rt_metadata` Table Definition SQL

```SQL
CREATE TABLE sample_matrix_tiles_rt_metadata (
row_id_value INTEGER NOT NULL,
r_raster_column TEXT NOT NULL DEFAULT 'tile_data',
compr_qual_factor INTEGER NOT NULL DEFAULT -1,
georectification INTEGER NOT NULL DEFAULT -1,
min_x DOUBLE NOT NULL DEFAULT -180.0,
min_y DOUBLE NOT NULL DEFAULT -90.0,
max_x DOUBLE NOT NULL DEFAULT 180.0,
max_y DOUBLE NOT NULL DEFAULT 90.0,
CONSTRAINT pk_smt_rm PRIMARY KEY (row_id_value, r_raster_column)
ON CONFLICT ROLLBACK
)
```

**Table 6.2** - EXAMPLE: `{RasterLayerName}_rt_metadata` Trigger Definition SQL

```SQL
SELECT add_rt_metadata_triggers('sample_rasters')
/* creates the following triggers */

CREATE TRIGGER 'sample_rasters_rt_metadata_r_raster_column_insert'
BEFORE INSERT ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''sample_rasters_rt_metadata'' violates constraint: r_raster_column must be specified for table sample_rasters in table raster_columns')
WHERE (NOT (NEW.r_raster_column IN (SELECT DISTINCT r_raster_column FROM raster_columns WHERE r_table_name = 'sample_rasters')));
END

CREATE TRIGGER 'sample_rasters_rt_metadata_r_raster_column_update'
BEFORE UPDATE OF r_raster_column ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''sample_rasters_rt_metadata'' violates constraint: r_raster_column must be specified for table sample_rasters in table raster_columns')
WHERE (NOT (NEW.r_raster_column IN (SELECT DISTINCT r_raster_column FROM raster_columns WHERE r_table_name = 'sample_rasters')));
END

CREATE TRIGGER 'sample_rasters_rt_metadata_georectification_insert'
BEFORE INSERT ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''sample_rasters_rt_metadata'' violates constraint: georectification must be -1, 0, 1 or 2')
WHERE (NOT (NEW.georectification IN (-1, 0, 1, 2)));
END

CREATE TRIGGER 'sample_rasters_rt_metadata_georectification_update'
BEFORE UPDATE OF georectification ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''sample_rasters_rt_metadata'' violates constraint: georectification must be -1, 0, 1 or 2')
WHERE (NOT (NEW.georectification IN (-1, 0, 1, 2)));
END

CREATE TRIGGER 'sample_rasters_rt_metadata_compr_qual_factor_insert' 
BEFORE INSERT ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''sample_rasters_rt_metadata'' violates constraint: compr_qual_factor < -1, must -1 or be between 1 and 100')
WHERE NEW.compr_qual_factor < -1;
SELECT RAISE(ROLLBACK, 'insert on table ''sample_rasters_rt_metadata'' violates constraint: compr_qual_factor = 0, must -1 or be between 1 and 100')
WHERE NEW.compr_qual_factor = 0;
SELECT RAISE(ROLLBACK, 'insert on table ''sample_rasters_rt_metadata'' violates constraint: compr_qual_factor > 100, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor > 100;
END

CREATE TRIGGER 'sample_rasters_rt_metadata_compr_qual_factor_update' 
BEFORE UPDATE OF compr_qual_factor ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''sample_rasters_rt_metadata'' violates constraint: compr_qual_factor < -1, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor < -1;
SELECT RAISE(ROLLBACK, 'update on table ''sample_rasters_rt_metadata'' violates constraint: compr_qual_factor = 0, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor = 0;
SELECT RAISE(ROLLBACK, 'update on table ''sample_rasters_rt_metadata'' violates constraint: compr_qual_factor > 100, must be -1 or between 1 and 100')
WHERE NEW.compr_qual_factor > 100;
END

CREATE TRIGGER 'sample_rasters_rt_metadata_row_id_value_insert' 
BEFORE INSERT ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table sample_rasters_rt_metadata violates constraint: row_id_value must exist in sample_rasters table')
WHERE NOT EXISTS (SELECT rowid
   FROM 'sample_rasters' WHERE rowid = NEW.row_id_value);
END

CREATE TRIGGER 'sample_rasters_rt_metadata_row_id_value_update' 
BEFORE UPDATE OF 'row_id_value' ON 'sample_rasters_rt_metadata'
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table sample_rasters_rt_metadata violates constraint: row_id_value must exist in sample_rasters table')
WHERE NOT EXISTS (SELECT rowid
   FROM 'sample_rasters' WHERE rowid = NEW.row_id_value);
END
```

**Table 6.3** - EXAMPLE: `{RasterLayerName}_rt_metadata` Insert Statement

```SQL
INSERT INTO sample_matrix_tiles_rt_metadata VALUES (
1,
"tile_data",
1,
-77.0,
38.0,
-75.0,
40.0,
100,
)
```
