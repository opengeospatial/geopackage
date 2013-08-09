# 2 Options
The optional capabilities specified in this clause depend on the required capabilities specified in the [Base section](1_base.md).

> **Req 13:** A Valid GeoPackage SHALL contain features per clause 2.1 and/or tiles per clause 2.2 and row(s) in the `gpkg_contents` table with `data_type` column values of “features” and/or “tiles” describing the user data tables.

## 2.1. Features

The optional capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file.

#### 2.1.1. Simple Features SQL Introduction

Vector feature data represents geolocated entities including conceptual ones such as districts, real
world objects such as roads and rivers, and observations thereof. International specifications
][15][16] have standardized practices for the storage, access and use of vector geospatial features
and geometries via SQL in relational databases.  The first component of the SQL schema for vector
features in a GeoPackage is the `gpkg_spatial_ref_sys` table defined in clause 1.1.2 above. Other
components are defined below.

In a GeoPackage file, “simple” features are geolocated using a linear geometry subset of the SQL/MM (ISO 13249-3) [16] geometry model shown in figure 2 below. 

*Figure 2 – Core Geometry Model*

![core geometry model](images/core-geometry-model.png)

The instantiable (not abstract) geometry types defined in this Standard are restricted to 0, 1 and
2-dimensional geometric objects that exist in 2, 3 or 4-dimensional coordinate space (R2, R3 or R4).
Geometry values in R2 have points with coordinate values for x and y. Geometry values in R3 have
points with coordinate values for x, y and z or for x, y and m. Geometry values in R4 have points
with coordinate values for x, y, z and m. The interpretation of the coordinates is subject to the
coordinate reference systems associated to the point. All coordinates within a geometry object
should be in the same coordinate reference systems.  Geometries may include z coordinate values. The
z coordinate value traditionally represents the third dimension (i.e. 3D). In a Geographic
Information System (GIS) this may be height above or below sea level. For example: A map might have
a point identifying the position of a mountain peak by its location on the earth, with the x and y
coordinate values, and the height of the mountain, with the z coordinate value.

Geometries may include m coordinate values. The m coordinate value allows the application
environment to associate some measure with the point values. For example: A stream network may be
modeled as multilinestring value with the m coordinate values measuring the distance from the mouth
of stream.

All geometry types described in this standard are defined so that instances of Geometry are
topologically closed, i.e. all represented geometries include their boundary as point sets. This
does not affect their representation, and open version of the same classes may be used in other
circumstances, such as topological representations.

A brief description of each geometry type is provided below. A more detailed description can be found in ISO 13249-3[16]. 

 * Geometry: the root of the geometry type hierarchy. 
 * Point: a single location in space. Each point has an X and Y coordinate. A point may optionally also have a Z and/or an M value.
 * Curve: the base type for all 1-dimensional geometry types. A 1-dimensional geometry is a geometry that has a length, but no area. A curve is considered simple if it does not intersect itself (except at the start and end point). A curve is considered closed its start and end point are coincident. A simple, closed curve is called a ring. 
 * LineString: A Curve that connects two or points in space. 
 * Surface: the base type for all 2-dimensional geometry types. A 2-dimensional geometry is a geometry that has an area. 
 * CurvePolygon: A planar surface defined by an exterior ring and zero or more interior ring. Each ring is defined by a Curve instance. 
 * Polygon: A restricted form of CurvePolygon where each ring is defined as a simple, closed LineString. 
 * GeometryCollection: A collection of zero or more Geometry instances. 
 * MultiSurface: A restricted form of GeometryCollection where each Geometry in the collection must be of type Surface. 
 * MultiPolygon: A restricted form of MultiSurface where each Surface in the collection must be of type Polygon. 
 * MultiCurve: A restricted form of GeometryCollection where each Geometry in the collection must be of type Curve. 
 * MultiLineString: A restricted form of MultiCurve where each Curve in the collection must be of type LineString. 
 * MultiPoint: A restricted form of GeometryCollection where each Geometry in the collection must be of type Point. 

#### 2.1.2. Contents
##### 2.1.2.1. Data
##### 2.1.2.1.1. Contents Table – Features Row

> **Req 14:** `gpkg_contents` SHALL contain a row with a `data_type` column value of “features” for each vector features user data table.

#### 2.1.3. Geometry Encoding
##### 2.1.3.1. Data
##### 2.1.3.1.1. BLOB Format

> **Req 15:** A GeoPackage file SHALL store feature table geometries with or without optional elevation (Z) and/or measure (M) values in SQL BLOBs using the GeoPackageBinary format specified in 4 and clause 2.1.3.1.1. 

*Table 4 GeoPackage SQL Geometry Binary Format*

```
GeoPackageBinary {
  byte[2] magic = 0x4750; // 'GP'
  byte version;           // 8-bit unsigned integer, 0 = version 1
  byte flags;             // see flags layout below
  int32 srs_id;
  double[] envelope;      // see flags envelope contents indicator code below
  WKBGeometry geometry;   // per  ISO 13249-3[16] clause 5.1.46 [^1]
}
```

**flags layout:**

| | | | | | | | | |
|---------|---|---|---|---|---|---|---|---|
| **bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| **use** | R | R | R | Y | E | E | E | B |

**use:**

R: reserved for future use; set to 0

Y: empty geometry flag
 * 0: non-empty geometry

 * 1: empty geometry
 
**E: envelope contents indicator code** (3-bit unsigned integer)

| code value | description | envelope length (bytes) |
|------------|-------------|-------------------------|
| 0 | no envelope (space saving slower indexing option) | 0 | 
| 1 | envelope is [minx, maxx, miny, maxy] | 32 |
| 2 | envelope is [minx, maxx, miny, maxy, minz, maxz] | 48 |
| 3 | envelope is [minx, maxx, miny, maxy, minm, maxm] | 48 |
| 4 | envelope is [minx, maxx, miny, maxy, minz, maxz, minm, maxm] | 64 |
| 5-7 | invalid | unknown |

**B: byte order for header values** (1-bit Boolean)
     0 = Big Endian   (most significant byte first)
     1 = Little Endian (least significant byte first)

**Well-Known Binary as defined in ISO 13249-3 [16] does not provide a standardized encoding for an empty point set (i.e., 'Point Empty' in Well-Known Text). In GeoPackage files these points SHALL be encoded as a Point where each coordinate value is set to an IEEE-754 quiet NaN value.  GeoPackage files SHALL use big endian 0x7ff8000000000000 or little endian 0x000000000000f87f as the binary encoding of the NaN values.**

##### 2.1.3.2. API
##### 2.1.3.2.1. Minimal Runtime SQL Functions

In contrast to functions in application code or a runtime library, triggers are part of the SQLite
database file. When an application writes to a GeoPackage file that it did not create itself then
there is the possibility that it will invoke a trigger that calls a function that the application’s
runtime library does not provide.   To avoid this interoperability problem, a small set of functions
on the GeoPackageBinary geometry specified in clause 2.1.3.1.1 are defined in Annex D. Every
implementation can be sure that triggers that only use these functions in addition to those provided
by SQLite will work as intended across implementations.[^2] [^3]

> **Req 16:** A GeoPackage SQLite Extension MAY provide SQL function support for triggers in GeoPackage file. One that does so SHALL provide the minimal runtime SQL functions listed in Annex D Table 36.

#### 2.1.4. Geometry Types
##### 2.1.4.1. Data
##### 2.1.4.1.1. Core Types

> **Req 17:** A GeoPackage file SHALL store feature table geometries with the basic simple feature geometry types (Geometry, Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeomCollection) in Annex G Table 46 in the GeoPackageBinary geometry encoding format. 

#### 2.1.5. Geometry Columns
##### 2.1.5.1. Data
##### 2.1.5.1.1. Table Definition

> **Req 18:** A GeoPackage file with a `gpkg_contents` table row with a “features” `data_type` SHALL contain a `gpkg_geometry_columns` table or updateable view per clause 2.1.5.1.1, Table 5 and Table 24. 

The second component of the SQL schema for vector features in a GeoPackage is a
`gpkg_geometry_columns` table that identifies the geometry columns in tables that contain user data
representing features. This table or updateable view SHALL contain one row record for each geometry
column in each vector feature data table (clause 2.1.6) in a GeoPackage.

*Table 5: Geometry Columns Table or View Definition*

| Column Name | Type | Description | Key |
|-------------|------|-------------|-----|
| `table_name` | text | Name of the table containing the geometry column | PK, FK|
| `column_name` | text | Name of a column in the feature table that is a Geometry Column | PK|
| `geometry_type_name` | text | Name from 46 or 47 in Annex G | |
| `srs_id` | integer | Spatial Reference System ID: `gpkg_spatial_ref_sys.srs_id` | FK |
| `z` | integer | 0: z values prohibited;  1: z values mandatory;  2: z values optional | |
| `m` | integer | 0: m values prohibited; 1: m values mandatory; 2: m values optional | |

The FK on `gpkg_geometry_columns.srs_id` references the PK on `gpkg_spatial_ref_sys.srs_id` to ensure that geometry columns are only defined in feature tables for defined spatial reference systems.

The `gpkg_geometry_columns` table or view MAY include additional columns to meet the requirements of implementation software or other specifications.  Views of this table or view MAY be used to provide compatibility with the SQL/MM [16] (25) and OGC Simple Features SQL [14][15] (26) specifications.

See clause C.4 `gpkg_geometry_columns`.

##### 2.1.5.1.2. Table Data Values

> **Req 19:** Values of the `gpkg_geometry_columns` table `table_name` column SHALL reference values in the `gpkg_contents` `table_name` column.

> **Req 20:** The `column_name` column value in a `gpkg_geometry_columns` table row SHALL be the name of a column in the table specified by the `table_name` column value for that row.

> **Req 21:** The `geometry_type_name` value in a `gpkg_geometry_columns` table row SHALL be one of the geometry type names specified in Annex G.

> **Req 22:** The `srs_id` value in a `gpkg_geometry_columns` table row SHALL be an `srs_id` column value from the `gpkg_spatial_ref_sys` table.

> **Req 23:** The z value in a `gpkg_geometry_columns` table row SHALL be one of 0, 1, or 2.

> **Req 24:** The m value in a `gpkg_geometry_columns` table row SHALL be one of 0, 1, or 2.

#### 2.1.6. Vector Feature User Data Tables
##### 2.1.6.1. Data
##### 2.1.6.1.1. Table Definition

The third component of the SQL schema for vector features in a GeoPackage described in clause 2.1.1 above are tables that contain user data representing features. Feature attributes are columns in a feature table, including geometries.[^4] Features are rows in a feature table.[^5] 

> **Req 25:** A GeoPackage file MAY contain tables or updateable views containing vector features. Every such feature table or view in a GeoPackage file SHALL have a primary key defined on one integer column per table 6 and table 27.

The integer primary key of a feature table allows features to be linked to row level metadata records in the `gpkg_metadata` table by rowid values in the `gpkg_metadata_reference` table as described in clause 2.4.3 below.

Table 6: EXAMPLE : Sample Feature Table or View Definition

| Column Name | Type | Description | Null | Default | Key |
|-------------|------|-------------|------|---------|-----|
| `id` | integer | Autoincrement primary key | no | | PK |
| `geometry_one` | BLOB | GeoPackage Geometry | no | | |
| `text_attribute` | text | Text attribute of feature | no | | |
| `real_attribute` | real | Real attribute of feature | no | | |
| `numeric_attribute` | numeric | Numeric attribute of feature | no | | |
| `raster_or_photo` | BLOB | Photograph of the area | no | | |


See Annex C: Table Definition SQL clause  C.5 `sample_feature_table` 

##### 2.1.6.1.2. Table Data Values

A feature geometry is stored in a geometry column specified by the `geometry_column` value for the feature table in the `gpkg_geometry_columns` table defined in clause 2.1.5 above. The geometry type of a feature geometry column specified in the `gpkg_geometry_columns` table `geometry_type_name` column is a name from Annex G.

> **Req 26:** **A feature table SHALL have only one geometry column.**

> Feature data models from non-GeoPackage implementations that have multiple geometry columns per feature table MAY be transformed into GeoPackage? implementations with a separate feature table for each geometry type whose rows have matching integer primary key values that allow them to be joined in a view with the same column definitions as the non-GeoPackage feature data model with multiple geometry columns.[^6].

Geometry subtypes are assignable  as defined in Annex G and shown in part in Figure 2 – Core Geometry Model. For example, if the `geometry_type_name` value in the `gpkg_geometry_columns` table is for a geometry type like POINT that has no subtypes, then the feature table geometry column MAY only contain geometries of that type. If the geometry `type_name` value in the `gpkg_geometry_columns` table is for a geometry type like GEOMCOLLECTION that has subtypes, then the feature table geometry column MAY only contain geometries of that type or any of its direct or indirect subtypes. If the geometry `type_name` is GEOMETRY (the root of the geometry type hierarchy) then the feature table geometry column MAY contain geometries of any geometry type. 
The presence or absence of optional elevation (Z) and/or measure (M) values in a geometry does not change its type or assignability.

The spatial reference system type of a feature geometry column specified by a `gpkg_geometry_columns` table `srs_id` column value is a code from the `gpkg_spatial_ref_sys` table `srs_id` column.

> **Req 27:** Feature table geometry columns SHALL contain geometries with the `srs_id` specified for the column by the `gpkg_geometry_columns` table `srs_id` column value.

[^1]: OGC WKB simple feature geometry types specified in [13] are a subset of the ISO WKB geometry types specified in [16]

[^2]: Functions other than the minimal runtime SQL functions required by triggers in a GeoPackage file SHOULD be documented in the gpkg_extensions table and provided by a GeoPackage SQLite Extension.

[^3]: SQL functions on geometries in addition to those defined in this clause should conform to the SF/SQL [14][15] and SQL/MM [16] specifications cited in clause 2.1.1 above.

[^4]: A feature type MAY be defined to have 0..n geometry and/or raster attributes, so the corresponding feature table MAY contain from 0..n geometry and/or raster columns.

[^5]: A GeoPackage is not required to contain any feature data tables. Feature data tables in a GeoPackage MAY be empty

[^6] GeoPackage applications MAY use SQL triggers or tests in application code to meet Req 26
