## 2.6. Extension Mechanism

The GeoPackage extension mechanism is an optional capability that is a required dependency for the optional registered extension capabilities defined in clause 3.

#### 2.6.1. Extensions
##### 2.6.1.1. Data

The optional capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage file.

##### 2.6.1.1.1. Table Definition

> **Req 60:** A GeoPackage file MAY contain a table or updateable view named gpkg_extensions. If present this table SHALL be defined per clause 2.6.1.1.1, Table 13 and Table 23.

The `gpkg_extensions` table in a GeoPackage file registers extension capabilities required to make direct use of its contents. An application that access a GeoPackage file can query the `gpkg_extensions` table instead of the contents of all the user data tables to determine if it has the required capabilities, and to “fail fast” and return an error message if it does not.

*Table 13: GeoPackage Extensions Table or View Definition*

| Column Name | Col Type | Column Description | Null | Key |
|-------------|----------|--------------------|------|-----|
| `table_name` | text | Name of the table that requires the extension. When NULL, the extension is required for the entire GeoPackage. SHALL NOT be NULL when the column_name is not NULL. | yes | Unique |
| `column_name` | text | Name of the column that requires the extension. When NULL, the extension is required for the entire table. | yes | Unique |
| `extension_name` | text | The name of the extension that is required, in the form \<author\>\_\<extension name\>. | no  | Unique |

See Annex C: Table Definition SQL clause C.3 gpkg_extensions.

##### 2.6.1.1.2. Table Data Values

> **Req 61:** Values of the `gpkg_extensions` table `table_name` column SHALL reference values in the `gpkg_contents` `table_name` column or be NULL.  They SHALL NOT be NULL for rows where the `column_name` value is not NULL.

> **Req 62:** The `column_name` column value in a `gpkg_extensions` table row SHALL be the name of a column in the table specified by the `table_name` column value for that row, or be NULL.

> **Req 63:** Each `extension_name` column value in a `gpkg_extensions` table row SHALL be a unique value of the form \<author\>\_\<extension name\> where \<author\> indicates the person or organization that developed and maintains the extension. The valid character set for \<author\> SHALL be [a-zA-Z0-9]. The valid character set for \<extension name\> SHALL be [a-zA-Z0-9\_]. An `extension_name` for the “gpkg” author name SHALL be one of those listed in Table 14.

The author value “gpkg” is reserved for GeoPackage extensions that are developed and maintained by OGC. Requirements for extension names for the “gpkg” author name are defined in the clauses listed in 14 below. GeoPackage implementers use their own author names to register other extensions.1

*Table 14: Reserved GeoPackage Extensions*

| Extension Name | Defined in Clause | Description |
|----------------|-------------------|-------------|
| gpkg\_geom\_\<gname\> | 3.1.2.1.2 | \<gname\> is name of specific extension geometry type from Annex G 47
| gpkg\_zoom\_other | 3.2.1.1.1 | Tile matrix set user data table with zoom intervals other than powers of two between adjacent layers |
| gpkg\_webp | 3.2.2.2.1 | Raster images in image/webp format  |
| gpkg\_tiff | 3.2.3.1.2 | Raster images in image/tiff format  | 
| gpkg\_nitf | 3.2.4.1.2 | Raster images in application/vnd.NITF  |
| gpkg\_rtree\_index | 3.1.3.1.2 | Rtree spatial index implemented via SQLite Virtual Table and maintained via triggers that use all minimal runtime SQL functions except ST_SRID. |
| gpkg\_gtype\_trigger | 3.1.4.1.2 | Trigger to restrict GeoPackage feature table geometry column geometries to geometry types equal to or substitutable for the geometry type specified for the column in the `gpkg_geometry_columns` table `geometry_type_name` column.|
| gpkg\_srs\_id\_trigger | 3.1.5.1.2 | Trigger to restrict GeoPackage feature table geometry column geometries to the `srs_id` specified for the geometry column in the `gpkg_geometry_columns` table using the ST_SRID SQL function. |

##### 2.6.1.2. API

The optional capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any GeoPackage SQLite Extension.

###### 2.6.1.2.1. API GeoPackage SQLite Config

> **Req 64:** A GeoPackage SQLite Extension MAY provide SQL runtime functions or rtree support for a GeoPackage file. One that does so SHALL have the SQLite library compile and run time options specified in clause 2.6.1.2.1 Table 15

*Table 15: API GeoPackage SQLite Configuration*

| Setting | Option | Shall / Not (Value) | Discussion |
|---------|--------|---------------------|------------|
| compile | SQLITE\_OMIT\_LOAD\_EXTENSION | Not | The load_extension() function is required to implement the MinimalRuntimeSQLFunctions |
| compile | SQLITE\_OMIT\_VIRTUALTABLE | Not | Virtual tables are required to implement RTrees |
| compile | SQLITE\_ENABLE\_RTREE | Shall | Rtrees are used for GeoPackage Spatial Indexes. See SpatialIndexRequirements |
| compile | SQLITE\_RTREE\_INT\_ONLY | Not | Rtrees with floating point values are used for GeoPackage Spatial Indexes. |

##### 2.6.1.2.2. Safe GeoPackage SQLite Config

> **Req 65:** A GeoPackage SQLite Extension MAY provide primary/foreign key and trigger support for a GeoPackage file. One that does so SHALL have the SQLite library compile and run time options specified in clause 2.6.1.2.2 Table 16.

*Table 16: Safe GeoPackage SQLite Configuration*

| Setting | Option | Shall / Not (Value) | Discussion |
|---------|--------|---------------------|------------|
| compile | SQLITE\_DEFAULT\_FOREIGN\_KEYS | Shall (1) | Foreign key constraints are used to maintain GeoPackage relational integrity. |
| compile | SQLITE\_OMIT\_FOREIGN\_KEY | Not | Foreign key constraints are used to maintain GeoPackage relational integrity. |
| run | PRAGMA foreign\_keys | Not (OFF) | Foreign key constraints are used to maintain GeoPackage relational integrity. | 
| compile | SQLITE\_OMIT\_INTEGRITY\_CHECK | Not | This option omits support for the integrity_check pragma, which does an integrity check of the entire database. This pragma should be part of GeoPackage conformance validation. |
| compile | SQLITE\_OMIT\_SUBQUERY | Not | This option omits support for sub-selects and the IN() operator, both of which are used in GeoPackage triggers. |
| compile | SQLITE\_OMIT\_TRIGGER | Not| Defining this option omits support for TRIGGER objects. Neither the CREATE TRIGGER or DROP TRIGGER commands are available in this case, and attempting to execute either will result in a parse error. This option also disables enforcement of foreign key constraints, since the code that implements triggers and which is omitted by this option is also used to implement foreign key actions. Foreign keys and triggers are used by Safe GeoPackages. Triggers are used to maintain spatial indexes. |

