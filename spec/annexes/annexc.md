Table Definition SQL (Normative)
==============

gpkg\_spatial\_ref\_sys
--------------------

### gpkg\_spatial\_ref\_sys Table Definition SQL

    CREATE TABLE gpkg_spatial_ref_sys (
      srs_name TEXT NOT NULL,
      srs_id INTEGER NOT NULL PRIMARY KEY,
      organization TEXT NOT NULL,
      organization_coordsys_id INTEGER NOT NULL,
      definition TEXT NOT NULL,
      description TEXT
    )

### SQL/MM View of gpkg\_spatial\_ref\_sys Definition SQL

    CREATE VIEW st_spatial_ref_sys AS SELECT
      srs_name,
      srs_id,
      organization,
      organization_coordsys_id,
      definition,
      description
    FROM gpkg_spatial_ref_sys;

### SF/SQL View of gpkg\_spatial\_ref\_sys Definition SQL

    CREATE VIEW spatial_ref_sys AS SELECT
      srs_id AS srid,
      organization AS auth_name,
      organization_coordsys_id AS auth_srid,
      definition AS srtext
      FROM gpkg_spatial_ref_sys;


gpkg_contents
-------------

### gpkg_contents Table Definition SQL

    CREATE TABLE gpkg_contents (
      table_name TEXT NOT NULL PRIMARY KEY,
      data_type TEXT NOT NULL,
      identifier TEXT UNIQUE,
      description TEXT DEFAULT '',
      last_change TEXT NOT NULL DEFAULT
        (strftime('%Y-%m-%dT%H:%M:%fZ',CURRENT_TIMESTAMP)),
      min_x DOUBLE,
      min_y DOUBLE,
      max_x DOUBLE,
      max_y DOUBLE,
      srs_id INTEGER,
      CONSTRAINT fk_gc_r_srs_id FOREIGN KEY (srs_id) REFERENCES
        gpkg_spatial_ref_sys(srs_id))

gpkg_extension
--------------

### gpkg_extensions Table Definition SQL

    CREATE TABLE gpkg_extensions (
      table_name TEXT,
      column_name TEXT,
      extension_name TEXT NOT NULL,
      CONSTRAINT ge_tce UNIQUE
        (table_name, column_name, extension_name))

gpkg\_geometry\_columns
---------------------

### gpkg\_geometry\_columns Table Definition SQL

    CREATE TABLE gpkg_geometry_columns (
      table_name TEXT NOT NULL,
      column_name TEXT NOT NULL,
      geometry_type TEXT NOT NULL,
      srs_id INTEGER NOT NULL,
      z INTEGER NOT NULL,
      m INTEGER NOT NULL,
      CONSTRAINT pk_geom_cols PRIMARY KEY (table_name, column_name),
      CONSTRAINT fk_gc_tn FOREIGN KEY (table_name)
                            REFERENCES gpkg_contents(table_name),
      CONSTRAINT fk_gc_srs FOREIGN KEY (srs_id)
                            REFERENCES gpkg_spatial_ref_sys (srs_id))



### SQL/MM View of gpkg\_geometry\_columns Definition SQL

    CREATE VIEW st_geometry_columns AS SELECT
      table_name,
      column_name,
      "ST_" || geometry_type_name,
      g.srs_id,
      srs_name
    FROM gpkg_geometry_columns as g JOIN gpkg_spatial_ref_sys AS s
    WHERE g.srs_id = s.srs_id;

### SF/SQL VIEW of gpkg\_geometry\_columns Definition SQL

    CREATE VIEW geometry_columns AS SELECT
      table_name AS f_table_name,
      column_name AS f_geometry_column,
      code4name(geometry_type_name) AS geometry_type,
      2 + (CASE z WHEN 1 THEN 1 WHEN 2 THEN 1 ELSE 0 END)
        + (CASE m WHEN 1 THEN 1 WHEN 2 THEN 1 ELSE 0 END)
        AS coord_dimension,
      srs_id AS srid
    FROM gpkg_geometry_columns;

Note: Implementer must provide code4name(geometry\_type\_name) SQL function

sample\_feature\_table (Informative)
----------------------------------

### sample\_feature\_table Table Definition SQL

    CREATE TABLE sample_feature_table (
      id INTEGER AUTOINCREMENT PRIMARY KEY,
      geometry_one BLOB NOT NULL,
      text_attribute TEXT NOT NULL,
      real_attribute REAL NOT NULL,
      numeric_attribute NUMERIC NOT NULL,
      raster_or_photo BLOB NOT NULL
    )

gpkg\_tile\_matrix\_metadata
-------------------------

### gpkg\_tile\_matrix\_metadata Table Creation SQL

    CREATE TABLE gpkg_tile_matrix_metadata (
      table_name TEXT NOT NULL,
      zoom_level INTEGER NOT NULL,
      matrix_width INTEGER NOT NULL,
      matrix_height INTEGER NOT NULL,
      tile_width INTEGER NOT NULL,
      tile_height INTEGER NOT NULL,
      pixel_x_size DOUBLE NOT NULL,
    pixel_y_size DOUBLE NOT NULL,
    CONSTRAINT pk_ttm PRIMARY KEY (table_name, zoom_level)
      ON CONFLICT ROLLBACK,
    CONSTRAINT fk_tmm_table_name FOREIGN KEY (table_name)
      REFERENCES gpkg_contents(table_name))



### EXAMPLE: gpkg\_tile\_matrix_metadata Insert Statement

    INSERT INTO gpkg_tile_matrix_metadata VALUES (
    "sample_matrix_tiles",
    1,
    1,
    512,
    512,
    2.0,
    2.0);


sample\_matrix\_tiles (Informative)
---------------------------------

### EXAMPLE: tiles table Create Table SQL

    CREATE TABLE sample_matrix_tiles (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      zoom_level INTEGER NOT NULL,
      tile_column INTEGER NOT NULL,
      tile_row INTEGER NOT NULL,
      tile_data BLOB NOT NULL),
    UNIQUE (zoom_level, tile_column, tile_row))

### EXAMPLE: tiles table Insert Statement

    INSERT INTO sample_matrix_tiles VALUES (
    1,
    1,
    1,
    1,
    "BLOB VALUE")

gpkg\_data\_columns
-----------------

### gpkg\_data\_columns Table Definition SQL

    CREATE TABLE gpkg_data_columns (
      table_name TEXT NOT NULL,
      column_name TEXT NOT NULL,
      name TEXT,
      title TEXT,
      description TEXT,
      mime_type TEXT,
      CONSTRAINT pk_gdc PRIMARY KEY (table_name, column_name)
      ON CONFLICT ROLLBACK,
      CONSTRAINT fk_gdc_tn FOREIGN KEY (table_name)
               REFERENCES gpkg_contents(table_name))

metadata
--------

### gpkg_metadata Table Definition SQL

    CREATE TABLE gpkg_metadata (
      id INTEGER CONSTRAINT m_pk PRIMARY KEY ASC
        ON CONFLICT ROLLBACK AUTOINCREMENT NOT NULL UNIQUE,
      md_scope TEXT NOT NULL DEFAULT 'dataset',
      metadata_standard_URI TEXT NOT NULL DEFAULT
    'http://schemas.opengis.net/iso/19139/',
      mime_type TEXT NOT NULL DEFAULT ‘text/xml’,
      metadata TEXT NOT NULL DEFAULT (‘’)
    )

metadata_reference
------------------

### gpkg\_metadata\_reference Table Definition SQL

    CREATE TABLE gpkg_metadata_reference (
      reference_scope TEXT NOT NULL,
      table_name TEXT,
      column_name TEXT,
      row_id_value INTEGER,
      timestamp TEXT NOT NULL DEFAULT (strftime('%Y-%m-
    %dT%H:%M:%fZ',CURRENT_TIMESTAMP)),
      md_file_id INTEGER NOT NULL,
      md_parent_id INTEGER,
      CONSTRAINT crmr_mfi_fk FOREIGN KEY (md_file_id) REFERENCES
    gpkg_metadata(id),
      CONSTRAINT crmr_mpi_fk FOREIGN KEY (md_parent_id) REFERENCES
    gpkg_metadata(id)
    )

### Example: gpkg\_metadata\_reference SQL insert statement

    INSERT INTO gpkg_metadata_reference VALUES (
    'table','sample_rasters',NULL, NULL, '2012-08-
    17T14:49:32.932Z', 98, 99)


