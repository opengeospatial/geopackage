# 3 Registered Extensions

The optional registered extension capabilities specified in this clause depend on required capabilities specified in clause 1 and optional capabilities specified in clause 2. Any optional capability in this class that is implemented SHALL be registered using the Extension Mechanism defined in clause 2.6, as specified by the sub clauses below for extension name and extension row for the optional capability. 

> **Req 66:** Any table in a GeoPackage file subject to a registered extension with an `author_name` other than “gpkg” SHALL NOT be described by a `gpkg_contents` table row with a `data_type` value of “feature” or “tiles”. 

Such tables do not count[^1] in the determination of GeoPackage file validity per clause 2 Req 13: but otherwise MAY differ from “features” and “tiles” tables only with respect to non-gpkg registered extensions that enable implementers to meet requirements not addressed in the current version of this specification, and may be included in a valid GeoPackage.

## 3.1. Features
#### 3.1.1. Geometry Encoding
##### 3.1.1.1. Data

The optional registered extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements the requirements of clause 2.1 and clause 2.6.1.1 on which they depend.

##### 3.1.1.1.1. BLOB Format

A GeoPackage file CAN store geometries using BLOB formats other than the GeoPackageBinary format specified in clause 2.1.3.1.1. However,  tables with geometry column data encoded in such extension formats are not considered to be GeoPackage feature tables for purposes of determining GeoPackage file validity.

##### 3.1.1.1.2. BLOB format - Extensions Name

> **Req 67:** An extension name in the form <author\_name>\_geometry encoding SHALL be defined for an author name other than “gpkg” for each geometry BLOB format other than GeoPackageBinary used in a GeoPackage file.

##### 3.1.1.1.3. BLOB format - Extensions Row

> **Req 68:** A GeoPackage file that contains geometry column BLOB values encoded in an extension format SHALL contain a `gpkg_extensions` table that contains row records with `table_name` and `column_name` values from the `gpkg_geometry_columns` table row records that identify extension format uses, and with `extension_name` column values constructed per clause 3.1.1.1.2.

#### 3.1.2. Geometry Types
##### 3.1.2.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements the requirements of clause 2.1 and clause 2.6.1.1 on which they depend, as specified in Annex A.

##### 3.1.2.1.1. Extension Types

> **Req 69:** A GeoPackage file MAY store feature table geometries with the extended non-linear geometry types (CircularString, CompoundCurve, CurvePolygon, MultiCurve, MultiSurface, Curve, Surface) in Annex G. If it does so, they SHALL be encoded in the GeoPackageBinary geometry format.

##### 3.1.2.1.2. Extensions Types - Extensions Name

> **Req 70:** An extension name to specify a feature geometry extension type SHALL be defined for the “gpkg” author name using the “gpkg\_geom\_<gname>” template where <gname> is the name of the extension geometry type from Annex G used in a GeoPackage file.

##### 3.1.2.1.3. Extensions Types - Extensions Row

> **Req 71:** A GeoPackage file that contains a `gpkg_geometry_columns` table or updateable view with row records that specify extension `geometry_type` column values SHALL contain a `gpkg_extensions` table that contains row records with `table_name` and `column_name` values from the `geometry_columns` row records that identify extension type uses, and `extension_name` column values for each of those geometry types constructed per clause 3.1.2.1.2.

#### 3.1.3. Spatial Indexes
##### 3.1.3.1. Data

The optional registered extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements requirements of clause 2.1 and clause 2.6 on which they depend.

##### 3.1.3.1.1. Spatial Indexes Implementation

Spatial indexes provide a significant performance advantage for searches with basic envelope spatial criteria that return subsets of the rows in a feature table with a non-trivial number (thousands or more) of rows.[^2] 

Spatial indexes are an optional GeoPackage extension with the following runtime requirements
 * The SQLite RTree extension SHALL be available and loaded per clause 2.6.1.2.1.
 * SQLite trigger support SHALL be present per clause 2.6.1.2.2.
 * The ST\_MinX, ST\_MaxX, ST\_MinY, ST\_MaxY SQL functions specified in Annex D SHALL be available.

> **Req 72:** A GeoPackage file SHALL implement spatial indexes on feature table geometry columns as specified in clause 3.1.3.1.1 using the SQLite Virtual Table RTrees and triggers specified in Annex E.

##### 3.1.3.1.2. Spatial Indexes - Extensions Name

> **Req 73:** The “gpkg\_rtree\_index” extension name SHALL be used as a `gpkg_extension` table extension name column value to specify implementation of spatial indexes on a geometry column.

##### 3.1.3.1.3. Spatial Indexes - Extensions Row

> **Req 74:** A GeoPackage file that implements spatial indexes SHALL have a `gpkg_extensions` table that contains a row for each spatially indexed column with `extension_name` “gpkg\_rtree\_index”, the `table_name` of the table with a spatially indexed column, and the `column_name` of the spatially indexed column.

#### 3.1.4. Geometry Type Triggers
##### 3.1.4.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements requirements of clause 2.1 and clause 2.6 on which they depend.

##### 3.1.4.1.1. Geometry Type Triggers – Implementation

> **Req 75:** A GeoPackage file SHALL include the SQL insert and update triggers specified in clause 3.1.4.1.1 and 17 on every feature table geometry column to enforce the geometry type values specified for those columns in the `gpkg_geometry_columns` table.

*Table 17: Geometry Type Trigger Definition SQL Template*

```SQL
CREATE TRIGGER fgti_<t>_<c> BEFORE INSERT ON '<t>'
FOR EACH ROW 
BEGIN
  SELECT RAISE (ROLLBACK, 'insert on <t> violates constraint: ST_GeometryType(<c>) is not assignable from gpkg_geometry_columns.geometry_type_name value')
  WHERE (SELECT geometry_type_name FROM gpkg_geometry_columns
         WHERE Lower(table_name) = Lower('<t>') 
	      AND   Lower(column_name) = Lower('<c>') 
	      AND   gpkg_IsAssignable(geometry_type_name,
	                              ST_GeometryType(NEW.<c>)) = 0;

END

CREATE TRIGGER fgtu_<t>_<c> BEFORE UPDATE OF '<c>' ON '<t>'
FOR EACH ROW 
BEGIN
SELECT RAISE (ROLLBACK, 
'update of <c> on <t> violates constraint: ST_GeometryType(<c>) is not assignable from gpkg_geometry_columns.geometry_type_name value')
WHERE (SELECT geometry_type_name FROM gpkg_geometry_columns
       WHERE Lower(table_name) = Lower('<t>') 
	    AND   Lower(column_name) = Lower('<c>') 
	    AND   gpkg_IsAssignable(geometry_type_name,
	                            ST_GeometryType(NEW.<c>)) = 0;
END
```

where \<t\> and \<c\> are replaced with the names of the feature table and geometry column being inserted or updated.
The triggers to enforce `gpkg_geometry_columns` `geometry_type_name` constraints on feature table geometries use Minimal Runtime SQL Functions specified in Annex D.

##### 3.1.4.1.2. Geometry Type Triggers – Extensions Name

> **Req 76:** The “gpkg_geometry_type_trigger” extension name SHALL be used as a `geopackage_extension` table extension name column value to specify implementation of geometry type triggers.

##### 3.1.4.1.3. Geometry Type Triggers – Extensions Row

> **Req 77:**  A GeoPackage file that implements geometry type triggers on feature table geometry columns SHALL contain a `gpkg_extensions` table that contains a row for each such geometry column with `extension_name` “gpkg\_geometry\_type\_trigger”, `table_name` of the feature table with a geometry column, and `column_name` of the geometry column.

#### 3.1.5. SRS_ID Triggers
##### 3.1.5.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements requirements of clause 2.1 and clause 2.6 on which they depend.

##### 3.1.5.1.1. SRS_ID Triggers – Implementation

> **Req 78:** A GeoPackage file SHALL include the SQL insert and update triggers specified in clause 3.1.5.1.1 and 18 on every feature table geometry column to enforce the `srs_id` values specified for those columns in the `gpkg_geometry_columns` table.

Table  SRS_ID Trigger Definition SQL Templates

```SQL
CREATE TRIGGER fgsi_<t> _<c> BEFORE INSERT ON '<t>'
FOR EACH ROW 
BEGIN
  SELECT RAISE (ROLLBACK, 'insert on <t>violates constraint: ST_SRID(<c>) does not match gpkg_geometry_columns.srs_id value')
  WHERE (SELECT srs_id FROM gpkg_geometry_columns
       WHERE Lower(table_name) = Lower('<t>') 
	   AND   Lower(column_name) = Lower('<c>') 
	   AND   ST_SRID(NEW.'<c>') <> srs_id) ;
END

CREATE TRIGGER fgsu_<t>_<c> BEFORE UPDATE OF '<c>' ON '<t>'
FOR EACH ROW 
BEGIN
SELECT RAISE (ROLLBACK, 
'update of <c> on <t> violates constraint: ST_SRID(<c>) does not match gpkg_geometry_columns.srs_id value')
WHERE (SELECT srs_id FROM gpkg_geometry_columns
       WHERE Lower(table_name) = Lower('<t>') 
	   AND   Lower(column_name) = Lower('<c>') 
	   AND   ST_SRID(NEW.'<c>') <> srs_id);
END
```

where \<t\> and \<c\> are replaced with the names of the feature table and geometry column being inserted or updated.
The triggers to enforce `geometry_columns` `srs_id` constraints on feature table geometries use Minimal Runtime SQL Functions specified in Annex F

##### 3.1.5.1.2. SRS_ID Triggers – Extensions Name

> **Req 79:** The “gpkg\_srs\_id\_trigger” extension name SHALL be used as a `geopackage_extension` table extension name column value to specify implementation of `srs_id` triggers.

##### 3.1.5.1.3. SRS_ID Triggers – Extensions Row

> **Req 80:** A GeoPackage file that implements `srs_id` triggers on feature table geometry columns SHALL contain a `gpkg_extensions` table that contains a row for each geometry column with `extension_name` “gpkg\_srs\_id\_trigger”, `table_name` of the feature table with a geometry column, and `column_name` of the geometry column.

## 3.2. Tiles
#### 3.2.1. Zoom Levels
##### 3.2.1.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements the requirements of clause 2.2 and clause 2.6.1.1 on which they depend.

##### 3.2.1.1.1. Zoom Other Intervals

As a registered extension, a GeoPackage file MAY contain tile matrix set user data tables with pixel sizes that vary by irregular intervals or by regular intervals other than powers of two (the default) between adjacent zoom levels, as described in the `gpkg_tile_matrix_metadata` table. 

##### 3.2.1.1.2. Zoom Other – Extensions Name

> **Req 81:** The “gpkg\_zoom\_other” extension name SHALL be used as a `gpkg_extension` table extension name column value to specify implementation of other zoom intervals on a tile matrix set user data table.

##### 3.2.1.1.3. Zoom Other – Extensions Row

> **Req 82:** A GeoPackage file that implements other zoom intervals SHALL have a `gpkg_extensions` table that contains a row for each tile matrix set user data table with other zoom intervals with `extension_name` “gpkg\_zoom\_other”, the `table_name` of the table with other zoom intervals, and the “tile\_data” `column_name`.

#### 3.2.2. Tile Encoding WEBP
##### 3.2.2.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements the requirements of clause  2.2 and clause 2.6.1.1 on which they depend.

##### 3.2.2.2. WEBP MIME Type

As a registered extension, a GeoPackage file that contains a tile matrix user data table that contains tile data MAY store `tile_data` in MIME type image/x-webp[26].

##### 3.2.2.2.1. WEBP -- Extensions Name

> **Req 83:** The “gpkg\_webp” extension name SHALL be used as a `geopackage_extension` table extension name column value to specify storage of raster images in WEBP format.

##### 3.2.2.2.2. WEBP -- Extensions Row

> **Req 84:** A GeoPackage file that contains tile matrix user data tables with `tile_data` columns that contain raster images in WEBP format SHALL contain a `gpkg_extensions` table that contains row records with `table_name` values for each such table, “tile\_data” `column_name` values and `extension_name` column values of “gpkg\_webp”.

#### 3.2.3. Tiles Encoding TIFF
##### 3.2.3.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements the requirements of clause 2.2 and clause 2.6.1.1 on which they depend.

##### 3.2.3.1.1. TIFF MIME Type

As a registered extension, a GeoPackage file that contains a tile matrix user data table that contains tile data MAY store tile_data in MIME type image/tiff [27] for GeoTIFF images [28][29] that meet the requirements of the NGA Implementation Profile [31] for coordinate transformation case 3 where the position and scale of the data is known exactly, and no rotation of the image is required.

##### 3.2.3.1.2. TIFF -- Extensions Name 

> **Req 85:** The “gpkg\_tiff” extension name SHALL be used as a `geopackage_extension` table extension name column value to specify storage of raster images in TIFF format.

##### 3.2.3.1.3. Extensions Row

> **Req 86:** A GeoPackage file that contains tile matrix user data tables with `tile_data` columns that contain raster images in TIFF format per SHALL contain a `gpkg_extensions` table that contains row records with `table_name` values for each such table, “tile\_data” `column_name` values and `extension_name` column values of “gpkg\_tiff”.

#### 3.2.4. Tile Encoding NITF
##### 3.2.4.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements the requirements of clause 2.2 and clause 2.6.1.1 on which they depend.

##### 3.2.4.1.1. NITF MIME Type

As a registered extension, a GeoPackage file that contains a tile matrix user data table that contains tile data MAY store `tile_data` in MIME type application/vnd.NITF[46] for National Imagery Transmission Format images.

##### 3.2.4.1.2. NITF -- Extensions Name

> **Req 87:** The “gpkg\_nitf” extension name SHALL be used as a `geopackage_extension` table extension name column value to specify storage of raster images in NITF format.

##### 3.2.4.1.3. NITF -- Extensions Row 

> **Req 88:** A GeoPackage file that contains tile matrix user data tables with `tile_data` columns that contain raster images in NITF format SHALL contain a `gpkg_extensions` table that contains row records with `table_name` values for each such table, “tile\_data” `column_name` values and `extension_name` column values of “gpkg\_nitf”.

#### 3.2.5. Tile Encoding Other
##### 3.2.5.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements the requirements of clause 2.2 and clause 2.6.1.1 on which they depend.

##### 3.2.5.1.1. Other MIME Type

As a registered extension, a GeoPackage file that contains a tile matrix user data table that contains tile data MAY store `tile_data` in other MIME types. However, a table with such data is not considered to be a “tiles” table for purposes of determining GeoPackage file validity.

##### 3.2.5.1.2. Other Extensions Name

> **Req 89:** An extension name in the form <author\_name>\_<other>\_mime\_type SHALL be defined for an author name other than “gpkg” for each other MIME image format used for `tile_data` columns in tile matrix set user data tables, where <other> is replaced by the other MIME type abbreviation in uppercase

##### 3.2.5.1.3. Other Extensions Row

> **Req 90:** A GeoPackage file that contains tile matrix user data tables with `tile_data` columns that contain raster images in a MIME type format other than those defined in this specification SHALL contain a `gpkg_extensions` table that contains row records with `table_name` values for each such table, “tile\_data” `column_name` values and `extension_name` column values of the other format extension name defined per clause 3.2.5.1.2.

## 3.3. Any Tables
#### 3.3.1. Other Trigger
##### 3.3.1.1. Data

The optional extension capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file that implements requirements of clause 2.1 and/or 2.2 and clause 2.6 on which they depend.

##### 3.3.1.1.1. Other Trigger Implementation

As a registered extension, GeoPackage files MAY contain other triggers that require support from GeoPackage SQLite Extension functions other than those provided by SQLite or the GeoPackage Minimal Runtime SQL Functions to enforce data integrity or application business rule constraints. [^3]

##### 3.3.1.1.2. Other Trigger – Extensions Name

> **Req 91:** An extension name in the form <author><extension> for an author name other than “gpkg” SHALL be defined as a `geopackage_extension` table extension name column value to specify triggers in a GeoPackage file that use SQL functions other than those provided by SQLite or the GeoPackage Minimal Runtime SQL Functions.

##### 3.3.1.1.3. Other Trigger – Extensions Row

> **Req 92:** A GeoPackage file that implements triggers that use SQL functions other than those provided by SQLite or the GeoPackage Minimal Runtime SQL Functions SHALL have a `gpkg_extensions` table that contains row records with `table_name` values for each such table, `column_name` values for each such column and `extension_name` column values of the other trigger extension name defined per clause 3.3.1.1.2.

[^1]: They MAY be contained in a valid GeoPackage file.

[^2]: If an application process will make many updates, it is often faster to drop the indexes, do the updates, and then recreate the indexes.

[^3]: Other triggers that rely only on SQLite and Minimal Runtime SQL functions do not need to be registered as an extension.
