# 1 Base

The required capabilities specified in this clause serve as the base for
optional features and registered extensions capabilities specified in clauses 1
and 2.

## 1.1 Core

The mandatory core capabilities defined in sub clauses and requirement statements of this clause SHALL be implemented by every GeoPackage.

#### 1.1.1. SQLite Container

A self-contained, single-file, cross-platform, serverless, transactional, open source RDBMS
container is desired to simplify production, distribution and use of GeoPackages and guarantee the
integrity of the data they contain. “Self-contained” means that container software requires very
minimal support from external libraries or from the operating system. “Single-file” means that a
container not currently opened by any software application consists of a single file in a file
system supported by a computing platform operating system. “Cross-platform” means that a container
file MAY be created and loaded with data on one computing platform, and used and updated on another,
even if they use different operating systems, file systems, and byte order (endian) conventions.
“Serverless” means that the RDBMS container is implemented without any intermediary server process,
and accessed directly by application software. “Transactional” means that RDBMS transactions
guarantee that all changes to data in the container are Atomic, Consistent, Isolated, and Durable
(ACID) despite program crashes, operating system crashes, and power failures.

#### 1.1.1.1. Data
#### 1.1.1.1.1. File Format

> **Req 1:** The GeoPackage file format SHALL be a [SQLite](http://www.sqlite.org/) database [version 3 format file](http://sqlite.org/fileformat2.html), the first 16 bytes of which contain “SQLite format 3”[^1] in ASCII.[^2]

It is RECOMMENDED that data providers whose data is intended for use in multiple applications put
the value “GPKG” in the SQLite database header application id field. However, applications that put
application-specific data in a GeoPackage MAY put their own application acronym in the application
id field, so this is NOT a GeoPackage requirement.

The maximum size of a GeoPackage file is about 140TB. In practice a lower size limit MAY be imposed
by the filesystem to which the file is written. Many mobile devices require external memory cards to
be formatted using the FAT32 file system which imposes a maximum size limit of 4GB.

##### 1.1.1.1.2. File Extension Name

> **Req 2:** GeoPackage files SHALL have the file extension name “.gpkg”.

##### 1.1.1.1.3. Integrity Check

> **Req 3:** The SQLite PRAGMA integrity_check SQL command SHALL return “ok” for a GeoPackage file. 

#### 1.1.1.2. API
#### 1.1.1.2.1. Structured Query Language (SQL)

> **Req 4:** A GeoPackage SQLite Extension SHALL provide SQL access to GeoPackage file contents via [SQLite sqlite3](http://www.sqlite.org/download.html) software APIs.[^3]

#### 1.1.1.2.2. Every GPKG SQLite Configuration

The [SQLite](http://www.sqlite.org/download.html) library has many [compile
time](http://www.sqlite.org/compile.html) and [run time](http://www.sqlite.org/pragma.html) options
that MAY be used to configure SQLite for different uses. A GeoPackage application can use the
[compile options](http://www.sqlite.org/pragma.html#pragma_compile_options) and other SQLite pragmas
to get the effective compile and run time option settings and compare them to those required for a
particular GeoPackage.

> **Req 5:** Every GeoPackage SQLite Extension SHALL have the SQLite library compile and run time options specified in clause 1.1.1.2.2 Table 1.

*Table 1: Every GeoPackage SQLite Configuration*

|Setting | Option | Shall / Not | Discussion |
|---------|--------|------------|------------|
| compile | SQLITE\_OMIT\_AUTOINCREMENT | Not | A number of tables in GeoPackage are specified to have autoincrement columns. |
| compile | SQLITE\_OMIT\_DATETIME\_FUNCS | Not | `gpkg_contents` table `last_change` column requires timestamps |
| compile | SQLITE\_OMIT\_DEPRECATED | Shall | Omit [PRAGMA](http://www.sqlite.org/pragma.html#syntax)s marked “Do not use this pragma!” in SQLite documentation. |
| compile | SQLITE\_OMIT\_FLOATING\_POINT | Not | min/max x/y columns in `gpkg_contents` table are type REAL |
| compile | SQLITE\_OMIT\_PRAGMA | Not | GeoPackage configuration checks will require use of the [compile_options](http://www.sqlite.org/pragma.html#pragma_compile_options) pragma. |
| compile | SQLITE\_OMIT\_FLAG\_PRAGMAS | Not | GeoPackage conformance validation will require use of the [integrity_check](http://www.sqlite.org/pragma.html#pragma_integrity_check) pragma |
| compile | SQLITE\_OMIT\_VIEW | Not | GeoPackage tables MAY be implemented as updateable views. |

#### 1.1.2. Spatial Reference Systems
#### 1.1.2.1. Data
#### 1.1.2.1.1. Table Definition

> **Req 6:** A GeoPackage file SHALL include a `gpkg_spatial_ref_sys` table or updateable view per clause 1.1.2.1.1, table 2 and table 19.

A table or updateable view named `gpkg_spatial_ref_sys` is the first component of the standard SQL
schema for simple features described in clause 2.1.1 below. The coordinate reference system
definitions it contains are referenced by the GeoPackage `gpkg_contents` and `gpkg_geometry_columns`
tables to relate the vector and tile data in user tables to locations on the earth. The
`gpkg_spatial_ref_sys` table includes at a minimum the columns specified in SQL/MM (ISO 13249-3)
[16] and shown in 2 below containing data that defines spatial reference systems. This table or view
MAY include additional columns to meet the requirements of implementation software or other
specifications.  Views of this table or view MAY be used to provide compatibility with the [SQL/MM](http://www.iso.org/iso/home/store/catalogue_ics/catalogue_detail_ics.htm?csnumber=53698) (see table 20 in Annex C) and OGC [Simple Features SQL](http://portal.opengeospatial.org/files/?artifact_id=25354) (see table 21 in Annex C) specifications.

*Table 2: Spatial Ref Sys Table or View Definition*

| Column Name | Column Type | Column Description | Key |
|-------------|-------------|--------------------|-----|
| `srs_name` | text | Human readable name of this SRS | |
| `srs_id` | integer| Unique identifier for each Spatial Reference System within a GeoPackage file | PK |
| `organization` | text | Case-insensitive name of the defining organization e.g. EPSG or epsg | |
| `organization_coordsys_id` | integer |  Numeric ID of the Spatial Reference System assigned by the organization | |
| `definition` | text| Well-known Text Representation of the Spatial Reference System | |
| `description` | `text` | Human readable description of this SRS | |

See Annex C Table Definition SQL (Normative) C.1 `gpkg_spatial_ref_sys`.

#### 1.1.2.1.2. Table Data Values

> **Req 7:** The `gpkg_spatial_ref_sys` table or updateable view in a GeoPackage SHALL contain a
> record for organization [EPSG](http://www.epsg.org/Geodetic.html) or epsg and `organization_coordsys_id` 4326 (see the [registry](http://www.epsg-registry.org/) and search for '4326') for [WGS-84](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CCwQFjAA&url=http%3A%2F%2Fwww.gwg.nga.mil%2Fdocuments%2Fcsmwg%2FMIL-STD-2401.pdf&ei=R4v6UcjZN-atigLgpIHwDw&usg=AFQjCNH6Qx9n3K7_40Wbr2p0z-ZtRiAIvA&bvm=bv.50165853,d.cGE),
> a record with an `srs_id`  of -1, an organization of “NONE”, an `organization_coordsys_id` of -1,
> and definition  “undefined” for undefined Cartesian coordinate reference systems, and a record
> with an `srs_id` of 0, an organization of “NONE”, an `organization_coordsys_id`  of 0, and
> definition  “undefined” for undefined geographic coordinate reference systems.

> **Req 8:** The `spatial_ref_sys` table or updateable view in a GeoPackage file SHALL contain records to define all spatial reference systems used by features and tiles in a GeoPackage.

#### 1.1.3. Contents
#### 1.1.3.1. Data
#### 1.1.3.1.1. Table Definition

> **Req 9:** A GeoPackage file SHALL include a `gpkg_contents` table or updateable view per clause
1.1.3.1.1, table 3 and table 22. The purpose of the `gpkg_contents` table is to provide identifying and
descriptive information that an application can display to a user in a menu of geospatial data that
is available for access and/or update.

*Table 3: Contents Table or View Definition*

| Column Name | Type | Description | Null | Default | Key |
|-------------|------|-------------|------|---------|-----|
| `table_name` | text | The name of the tiles, or feature table | no | | PK |
| `data_type` | text | Type of data stored in the table:. “features” per  clause 2.1.2.1.1,  “tiles” per clause 2.2.2.1.1, or an implementer-defined value for other data tables per clause 2.5.| no | | |
| `identifier` | text | A human-readable identifier (e.g. short name) for the table_name content | no | | |
| `description` | text | A human-readable description for the table_name content | no | “” | | 
| `last_change` | text | timestamp value in ISO 8601 format as defined by the strftime function '%Y-%m-%dT%H:%M:%fZ' format string applied to the current time | no | `strftime('%Y-%m-%dT%H:%M:%fZ', CURRENT_TIMESTAMP)` | |
| `min_x` | double | Bounding box for all content in table_name | no | | |
| `min_y` | double | Bounding box for all content in table_name | no | | |
| `max_x` | double | Bounding box for all content in table_name | no | | |
| `max_y` | double | Bounding box for all content in table_name | no | | |
| `srs_id` | integer | Spatial Reference System ID: `gpkg_spatial_ref_sys.srs_id`; when `data_type` is features, SHALL also match `gpkg_geometry_columns.srs_id` | no | | FK |

The `gpkg_contents` table is intended to provide a list of all geospatial contents in the GeoPackage. The `data_type` specifies the type of content. The bounding box (`min_x`, `min_y`, `max_x`, `max_y`) provides an informative bounding box (not necessarily minimum bounding box) of the content. If the `srs_id column` value references a geographic coordinate reference system (CRS), then the min/max x/y values are in decimal degrees; otherwise, the srs_id references a projected CRS and the min/max x/y values are in the units specified by that CRS.

See Annex C Table Definition SQL (Normative) C.2 `gpkg_contents`.

#### 1.1.3.1.2. Table Data Values

> **Req 10:** The `table_name` column value in a `gpkg_contents` table row SHALL contain the name of a SQLite table or view.

> **Req 11:** Values of the `gpkg_contents` table `last_change` column SHALL be in [ISO 8601](http://www.iso.org/iso/catalogue_detail?csnumber=40874) format containing a complete date plus UTC hours, minutes, seconds and a decimal fraction of a second, with a ‘Z’ (‘zulu’) suffix indicating UTC.[^4]

> **Req 12:** Values of the `gpkg_contents` table `srs_id` column SHALL reference values in the `spatial_ref_sys` table `srs_id` column.


[^1]: [SQLite version 4](http://sqlite.org/src4/doc/trunk/www/design.wiki), which will be an alternative to version 3, not a replacement thereof, was not available when this specification was written. See Future Work clause in Annex B.

[^2]: SQLite is in the public domain (see http://www.sqlite.org/copyright.html)

[^3]: New applications should use the [latest available](http://www.sqlite.org/download.html) SQLite version software

[^4]: The following statement selects an ISO 8601timestamp value using the SQLite strftime function: `SELECT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))`.
￼
