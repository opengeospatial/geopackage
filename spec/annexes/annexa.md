Conformance / Abstract Test Suite (Normative)
=============================================

## Base

### Core

#### SQLite Container

#####   Data

###### File Format

**Test Case ID**: /base/core/container/data/file\_format

*Test Purpose*: Verify that the Geopackage file is an SQLite version\_3 database

*Test Method*: Pass if the first 16 bytes of the file contain "SQLite format 3" in ASCII.

*Reference*: Clause 1.1.1.1.1 Req 1:

*Test Type*: Basic

###### File Extension Name

**Test Case ID**: /base/core/container/data/file\_extension\_name

*Test Purpose*: Verify that the geopackage file extension is ".gpkg"

*Test Method*: Pass if the geopackage file extension is ".gpkg"

*Reference*: Clause 1.1.1.1.2 Req 2:

*Test Type*: Basic
 
###### Integrity Check

**Test Case ID**: /base/core/container/data/file\_integrity

*Test Purpose*: Verify that the geopackage file passes the SQLite integrity check.

*Test Method*: Pass if PRAGMA integrity\_check returns "ok"

*Reference*: Clause 1.1.1.1.3 Req 3:

*Test Type*: Capability
 
##### API

###### Structured Query Language

**Test Case ID**: /base/core/container/api/sql

*Test Purpose*: Test that the GeoPackage SQLite Extension provides the SQLite SQL API
 interface.

*Test Method*:

1. SELECT * FROM sqlite\_master
2. Fail if returns an SQL error.
3. Pass otherwise

*Reference*:     Clause 1.1.1.2.1 Req 4:

*Test Type*:     Capability
 
###### Every GPKG SQLite Configuration

**Test Case ID**: /base/core/container/api/every\_gpkg\_sqlite\_config

*Test Purpose*: Verify that a GeoPackage SQLite Extension has the Every GeoPackage
 SQLite Configuration compile and run time options.

*Test Method*:

1. SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_AUTOINCREMENT')
2.    Fail if returns 1
3.    SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_DATETIME\_FUNCS')
4.    Fail if returns 1
5.    SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_ DEPRECATED ')
6.    Fail if returns 0
7.    SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_ FLOATING\_POINT ')
8.    Fail if returns 1
9.    SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_PRAGMA')
10.   Fail if returns 1
11.   SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_FLAG\_PRAGMAS')
12.   Fail if returns 1
13.   SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_VIEW')
14.   Fail if returns 1
15.   Pass otherwise

*Reference*:     Clause 1.1.1.2.2 Req 5:

*Test Type*:     Basic

#### Spatial Reference Systems

##### Data

###### Table Definition


**Test Case ID**: /base/core/spatial\_ref\_sys/data/table\_def

*Test Purpose*: Verify that the spatial\_ref\_sys table exists and has the correct definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name = 'gpkg\_spatial\_ref\_sys'
2. Fail if returns an empty result set
3. Pass if column names and column definitions in the returned CREATE TABLE
    statement in the sql column value, including data type, nullability, default values and
    primary, foreign and unique key constraints match all of those in the contents of C.1
    Table 19. Column order, check constraint and trigger definitions, and other column
    definitions in the returned sql are irrelevant.
4. Fail otherwise.

*Reference*:     Clause 1.1.2.1.1 Req 6:

*Test Type*:     Basic
 
###### Table Data Values


**Test Case ID**: /base/core/spatial\_ref\_sys/data\_values\_default

*Test Purpose*: Verify that the spatial\_ref\_sys table contains the required default contents.

*Test Method*:

1. SELECT srid, auth\_name, auth\_srid, srtext FROM spatial\_ref\_sys WHERE srid = -1
    returns -1 "NONE" -1 "Undefined", AND
2. SELECT srid, auth\_name, auth\_srid, srtext FROM spatial\_ref\_sys WHERE srid = 0
    returns 0 "NONE" 0 "Undefined", AND
3. SELECT srid, auth\_name, auth\_srid, srtext FROM spatial\_ref\_sys WHERE srid =
    4326 returns 4326 epsg 4326 GEOGCS["WGS 84", DATUM["WGS\_1984",
  SPHEROID["WGS 84",6378137,298.257223563, AUTHORITY["EPSG","7030"]],
  AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","
  8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],
  AUTHORITY["EPSG","4326"]] (whitespace irrelevant)
4. Pass if tests 1-3 are met
5. Fail otherwise

*Reference*:     Clause 1.1.2.1.2 Req 7:

*Test Type*:     Capability


**Test Case ID**: /base/core/spatial\_ref\_sys/data\_values\_required

*Test Purpose*: Verify that the spatial\_ref\_sys table contains rows to define all srs\_id values
 used by features and tiles in a GeoPackage.

*Test Method*:

1. SELECT DISTINCT gc.srs\_id AS gc\_srid, srs.srs\_name, srs.srs\_id, srs.organization,
  srs.organization\_coordsys\_id, srs.definition FROM gpkg\_contents AS gc LEFT
  OUTER JOIN gpkg\_spatial\_ref\_sys AS srs ON srs.srs\_id = gc.srs\_id
2. Pass if no returned srs values are NULL.
3. Fail otherwise

*Reference*:     Clause Clause 1.1.2.1.2 Req 7:

#### Test Type: CapabilityContents

#####   Data

###### Table Definition


**Test Case ID**: /base/core/contents/data/table\_def

*Test Purpose*: Verify that the gpkg\_contents table exists and has the correct definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name = 'gpkg\_contents'
2. Fail if returns an empty result set.
3. Pass if the column names and column definitions in the returned CREATE TABLE
  statement, including data type, nullability, default values and primary, foreign and
  unique key constraints match all of those in the contents of C.2 Table 20. Column
  order, check constraint and trigger definitions, and other column definitions in the
  returned sql are irrelevant.
4. Fail Otherwise

*Reference*:     Clause 1.1.3.1.1 Req 9:

*Test Type*:     Basic
 
###### Table Data Values

**Test Case ID**: /base/core/contents/data/data\_values\_table\_name

*Test Purpose*: Verify that the table\_name column values in the gpkg\_contents table are
 valid.

*Test Method*:

1. SELECT DISTINCT gc.table\_name AS gc\_table, sm.tbl\_name
FROM gpkg\_contents AS ge LEFT OUTER JOIN sqlite\_master AS sm ON
gc.table\_name = sm.tbl\_name
2. Not testable if returns an empty result set.
3. Fail if any gpkg\_contents.table\_name value is NULL
4. Pass otherwise.

*Reference*:    Clause 1.1.3.1.2 Req 10:

*Test Type*:    Capability



**Test Case ID**: /base/core/contents/data/data\_values\_last\_change

*Test Purpose*: Verify that the gpkg\_contents table last\_change column values are in ISO
 8601 [41]format containing a complete date plus UTC hours, minutes, seconds and a
 decimal fraction of a second, with a 'Z' ('zulu') suffix indicating UTC.

*Test Method*:

1. SELECT last\_change from gpkg\_contents.
2. Not testable if returns an empty result set.
3. For each row from step 1
  - Fail if format of returned value does not match yyyy-mm-ddThh:mm:ss.hhhZ
  - Log pass otherwise
4. Pass if logged pass and no fails.

*Reference*:    Clause 1.1.3.1.2 Req 11:

*Test Type*:    Capability



**Test Case ID**: /base/core/contents/data/data\_values\_srs\_id

*Test Purpose*: Verify that the gpkg\_contents table srs\_id column values are defined in the
 gpkg\_spatial\_ref\_sys table.

*Test Method*:

1. SELECT srs\_id FROM gpkg\_contents
2. Not testable if returns an empty result set
3. SELECT srs\_id FROM gpkg\_contents WHERE srs\_id NOT IN (SELECT srs\_id
  FROM gpkg\_spatial\_ref\_sys)
4. Fail if does not return an empty result set
5. SELECT srs\_id FROM gpkg\_contents gc WHERE data\_type = 'features' AND srs\_id
  NOT IN (SELECT srs\_id FROM gpkg\_geometry\_columns WHERE table\_name =
  gc.table\_name)
6. Fail if does not return an empty result set
7. Pass otherwise

*Reference*:    Clause Clause 1.1.3.1.2 Req 12:

*Test Type*:    Capability


## Options


**Test Case ID**: /opt/valid\_geopackage

*Test Purpose*: Verify that a GeoPackage contains a features or tiles table and gpkg\_contents
 table row describing it.

*Test Method*:

1.   Execute test /opt/features/contents/data/features\_row
2.   Pass if test passed
3.   Execute test /opt/tiles/contents/data/tiles\_row
4.   Pass if test passed
5.   Fail otherwise

*Reference*:     Clause 2 Req 13:

*Test Type*:     Capability
 
### Features

#### Contents

#####   Data

###### Contents Table Feature Row


**Test Case ID**: /opt/features/contents/data/features\_row

*Test Purpose*: Verify that the gpkg\_contents table\_name value table exists, and is
 apparently not a tiles table for every row with a data\_type column value of "features"

*Test Method*:

1. SELECT table\_name FROM gpkg\_contents where data\_type="features"
2. Fail if returns empty result set
3. For each row from step 1
  * PRAGMA table\_info(table\_name)
  * Fail if returns an empty result set
  * Fail if result set contains four rows where the name column values are "zoom\_level","tile\_column","tile\_row", and "tile\_data"
  * Fail if result set does not contain one row where the pk column value is 1 and the type column value is "INTEGER"
4. Pass if no fails

*Reference*:     Clause 2.1.2.1.1 Req 14:

*Test Type*:     Capability
 
#### Geometry Encoding

#####   Data

###### BLOB Format


**Test Case ID**: /opt/features/geometry\_encoding/data/blob

*Test Purpose*: Verify that geometries stored in feature table geometry columns are encoded
 in the GeoPackageBinary format.

*Test Method*:

1. SELECT table\_name AS tn, column\_name AS cn FROM gpkg\_geometry\_columns
  WHERE table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE
  data\_type = 'features')
2. Not testable if returns an empty result set
3. For each row from step 1
  * SELECT cn FROM tn
  * Not testable if none found
  * For each cn value from step a
      -  Fail if the first three bytes of each gc are not "GPB"
      -  Fail if gc.version\_number is not 0
      -  Fail if ST\_IsEmpty(cn value) = 1 and gc.flags.envelope != 0 and envelope values are not NaN
4. Pass if no fails

*Reference*:    Clause 2.1.3.1.1 Req 15:

*Test Type*:    Capability
 
#####   API

###### Minimal Runtime SQL Functions


**Test Case ID**: /opt/features/geometry\_encoding/sql\_func

*Test Purpose*: Verify that a GeoPackage SQLite Extension provides the GeoPackage
 Minimal Runtime SQL functions.

*Test Method*:

1. Open Geometry Test Data Set GeoPackage with GeoPackage SQLite Extension
2. For each Geometry Test Data Set &lt;gtype\_test&gt; data table row for each assignable
      (gtype, atype) and non-assignable (ntype, atype) combination of geometry type in
      Annex G, for an assortment of srs\_ids, for an assortment of coordinate values,
      without and with z and / or m values, in both big and little endian encodings:
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_SRID(geom) != srs\_id
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_GeometryType(geom) !=
          atype
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE GPKG\_IsAssignable(gtype,
          atype) = 0
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE GPKG\_IsAssignable(ntype,
          atype) = 1
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_Is3D(geom) != is3d
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_IsMeasured(geom) != ism
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MinX(geom) != minx
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MaxX(geom) != maxx
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MinY(geom) != miny
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MaxY(geom) != maxy
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MinZ(geom) != minz
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MaxZ(geom) != maxz
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MinM(geom) != minm
      - SELECT 'Fail' FROM &lt;gtype\_test&gt; WHERE ST\_MaxM(geom) != maxm
3. Pass if no 'Fail' selected from step 2

*Reference*:    Clause 2.1.3.2.1 Req 16:

*Test Type*:    Capability
 
#### Geometry Types

#####  Data

###### Core Types

**Test Case ID**: /opt/features/geometry\_encoding/data/core\_types\_existing\_sparse\_data

*Test Purpose*: Verify that existing basic simple feature geometries are stored in valid GeoPackageBinary format encodings.

*Test Method*:

1. SELECT table\_name FROM gpkg\_geometry\_columns
2. Not testable if returns an empty result set
3. SELECT table\_name AS tn, column\_name AS cn FROM gpkg\_geometry\_columns
    WHERE table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE
    data\_type = 'features'),
4. Fail if returns an empty result set
5. For each row from step 3
     - SELECT cn FROM tn;
     - For each row from step a, if bytes 2-5 of cn.wkb as uint32 in endianness of
            gc.wkb byte 1of cn from #1 are a geometry type value from Annex G Table 46,
            then
         +     Log cn.header values, wkb endianness and geometry type
         +     If cn.wkb is not correctly encoded per ISO 13249-3 clause 5.1.46 then log
                fail
         +      If cn.flags.E is 1 - 4 and some cn.wkbx is outside of cn.envelope.minx,maxx
                then log fail
         +      If cn.flags.E is 1 - 4 and some gc.wkby is outside of cn.envelope.miny,maxy
                then log fail
         +      If cn.flags.E is 2,4 and some gc.wkb.z is outside of cnenvelope.minz,maxz
                then log fail
         +      If cn.flags.E is 3,4 and some gc.wkb.m is outside of cn.envelope.minm,maxm
                then log fail
         +      If cn.flags.E is 5-7 then log fail
         +      Otherwise log pass

6. Pass if log contanins pass and no fails

*Reference*:     Clause 2.1.4.1.1 Req 17:

*Test Type*:     Capability


**Test Case ID**: /opt/features/geometry\_encoding/data/core\_types\_all\_types\_test\_data

*Test Purpose*: Verify that all basic simple feature geometry types and options are stored in valid GeoPackageBinary format encodings.

*Test Method*:

1. Open GeoPackage that has feature geometry values of geometry type in Annex G, for
  an assortment of srs\_ids, for an assortment of coordinate values, without and with z
  and / or m values, in both big and little endian encodings:
2. /opt/features/geometry\_encoding/data/core\_types\_existing\_sparse\_data
3. Pass if log contains pass record for big and little endian GPB headers containing big
  and little endian WKBs for 0-1 envelope contents indicator codes for every geometry
  type value from Annex G Table 46 without and with z and/or m values.
4. Fail otherwise

*Reference*:     Clause 2.1.4.1.1 Req 17:

*Test Type*:     Capability
 
#### Geometry Columns

##### Data

###### Table Definition


**Test Case ID**: /opt/features/geometry\_columns/data/table\_def

*Test Purpose*: Verify that the gpkg\_geometry\_columns table exists and has the correct
 definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name =
    'gpkg\_geometry\_columns'
2. Fail if returns an empty result set.
3. Pass if the column names and column definitions in the returned Create TABLE
    statement in the sql column value, including data type, nullability, default values and
    primary, foreign and unique key constraints match all of those in the contents of C.4
    Table 22. Column order, check constraint and trigger definitions, and other column
    definitions in the returned sql are irrelevant.
4. Fail otherwise.

*Reference*:     Clause 2.1.5.1.1 Req 18:

*Test Type*:     Basic
 
###### Table Data Values


**Test Case ID**: /opt/features/geometry\_columns/data/data\_values\_table\_name

*Test Purpose*: Verify that the table\_name column values in the gpkg\_geometry\_columns
 table are valid.

*Test Method*:

1. SELECT DISTINCT table\_name FROM gpkg\_geometry columns
2. Not testable if returns an empty result set.
3. For each row from setp 1
    - Fail if table\_name value is NULL
4. SELECT DISTINCT ggc.table\_name AS ggc\_table, gc.table\_name
    FROM gpkg\_geometry\_columns AS ggc LEFT OUTER JOIN geopackage\_contents
    AS gc ON ggc.table\_name = gc.table\_name
5. For each row from step 4
    - Fail if ggc.table\_name != gc.table\_name
6. Pass if no fails.

*Reference*:     Clause 2.1.5.1.2 Req 19:

*Test Type*:     Capability



**Test Case ID**: /opt/features/geometry\_columns/data/data\_values\_column\_name

*Test Purpose*: Verify that the column\_name column values in the gpkg\_geometry\_columns
table are valid.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns
2. Not testable if returns an empty result set
3. For each row from step 1
    - PRAGMA table\_info(table\_name)
    - Fail if gpkg\_geometry\_columns.column\_name value does not equal a name
	column value returned by PRAGMA table\_info.

Pass if no fails.

*Reference*:   Clause 2.1.5.1.2 Req 20:

*Test Type*: Capability


**Test Case ID**: /opt/features/geometry\_columns/data/data\_values\_geometry\_type\_name

*Test Purpose*: Verrify that the geometry\_type\_name column values in the
gpkg\_geometry\_columns table are valid.

*Test Method*:

1. SELECT DISTINCT geometry\_type\_name from gpkg\_geometry\_columns
2. Not testable if returns an empty result set
3. For each row from step 1
    - Fail if a returned geometry\_type value is not in Table 46 or Table 47 in Annex G
4. Pass if no fails.

*Reference*:     Clause 2.1.5.1.2 Req 21:

*Test Type*:     Capability


**Test Case ID**: /opt/features/geometry\_columns/data/data\_values\_srs\_id

*Test Purpose*: Verify that the gpkg\_geometry\_columns table srs\_id column values are
defined in the gpkg\_spatial\_ref\_sys table.

*Test Method*:

1. SELECT srs\_id FROM gpkg\_geometry\_columns
2. Not testable if returns an empty result set
3. SELECT srs\_id FROM gpkg\_geometry\_columns WHERE srs\_id NOT IN (SELECT
    srs\_id FROM gpkg\_spatial\_ref\_sys)
4. Fail if does not return an empty result set
5. Pass otherwise.

*Reference*:     Clause 2.1.5.1.2 Req 22:

*Test Type*:     Capability


**Test Case ID**: /opt/features/geometry\_columns/data/data\_values\_z

*Test Purpose*: Verify that the gpkg\_geometry\_columns table z column values are valid.

*Test Method*:

1.   SELECT z FROM gpkg\_geometry\_columns
2.   Not testable if returns an empty result set
3.   SELECT z FROM gpkg\_geometry\_columns WHERE z NOT IN (1,2,3)
4.   Fail if does not return an empty result set
5.   Pass otherwise.

*Reference*:     Clause 2.1.5.1.2 Req 23:

*Test Type*:     Capability



**Test Case ID**: /opt/features/geometry\_columns/data/data\_values\_m

*Test Purpose*: Verify that the gpkg\_geometry\_columns table m column values are valid.

*Test Method*:

1.   SELECT m FROM gpkg\_geometry\_columns
2.   Not testable if returns an empty result set
3.   SELECT m FROM gpkg\_geometry\_columns WHERE m NOT IN (1,2,3)
4.   Fail if does not return an empty result set
5.   Pass otherwise.

*Reference*:     Clause 2.1.5.1.2 Req 24:

*Test Type*:     Capability


#### Vector Features User Data Tables

##### Data

###### Table Definition


**Test Case ID**: /opt/features/vector\_features/data/feature\_table\_integer\_primary\_key

*Test Purpose*: Verify that every vector features user data table has an integer primary key.

*Test Method*:

1. SELECT table\_name FROM gpkg\_contents WERE data\_type = 'features'
2. Not testable if returns an empty result set
3. For each row from step 1
   - PRAGMA table\_info(table\_name)
   - Fail if returns an empty result set
   - Fail if result set does not contain one row where the pk column value is 1 and the not
       null column value is 1 and the type column value is "INTEGER"
4. Pass if no fails.

*Reference*:     Clause 2.1.6.1.1 Req 25:

*Test Type*:     Basic

**Test Case ID**: /opt/features/vector/features/data/feature\_table\_one\_geometry\_column

*Test Purpose*: Verify that every vector features user data table has one geometry column.

*Test Method*:

1. SELECT table\_name FROM gpkg\_contents WERE data\_type = 'features'
2. Not testable if returns an empty result set
3. For each row table name from step 1
   - SELECT column\_name from gpkg\_geometry\_columns where table\_name = row
       table name
   - Fail if returns more than one column name
4. Pass if no fails
  
*Reference*: Clause 2.1.6.1.1 Req 26:
  
*Test Type*: Capability

###### Table Data Values

**Test Case ID**: /opt/features/vector\_features/data/data\_values\_geometry\_type

*Test Purpose*: Verify that the geometry type of feature geometries are of the type or are
 assignable for the geometry type specified by the gpkg\_geometry columns table
 geometry\_type\_name column value.

*Test Method*:

1. SELECT table\_name AS tn, column\_name AS cn, geometry\_type\_name AS gt\_name
  FROM gpkg\_geometry\_columns WHERE table\_name IN (SELECT table\_name
  FROM gpkg\_contents WHERE data\_type = 'features')
2. Not testable if returns an empty result set
3. For each row from step 1
  - SELECT DISTINCT ST\_GeometryType(cn) FROM tn
  - For each row actual\_type\_name from step a
      +    SELECT GPKG\_IsAssignable(geometry\_type\_name, actual\_type\_name)
      +    Fail if any returned 0
4. Pass if no fails

*Reference*:     Clause 2.1.6.1.2 Req 27:

*Test Type*:     Capability



**Test Case ID**: /opt/features/vector\_features/data/tata\_value\_geometry\_srs\_id

*Test Purpose*: Verify the the srs\_id of feature geometries are the srs\_id specified for the
 gpkg\_geometry\_columns table srs\_id column value.

*Test Method*:

1. SELECT table\_name AS tn, column\_name AS cn, srs\_id AS gc\_srs\_id FROM
  gpkg\_geometry\_columns WHERE table\_name IN (SELECT table\_name FROM
  gpkg\_contents where data\_type = 'features')
2. Not testable if returns an empty result set
3. For each row from step 1
  - SELECT DISTINCT st\_srid(cn) FROM tn
  - For each row from step a
    +     Fail if returnvalue not equal to gc\_srs\_id
4. Pass if no fails

*Reference*:     Clause 2.1.6.1.2 Req 28:

*Test Type*:     Capability
 
### Tiles

#### Contents

#####   Data

###### Contents Table - Tiles Row


**Test Case ID**: /opt/tiles/contents/data/tiles\_row

*Test Purpose*: Verify that the gpkg\_contents table\_name value table exists and is apparently
 a tiles table for every row with a data\_type column value of "tiles".

*Test Method*:

1. SELECT table\_name FROM gpkg\_contents WHERE data\_type = "tiles"
2. Fail if returns empty result set
3. For each row from step 1
  - PRAGMA table\_info(table\_name)
  - Fail if returns an empty result set
  - Fail if result set does not contain one row where the pk column value is 1 and the
      not null column value is 1 and the type column value is "INTEGER"and the
      name column value is "id"
  - Fail if result set does not contain four other rows where the name column values
      are "zoom\_level","tile\_column","tile\_row", and "tile\_data".
4. Pass if no fails.

*Reference*:     Clause 2.2.2.1.1 Req 29:

*Test Type*:     Capability
 
#### Zoom Levels

#####   Data

###### Zoom Times Two


**Test Case ID**: /opt/tiles/zoom\_levels\_data\_zoom\_times\_two

*Test Purpose*: Verify that by default zoom level pixel sizes for tile matrix user data tables
 vary by powers of 2 between adjacent zoom levels in the tile matrix metadata table.

*Test Method*:

1. SELECT CASE
  WHEN (SELECT tbl\_name FROM sqlite\_master WHERE tbl\_name =
  'gpkg\_extensions') = 'gpkg\_extensions' THEN
  (SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles' AND
  table\_name NOT IN
    (SELECT table\_name from gpkg\_extensions WHERE extension\_name =
  'gpkg\_zoom\_other'))
  ELSE (SELECT table\_name FROM geopackage\_contents WHERE data\_type =
  'tiles')
  END;
2. Not testable if returns empty result set
3. For each row table\_name from step 1
  - SELECT zoom\_level, pixel\_x\_size, pixel\_y\_size FROM tile\_matrix\_metadata
	WHERE table\_name = selected table name ORDER BY zoom\_level ASC
  - Not testable if returns empty result set, or only one row
  - Not testable if there are not two rows with adjacent zoom levels
  - Fail if any pair of rows for adjacent zoom levels have pixel\_x\_size or
      pixel\_y\_size values that differ by other than powers of two
4. Pass if no fails

*Reference*:      Clause 2.2.3.1.1 Req 30:

*Test Type*:      Capability

#### Tile Encoding PNG

##### Data

###### MIME Type PNG


**Test Case ID**: /opt/tiles/tiles\_encoding/data/mime\_type\_png

*Test Purpose*: Verify that a tile matrix user data table that contains tile data that is not
 MIME type image/jpeg by default contains tile data in MIME type image/png.

*Test Method*:

1. SELECT CASE
    WHEN (SELECT tbl\_name FROM sqlite\_master WHERE tbl\_name =
    'gpkg\_extensions') = 'gpkg\_extensions' THEN
    (SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles' AND
    table\_name NOT IN
    (SELECT table\_name from gpkg\_extensions WHERE extension\_name IN
    ('gpkg\_webp','gpkg\_tiff','gpkg\_nitf')))
    ELSE (SELECT table\_name FROM geopackage\_contents WHERE data\_type =
    'tiles')
    END;
2. Not testable if returns empty result set
3. For each row tbl\_name from step 1
    - SELECT tile\_data FROM tbl\_name
    - For each row tile\_data from step a
	+ Pass if tile data in MIME type image/png
4. Fail if no passes

*Reference*:      Clause 2.2.4.1.1 Req 31:

*Test Type*:      Capability
 
#### Tile Encoding JPEG

##### Data

###### MIME Type JPEG


**Test Case ID**: /opt/tiles/tiles\_encoding/data/mime\_type\_jpeg

*Test Purpose*: Verify that a tile matrix user data table that contains tile data that is not
 MIME type image/png by default contains tile data in MIME type image/jpeg.

*Test Method*:

1. SELECT CASE
  WHEN (SELECT tbl\_name FROM sqlite\_master WHERE tbl\_name =
  'gpkg\_extensions') = 'gpkg\_extensions' THEN
  (SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles' AND
  table\_name NOT IN
    (SELECT table\_name from gpkg\_extensions WHERE extension\_name IN
  ('gpkg\_webp','gpkg\_tiff','gpkg\_nitf')))
  ELSE (SELECT table\_name FROM geopackage\_contents WHERE data\_type =
  'tiles')
  END;
2. Not testable if returns empty result set
3. For each row tbl\_name from step 1
  - SELECT tile\_data FROM tbl\_name
  - For each row tile\_data from step a
      +   Pass if tile data in MIME type image/jpeg
4. Fail if no passes

*Reference*:    Clause 2.2.5.1.1 Req 32:

*Test Type*:    Capability
 
#### Tile Matrix Metadata

##### Data

###### Table Definition


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/table\_def

*Test Purpose*: Verify that the gpkg\_tile\_matrix\_metadata table exists and has the correct
 definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name =
  'gpkg\_tile\_matrix\_metadata'
2. Fail if returns an empty result set.
3. Pass if the column names and column definitions in the returned CREATE TABLE
  statement in the sql column value,, including data type, nullability, default values and
  primary, foreign and unique key constraints match all of those in the contents of C.7
  Table 25. Column order, check constraint and trigger definitions, and other column
  definitions in the returned sql are irrelevant.
4. Fail otherwise.

*Reference*:    Clause 2.2.6.1.1 Req 33:

*Test Type*:    Basic


###### Table Data Values

**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data\_values\_table\_name

*Test Purpose*: Verify that values of the gpkg\_tile\_matrix\_metadata table\_name column
 reference values in the gpkg\_contents table\_name column for rows with a data type of
 "tiles".

*Test Method*:

1. SELECT table\_name FROM gpkg\_tile\_matrix\_metadata
2. Not testable if returns an empty result set
3. SELECT table\_name FROM gpkg\_tile\_matrix\_metadata tmm WHERE table\_name
    NOT IN (SELECT table\_name FROM gpkg\_contents gc WHERE tmm.table\_name =
    gc.table\_name)
4. Fail if result set contains any rows
5. Pass otherwise
  
*Reference*:    Clause 2.2.6.1.2 Req 34:

*Test Type*:    Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_zoom\_level\_rows

*Test Purpose*: Verify that the gpkg\_tile\_matrix\_metadata table contains a row record for
each zoom level that contains one or more tiles in each tile matrix user data table.

*Test Method*:

1. SELECT table\_name AS &lt;user\_data\_tiles\_table&gt; from gpkg\_contents where
    data\_type = 'tiles'
2. Not testable if returns an empty result set
3. For each row from step 1
    - SELECT DISTINCT gtmm.zoom\_level AS gtmm\_zoom, udt.zoom\_level AS
	udtt\_zoom FROM tile\_matrix\_metadata AS gtmm
	LEFT OUTER JOIN &lt;user\_data\_tiles\_table&gt; AS udtt ON udtt.zoom\_level =
	gtmm.zoom\_level AND gtmm.t\_table\_name = '&lt;user\_data\_tiles\_table&gt;'
    - Fail if any gtmm\_zoom column value in the result set is NULL
4. Pass if no fails

*Reference*:    Clause 2.2.6.1.2 Req 35:

*Test Type*:    Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_zoom\_level

*Test Purpose*: Verify that zoom level column values in the gpkg\_tile\_matrix\_metadata table
are not negative.

*Test Method*:

1.   SELECT zoom\_level FROM gpkg\_tile\_matrix\_metadata
2.   Not testable if returns an empty result set
3.   SELECT min(zoom\_level) FROM gpkg\_tile\_matrix\_metadata.
4.   Fail if less than 0.
5.   Pass otherwise.

*Reference*:    Clause 2.2.6.1.2 Req 36:

*Test Type*:    Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_matrix\_width

*Test Purpose*: Verify that the matrix\_width values in the gpkg\_tile\_matrix\_metadata table
are valid.

*Test Method*:

1.   SELECT matrix\_width FROM gpkg\_tile\_matrix\_metadata
2.   Not testable if returns an empty result set
3.   SELECT min(matrix\_width) FROM gpkg\_tile\_matrix\_metadata.
4.   Fail if less than 1.
5.   Pass otherwise.

*Reference*:     Clause 2.2.6.1.2 Req 37:

*Test Type*:     Capabilty


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_matrix\_height

*Test Purpose*: Verify that the matrix\_height values in the gpkg\_tile\_matrix\_metadata table
are valid.

*Test Method*:

1.   SELECT matrix\_height FROM gpkg\_tile\_matrix\_metadata
2.   Not testable if returns an empty result set
3.   SELECT min(matrix\_height) FROM gpkg\_tile\_matrix\_metadata.
4.   Fail if less than 1.
5.   Pass otherwise.

*Reference*:     Clause 2.2.6.1.2 Req 38:

*Test Type*:     Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_tile\_width

*Test Purpose*: Verify that the tile\_width values in the gpkg\_tile\_matrix\_metadata table are
valid.

*Test Method*:

1.   SELECT tile\_width FROM gpkg\_tile\_matrix\_metadata
2.   Not testable if returns an empty result set
3.   SELECT min(tile\_width) FROM gpkg\_tile\_matrix\_metadata.
4.   Fail if less than 1.
5.   Pass otherwise.

*Reference*:     Clause 2.2.6.1.2 Req 39:

*Test Type*:     Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_tile\_height

*Test Purpose*: Verify that the tile\_height values in the gpkg\_tile\_matrix\_metadata table are
valid.

*Test Method*:

1. SELECT tile\_height FROM gpkg\_tile\_matrix\_metadata
2.   Not testable if returns an empty result set
3.   SELECT min(tile\_height) FROM gpkg\_tile\_matrix\_metadata.
4.   Fail if less than 1.
5.   Pass otherwise.

*Reference*:    Clause 2.2.6.1.2 Req 40:

*Test Type*:    Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_pixel\_x\_size

*Test Purpose*: Verify that the pixel\_x\_size values in the gpkg\_tile\_matrix\_metadata table
are valid.

*Test Method*:

1.   SELECT pixel\_x\_size FROM gpkg\_tile\_matrix\_metadata
2.   Not testable if returns an empty result set
3.   SELECT min(pixel\_x\_size) FROM gpkg\_tile\_matrix\_metadata.
4.   Fail if less than 0.
5.   Pass otherwise.

*Reference*:    Clause 2.2.6.1.2 Req 41:

*Test Type*:    Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_pixel\_y\_size

*Test Purpose*: Verify that the pixel\_y\_size values in the gpkg\_tile\_matrix\_metadata table
are valid.

*Test Method*:

1.   SELECT pixel\_y\_size FROM gpkg\_tile\_matrix\_metadata
2.   Not testable if returns an empty result set
3.   SELECT min(pixel\_y\_size) FROM gpkg\_tile\_matrix\_metadata.
4.   Fail if less than 0.
5.   Pass otherwise.

*Reference*:    Clause 2.2.6.1.2 Req 42:

*Test Type*:    Capability


**Test Case ID**: /opt/tiles/tile\_matrix\_metadata/data/data\_values\_pixel\_size\_sort

*Test Purpose*: Verify that the pixel\_x\_size and pixel\_y\_size column values for zoom level
column values in a gpkg\_tile\_matrix\_metadata table sorted in ascending order are sorted in
descending order, showing that lower zoom levels are zoomed "out".

*Test Method*:

1. SELECT table\_name FROM gpkg\_contents WHERE data\_type = 'tiles'
2. Not testable if returns empty result set
3. For each row table\_name from step 1
    - SELECT zoom\_level, pixel\_x\_size, pixel\_y\_size from
	gpkg\_tile\_matrix\_metadata WHERE table\_name = row table name ORDER BY
	zoom\_level ASC
    - Not testable if returns empty result set
    - Fail if pixel\_x\_sizes are not sorted in descending order
    - Fail if pixel\_y\_sizes are not sorted in descending order
4. Pass if testable and no fails

*Reference*:     Clause 2.2.6.1.2 Req 43:

*Test Type*:     Capability

#### Tile Matrix User Data

##### Data

###### Table Definition


**Test Case ID**: /opt/tiles/tile\_matrix/data/table\_def

*Test Purpose*: Verify that multiple tile matrix sets are stored in different tiles tables with
 unique names containing the required columns.

*Test Method*:

1. SELECT COUNT(table\_name) FROM gpkg\_contents WERE data\_type = "tiles"
2. Fail if less than 2
3. SELECT table\_name FROM gpkg\_contents WHERE data\_type = "tiles"
4. For each row from step 3
    - PRAGMA table\_info(table\_name)
    - Fail if returns an empty result set
    - Fail if result set does not contain one row where the pk column value is 1 and the
	not null column value is 1 and the type column value is "INTEGER"and the
	name column value is "id"
    - Fail if result set does not contain four other rows where the name column values
	are "zoom\_level","tile\_column","tile\_row", and "tile\_data".
5. Pass if no fails

*Reference*:     Clause 2.2.7.1.1 Req 44:

*Test Type*:     Basic
 
###### Table Data Values


**Test Case ID**: /opt/tiles/tile\_matrix/data/data\_values\_zoom\_levels

*Test Purpose*: Verify that the zoom level column values in each tile matrix user data table
 are within the range of zoom levels defined by rows in the tile\_matrix\_metadata table.

*Test Method*:

1. SELECT DISTINCT table\_name AS &lt;user\_data\_tiles\_table&gt; FROM
  gpkg\_tile\_matrix\_metadata
2. Not testable if returns an empty result set
3. For each row &lt;user\_data\_tiles\_table&gt; from step 1
      - SELECT zoom\_level FROM &lt;user\_data\_tiles\_table&gt;
      - If result set not empty
	  + SELECT MIN(gtmm.zoom\_level) AS min\_gtmm\_zoom,
		  MAX(gtmm.zoom\_level) AS max\_gtmm\_zoom FROM
		  gpkg\_tile\_matrix\_metadata WHERE table\_name =
		  &lt;user\_data\_tiles\_table&gt;
	  + SELECT id FROM &lt;user\_data\_tiles\_table&gt; WHERE zoom\_level &lt;
		  min\_gtmm\_zoom
	  + Fail if result set not empty
	  + SELECT id FROM &lt;user\_data\_tiles\_table&gt; WHERE zoom\_level &gt;
		  max\_gtmm\_zoom
	  + Fail if result set not empty
	  + Log pass otherwise
4. Pass if logged pas and no fails

*Reference*:     Clause 2.2.7.1.2 Req 45:

*Test Type*:     Capability


**Test Case ID**: /opt/tiles/tile\_matrix/data/data\_values\_tile\_column

*Test Purpose*: Verify that the tile\_column column values for each zoom level value in each
tile matrix user data table are within the range of columns defined by rows in the
tile\_matrix\_metadata table.

*Test Method*:

1. SELECT DISTINCT table\_name AS &lt;user\_data\_tiles\_table&gt; FROM
    gpkg\_tile\_matrix\_metadata
2. Not testable if returns an empty result set
3. For each row &lt;user\_data\_tiles\_table&gt; from step 1
      + SELECT DISTINCT gtmm.zoom\_level AS gtmm\_zoom, gtmm.matrix\_width
	    AS gtmm\_width, udt.zoom\_level AS udt\_zoom, udt.tile\_column AS
	    udt\_column FROM tile\_matrix\_metadata AS gtmm LEFT OUTER JOIN
	    &lt;user\_data\_tiles\_table&gt; AS udt ON udt.zoom\_level = gtmm.zoom\_level AND
	    gtmm.t\_table\_name = '&lt;user\_data\_tiles\_table&gt;' AND (udt\_column &lt; 0 OR
	    udt\_column &gt; (gtmm\_width - 1))
      + Fail if any udt\_column value in the result set is not NULL
      + Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 2.2.7.1.2 Req 46:

*Test Type*:     Capability

**Test Case ID**: /opt/tiles/tile\_matrix\_data/data\_values\_tile\_row

*Test Purpose*: Verify that the tile\_row column values for each zoom level value in each tile
matrix user data table are within the range of rows defined by rows in the
tile\_matrix\_metadata table.

*Test Method*:

1. SELECT DISTINCT table\_name AS &lt;user\_data\_tiles\_table&gt; FROM
  gpkg\_tile\_matrix\_metadata
2. Not testable if returns an empty result set
3. For each row &lt;user\_data\_tiles\_table&gt; from step 1
      + SELECT DISTINCT gtmm.zoom\_level AS gtmm\_zoom, gtmm.matrix\_height
	  AS gtmm\_height, udt.zoom\_level AS udt\_zoom, udt.tile\_row AS udt\_row
	  FROM tile\_matrix\_metadata AS gtmm LEFT OUTER JOIN
	  &lt;user\_data\_tiles\_table&gt; AS udt ON udt.zoom\_level = gtmm.zoom\_level AND
	  gtmm.t\_table\_name = '&lt;user\_data\_tiles\_table&gt; ' AND (udt\_row &lt; 0 OR
	  udt\_row &gt; (gtmm\_height - 1))
      + Fail if any udt\_row value in the result set is not NULL
      + Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 2.2.7.1.2 Req 47:

*Test Type*:     Capability

### Schema

#### Data Columns

##### Data

###### Table Definition

**Test Case ID**: /opt/schema/data\_columns/data\_table\_def

*Test Purpose*: Verify that the gpkg\_data\_columns table exists and has the correct definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name = 'gpkg\_data\_columns'
2. Fail if returns an empty result set
3. Pass if column names and column definitions in the returned CREATE TABLE
    statement in the sql column value, including data type, nullability, default values and
    primary, foreign and unique key constraints match all of those in the contents of C.1
    Table 32. Column order, check constraint and trigger definitions, and other column
    definitions in the returned sql are irrelevant.
4. Fail otherwise.

*Reference*:     Clause 2.3.1.1.1 Req 48:

*Test Type*:     Basic

###### Data Values

**Test Case ID**: /opt/schema/data\_columns/data/data\_values\_table\_name

*Test Purpose*: Verify that values of the gpkg\_data\_columns table\_name column reference
 values in the gpkg\_contents table\_name column.

*Test Method*:

1. SELECT table\_name FROM gpkg\_data columns
2. Not testable if returns an empty result set
3. SELECT table\_name FROM gpkg\_data\_columns gdc WHERE table\_name NOT IN
    (SELECT table\_name FROM gpkg\_contents gc WHERE gdc.table\_name =
    gc.t\_table\_name)
4. Fail if result set contains any rows
5. Pass otherwise

*Reference*:     Clause 2.3.1.1.2 Req 49:

*Test Type*:     Capability



**Test Case ID**: /opt/schema/data\_columns/data/data\_values\_column\_name

*Test Purpose*: Verify that for each gpkg\_data\_columns row, the column\_name value is the
 name of a column in the table\_name table.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_data\_columns
2. Not testable if returns an empty result set
3. For each row from step 1
    + PRAGMA table\_info(table\_name)
    + Fail if gpkg\_data\_columns.column\_name value does not equal a name column
	value returned by PRAGMA table\_info.
4. Pass if no fails.

*Reference*:     Clause 2.3.1.1.2 Req 50:

*Test Type*:     Capability


### Metadata

#### Metadata Table

##### Data

###### Table Definition


**Test Case ID**: /opt/metadata/metadata/data/table\_def

*Test Purpose*: Verify that the gpkg\_metadata table exists and has the correct definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name = 'gpkg\_metadata'
2. Fail if returns an empty result set.
3. Pass if the column names and column definitions in the returned Create TABLE
    statement in the sql column value, including data type, nullability, default values and
    primary, foreign and unique key constraints match all of those in the contents of
    Table 33. Column order, check constraint and trigger definitions, and other column
    definitions in the returned sql are irrelevant.
4. Fail otherwise.

*Reference*:     Clause 2.4.2.1.1 Req 51:

*Test Type*:     Basic
 
###### Table Data Values


**Test Case ID**: /opt/metadata/metadata/data/data\_values\_md\_scope

*Test Purpose*: Verify that each of the md\_scope column values in a gpkg\_metadata table is
 one of the name column values from Table 11 in clause 2.4.2.1.2.

*Test Method*:

1. SELECT md\_scope FROM gpkg\_metadata
2. Not testable if returns an empty result set
3. For each row returned from step 1
  - Fail if md\_scope value not one of the name column values from Table 11 in clause 2.4.2.1.2
4. Pass if no fails

*Reference*:    Clause 2.4.2.1.2 Req 52:

*Test Type*:    Capabilities

#### Metadata Reference Table

##### Data

###### Table Definition


**Test Case ID**: /opt/metadata/metadata\_reference\_data\_table\_def

*Test Purpose*: Verify that the gpkg\_metadata\_reference table exists and has the correct
 definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name = 'gpkg\_metadata\_reference'
2. Fail if returns an empty result set.
3. Pass if the column names and column definitions in the returned Create TABLE
  statement in the sql column value, including data type, nullability, default values and
  primary, foreign and unique key constraints match all of those in the contents of
  Table 34. Column order, check constraint and trigger definitions, and other column
  definitions in the returned sql are irrelevant.
4. Fail otherwise.

*Reference*:    Clause 2.4.3.1.1 Req 53:

*Test Type*:    Basic

###### Data Values


**Test Case ID**: /opt/metadata/metadata\_reference/data/data\_values\_reference\_scope

*Test Purpose*: Verify that gpkg\_metadata\_reference table reference\_scope column values
 are valid.

*Test Method*:

1. SELECT reference\_scope FROM gpkg\_metadata\_reference
2. Not testable if returns an empty result set
3. SELECT reference\_scope FROM gpkg\_metadata\_reference WHERE
  reference\_scope NOT IN ('geopackage','table','column','row','row/col')
4. Fail if does not return an empty result set
5. Pass otherwise.

*Reference*:    Clause 2.4.3.1.2 Req 54:

*Test Type*:    Capability



**Test Case ID**: /opt/metadata/metadata\_reference/data/data\_values\_table\_name

*Test Purpose*: Verify that gpkg\_metadata\_reference table\_name column values are NULL
for rows with reference\_scope values of 'geopackage', and reference gpkg\_contents
table\_name values for all other reference\_scope values.

*Test Method*:

1. SELECT table\_name FROM gpkg\_metadata\_reference
2. Not testable if returns an empty result set
3. SELECT table\_name FROM gpkg\_metadata\_reference WHERE reference\_scope = 'geopackage'
4. Fail if result set contains any non-NULL values
5. SELECT table\_name FROM metadata\_reference WHERE reference\_scope != 'geopackage' AND table\_name NOT IN (SELECT table\_name FROM gpkg\_contents)
6. Fail if result set is not empty
7. Pass otherwise.

*Reference*:    Clause 2.4.3.1.2 Req 55:

*Test Type*:    Capability


**Test Case ID**: /opt/metadata/metadata\_reference/data/data\_values\_column\_name

*Test Purpose*: Verify that gpkg\_metadata\_reference column\_name column values are
NULL for rows with reference scope values of 'geopackage', 'table', or 'row', and contain
the name of a column in table\_name table for other reference scope values.

*Test Method*:

1. SELECT column\_name FROM gpkg\_metadata\_reference
2. Not testable if returns an empty result set
3. SELECT column\_name FROM gpkg\_metadata\_reference WHERE reference\_scope
    IN ('geopackage', 'table', 'row')
4. Fail if result set contains any non-NULL values
5. SELECT &lt;table\_name&gt;, &lt;column\_name&gt; FROM metadata\_reference WHERE
    reference\_scope NOT IN ('geopackage', 'table', 'row')
6. For each row from step 5
    - SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name = '&lt;table\_name&gt;'
    - Fail if returns an empty result set.
    - Fail if the one of the column names in the returned sql Create TABLE statement
	is not &lt;column\_name&gt;
    - Log pass otherwise
7. Pass if logged pass and no fails.

*Reference*:    Clause 2.4.3.1.2 Req 56:

*Test Type*:    Capability


**Test Case ID**: /opt/metadata/metadata\_reference/data/data\_values\_row\_id\_value

*Test Purpose*: Verify that gpkg\_metadata\_reference row\_id\_value column values are NULL
for rows with reference scope values of 'geopackage', 'table', or 'row', and contain the
ROWID of a row in the table\_name for other reference scope values.

*Test Method*:

1. SELECT row\_id\_value FROM gpkg\_metadata\_reference
2. Not testable if returns an empty result set
3. SELECT row\_id\_value FROM gpkg\_metadata\_reference WHERE reference\_scope
    IN ('geopackage', 'table', 'row')
4. Fail if result set contains any non-NULL values
5. For each SELECT &lt;table\_name&gt;, &lt;row\_id\_value&gt; FROM gpkg\_metadata\_reference
    WHERE reference\_scope NOT IN ('geopackage', 'table', 'row')
6. For each row from step 5
    - SELECT * FROM &lt;table\_name&gt; WHERE ROWID = &lt;row\_id\_value&gt;
    - Fail if result set is empty
    - Log pass otherwise
7. Pass if logged pass and no fails.

*Reference*:    Clause 2.4.3.1.2 Req 57:

*Test Type*:    Capability


**Test Case ID**: /opt/metadata/metadata\_reference/data/data\_values\_timestamp

*Test Purpose*: Verify that every gpkg\_metadata\_reference table row timestamp column
value is in ISO 8601 UTC format.

*Test Method*:

1. SELECT timestamp from gpkg\_metadata\_reference.
2. Not testable if returns an empty result set
3. For each row from step 1
    - Fail if format of returned value does not match yyyy-mm-ddThh:mm:ss.hhhZ
    - Log pass otherwise
4. Pass if logged pass and no fails.

*Reference*:    Clause 2.4.3.1.2 Req 58:

*Test Type*:    Capability


**Test Case ID**: /opt/metadata/metadata\_reference/data/data\_values\_md\_file\_id

*Test Purpose*: Verify that every gpkg\_metadata\_reference table row md\_file\_id column
value is an id column value from the gpkg\_metadata table.

*Test Method*:

1.   SELECT md\_file\_id FROM gpkg\_metadata\_reference
2.   Not testable if returns an empty result set
3.   SELECT gmr.md\_file\_id, gm.id FROM gpkg\_metadata\_reference AS gmr
4.   LEFT OUTER JOIN gpkg\_metadata gm ON gmr.md\_file\_id = gm.id
5.   Fail if result set is empty
6.   Fail if any result set gm.id values are NULL
7.   Pass otherwise

*Reference*:     Clause 2.4.3.1.2 Req 59:

*Test Type*:     Capability



**Test Case ID**: /opt/metadata/metadata\_reference/data/data\_values\_md\_parent\_id

*Test Purpose*: Verify that every gpkg\_metadata\_reference table row md\_parent\_id column
 value that is not null is an id column value from the gpkg\_metadata\_table that is not equal to
 the md\_file\_id column value for that row.

*Test Method*:

1.    SELECT md\_file\_id FROM gpkg\_metadata\_reference
2.    Not testable if returns an empty result set
3.    SELECT gmr.md\_file\_id, gmr.md\_parent\_id
4.    FROM gpkg\_metadata\_reference AS gmr
5.    WHERE gmr.md\_file\_id == gmr.md\_parent\_id
6.    Fail if result set is not empty
7.    SELECT gmr.md\_file\_id, gmr.md\_parent\_id, gm.id
8.    FROM gpkg\_metadata\_reference AS gmr
9.    LEFT OUTER JOIN gpkg\_metadata gm ON gmr.md\_parent\_id =gm.id
10.   Fail if any result set gm.id values are NULL
11.   Pass otherwise

*Reference*:     Clause 2.4.3.1.2 Req 60:

*Test Type*:     Capability

### Extension Mechanism

#### Extensions

##### Data

###### Table Definition


**Test Case ID**: /opt/extension\_mechanism/extensions/data/table\_def

*Test Purpose*: Verify that a gpkg\_extensions table exists and has the correct definition.

*Test Method*:

1. SELECT sql FROM sqlite\_master WHERE type = 'table' AND tbl\_name =
  'gpkg\_extensions'
2. Fail if returns an empty result set.
3. Pass if the column names and column definitions in the returned Create TABLE
  statement in the sql column value, including data type, nullability, default values and
  primary, foreign and unique key constraints match all of those in the contents of
  Table 23. Column order, check constraint and trigger definitions, and other column
  definitions in the returned sql are irrelevant.
4. Fail otherwise.

*Reference*:     Clause 2.6.1.1.1 Req 61:

*Test Type*:     Basic

###### Table Data Values


**Test Case ID**: /opt/extension\_metchanism/extensions/data/data\_values\_table\_name

*Test Purpose*: Verify that the table\_name column values in the gpkg\_extensions table are
 valid.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_extensions
2. Not testable if returns an empty result set
3. For each row from step one
  - Fail if table\_name value is NULL and column\_name value is not NULL.
  - SELECT DISTINCT ge.table\_name AS ge\_table, sm.tbl\_name
      FROM gpkg\_extensions AS ge LEFT OUTER JOIN sqlite\_master AS sm ON
      ge.table\_name = sm.tbl\_name
  - Log pass if every row ge.table\_name = sm.tbl\_name (MAY both be NULL).
4. Pass if logged pass and no fails.

*Reference*:    Clause 2.6.1.1.2 Req 63:

*Test Type*:    Capability



**Test Case ID**: /opt/extension\_metchanism/extensions/data/data\_values\_column\_name

*Test Purpose*: Verify that the column\_name column values in the gpkg\_extensions table are
 valid.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_extensions
2. Not testable if returns an empty result set
3. SELECT table\_name, column\_name FROM gpkg\_extensions WHERE table\_name
  IS NOT NULL AND column\_name IS NOT NULL
4. Pass if returns an empty result set
5. For each row from step 3
  - PRAGMA table\_info(table\_name)
  - Fail if gpkg\_extensions.column\_name value does not equal a name column value
      returned by PRAGMA table\_info.
  - Log pass otherwise
6. Pass if logged pass and no fails.

*Reference*:    Clause 2.6.1.1.2 Req 63:

*Test Type*:    Capability



**Test Case ID**: /opt/extension\_mechanism/extensions/data/data\_values\_extension\_name

*Test Purpose*: Verify that the extension\_name column values in the gpkg\_extensions table
 are valid.

*Test Method*:

1. SELECT extension\_name FROM gpkg\_extensions
2. Not testable if returns an empty result set
3. For each row returned from step 1
  - Log pass if extension\_name is one of those listed in Table 14
  - Separate extension\_name into &lt;author&gt; and &lt;extension&gt; at the first "\_"
  - Fail if &lt;author&gt; is "gpkg"
  - Fail if &lt;author&gt; contains characters other than [a-zA-Z0-9]
  - Fail if &lt;extension&gt; contains characters other than [a-zA-Z0-9\_]
  - Log pass otherwise
4. Pass if logged pass and no fails.

*Reference*:    Clause 2.6.1.1.2 Req 64:

*Test Type*:    Capability


#### API

##### API GeoPackage SQLite Config


**Test Case ID**: /opt/extension\_mechanism/extensions/api/api\_geopackage\_sqlite\_config

*Test Purpose*: Verify that a GeoPackage SQLite Extension has the API GeoPackage SQLite
 Configuration compile and run time options.

*Test Method*:

1.   SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_LOAD\_EXTENSION')
2.   Fail if returns 1
3.   SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_VIRTUALTABLE')
4.   Fail if returns 1
5.   SELECT sqlite\_compileoption\_used('SQLITE\_ENABLE\_RTREE\_')
6.   Fail if returns 0
7.   SELECT sqlite\_compileoption\_used('SQLITE\_RTREE\_INT\_ONLY')
8.   Fail if returns 1
9.   Pass otherwise

*Reference*:    Clause 2.6.1.2.1 Req 65:

*Test Type*:    Basic

###### Safe GeoPackage SQLite Config

**Test Case ID**: /opt/extension\_mechanism/extensions/api/safe\_geopackage\_sqlite\_config

*Test Purpose*: Verify that a GeoPackage SQLite Extension has the Safe GeoPackage
 SQLite Configuration compile and run time options.

*Test Method*:

1.   SELECT sqlite\_compileoption\_used('SQLITE\_DEFAULT\_FOREIGN\_KEYS ')
2.   Fail if returns 0
3.   SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_FOREIGN\_KEY')
4.   Fail if returns 1
5.   PRAGMA foreign\_keys
6.   Fail if returns 0
7.   SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_INTEGRITY\_CHECK')
8.   Fail if returns 1
9.    SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_SUBQUERY')
10.   Fail if returns 1
11.   SELECT sqlite\_compileoption\_used('SQLITE\_OMIT\_TRIGGER')
12.   Fail if returns 1
13.   Pass otherwise

*Reference*:     Clause 2.6.1.2.2 Req 66:

*Test Type*:     Basic

## Registered Extensions



**Test Case ID**: /reg\_ext/all/author\_name/not\_gpkg/not\_features\_or\_tiles

*Test Purpose*: Verify that any table in a GeoPackage file subject to a registered extension
 with an author\_name other than "gpkg" is not described by a gpkg\_contents table row with a
 data\_type value of 'features' or 'tiles'.

*Test Method*:

1. /opt/extension\_mechanism/extensions/data/table\_def
2. Not testable if failed
3. SELECT table\_name FROM geopackage\_contents
  WHERE data\_type IN ('features','tiles') AND table\_name IN
  (SELECT table\_name FROM gpkg\_extensions WHERE
  substr(lower(extension\_name),1,4. != 'gpkg')
4. Fail if result set is not empty
5. Pass otherwise

*Reference*:     Clause 3 Req 67:

*Test Type*:     Basic

### Features

#### Geometry Encoding

#####   Data

###### BLOB Format - Extensions Name


**Test Case ID**: /reg\_ext/features/geometry\_encoding/data/ext\_name

*Test Purpose*: Verify that an extension name in the form
 &lt;author\_name&gt;\_geometry\_encoding is defined for an author name other than "gpkg" for
 each geometry BLOB format other than GeoPackageBinary used in a GeoPackage file.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
  table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type NOT
  IN ('features', 'tiles'))
2. Not testable if returns an empty result set
3. For each row table\_name, column\_name from step 1
      * SELECT result\_set\_column\_name FROM result\_set\_table\_name
      * Not testable if returns an empty result set
      * For each geometry column value from step a
	      - If the first three bytes of geometry column value are not "GPB", then
		    + /opt/extension\_mechanism/extensions/data/table\_def
		    + Fail if failed
		    + SELECT extension\_name FROM gpkg\_extensions WERE
			table\_name = result\_set\_table\_name AND column\_name =
			result\_set\_column\_name AND
			substr(lower(extension\_name),1,4. != 'gpkg')
				* Fail if returns an empty result set
				* Separate extension\_name into &lt;author&gt; and
				  &lt;extension&gt; at the first "\_"
				* Fail if &lt;extension&gt; is not '\_geometry\_encoding'.
				* Otherwise log pass
4. Pass if logged pass and no fails

*Reference*:     Clause 3.1.1.1.2 Req 68:

*Test Type*:     Basic

###### BLOB Format - Extensions Row


**Test Case ID**: /reg\_ext/features/geometry\_encoding/data/ext\_row

*Test Purpose*: Verify that the gpkg\_extensions table contains a row with an extension\_name
 in the form &lt;author\_name&gt;\_geometry\_encoding is defined for an author name other than
 "gpkg" for each table\_name and column\_name that contain a geometry BLOB format other
 than GeoPackageBinary in a GeoPackage file.

*Test Method*:

Same as /reg\_ext/features/geometry\_encoding/data/ext\_name

*Reference*:     Clause 3.1.1.1.3 Req 69:

*Test Type*:     Capability


#### Geometry Types

#####   Data

###### Extension Types


**Test Case ID**: /reg\_ext/features/geometry\_encoding/data/extension\_types\_existing\_sparse\_data

*Test Purpose*: Verify that existing extended non-linear geometry types are stored in valid
 GeoPackageBinary format encodings.

*Test Method*:

1. SELECT table\_name FROM gpkg\_geometry\_columns
2. Not testable if returns an empty result set
3. SELECT table\_name AS tn, column\_name AS cn FROM gpkg\_geometry\_columns
  WHERE table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE
  data\_type = 'features'),
4. Fail if returns an empty result set
5. For each row from step 3 
      + SELECT cn FROM tn;
      + For each row from step a, if bytes 2-5 of cn.wkb as uint32 in endianness of
	  gc.wkb byte 1of cn from #1 are a geometry type value from Annex G Table
	  46, then
	    - Log cn.header values, wkb endianness and geometry type
	    - If cn.wkb is not correctly encoded per ISO 13249-3 clause 5.1.46 then
		  log fail
	    - If cn.flags.E is 1 - 4 and some cn.wkbx is outside of
		  cn.envelope.minx,maxx then log fail
	    - If cn.flags.E is 1 - 4 and some gc.wkby is outside of
		  cn.envelope.miny,maxy then log fail
	    -    If cn.flags.E is 2,4 and some gc.wkb.z is outside of
		  cnenvelope.minz,maxz then log fail
	    - If cn.flags.E is 3,4 and some gc.wkb.m is outside of
		  cn.envelope.minm,maxm then log fail
	    - If cn.flags.E is 5-7 then log fail
	    - Otherwise log pass
6. Log pass if log contains pass and no fails

*Reference*:     Clause 3.1.2.1.1 Req 70:

*Test Type*:     Capability


**Test Case ID**: /reg\_ext/features/geometry\_encoding/data/extension\_types\_all\_types\_test\_data

*Test Purpose*: Verify that all extended non-linear geometry types and options are stored in
 valid GeoPackageBinary format encodings.

*Test Method*:

1. Open GeoPackage that has feature geometry values of geometry type in Annex G, for
  an assortment of srs\_ids, for an assortment of coordinate values, without and with z
  and/or m values, in both big and little endian encodings:
2. /reg\_ext/features/geometry\_encoding/data/extension\_types\_existing\_sparse\_data
3. Pass if log contains pass record for big and little endian GPB headers containing big
  and little endian WKBs for 0-1 envelope contents indicator codes for every geometry
  type value from Annex G Table 47 without and with z and/or m values.
4. Fail otherwise

*Reference*:     Clause 3.1.2.1.1 Req 70:

*Test Type*:     Capability

###### Geometry Types -- Extensions Name


**Test Case ID**: /reg\_ext/features/geometry\_encoding/data/extension\_name

*Test Purpose*: Verify that an extension name in the form gpkg\_geom\_&lt;gname&gt; is defined
 for each &lt;gname&gt; extension geometry type from Annex G Table 47 used in a GeoPackage
 file.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
    table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type ==
    'features'))
2. Not testable if result set is empty
3. For each row result set table\_name, column\_name from step 3
	- SELECT result\_set\_column\_name FROM result\_set\_table\_name
	- For each geometry column value from step a
	      + If the first three bytes of each geometry column value are "GPB", then
		      * /opt/extension\_mechanism/extensions/data/table\_def
		      * Fail if failed
		      * SELECT ST\_GeometryType(geometry column value) AS lt;gtype&gt;;
		      * SELECT extension\_name FROM gpkg\_extensions WERE
			    table\_name = result\_set\_table\_name AND column\_name =
			    result\_set\_column\_name AND extension\_name = 'gpkg\_geom\_'
			    || &lt;gtype&gt;
				  - Fail if result set is empty
				  - Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 3.1.2.1.2 Req 71:

*Test Type*:     Basic

###### Geometry Types -- Extensions Row


**Test Case ID**: /reg\_ext/features/geometry\_encoding/data/extension\_row

*Test Purpose*: Verify that the gpkg\_extensions table contains a row with an extension\_name
 in the form gpkg\_geom\_&lt;gname&gt; for each table\_name and column\_name in the
 gpkg\_geometry\_columns table with a &lt;gname&gt; geometry\_type\_name.

*Test Method*:

/reg\_ext/features/geometry\_encoding/data/extension\_name


*Reference*:     Clause 3.1.2.1.3 Req 72:

*Test Type*:     Capability


#### Spatial Indexes

#####   Data

###### Spatial Indexes Implementation


**Test Case ID**: /reg\_ext/features/spatial\_indexes/implementation

*Test Purpose*: Verify the correct implementation of spatial indexes on feature table
 geometry columns.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
  table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type ==
  'features'))
2. Not testable if result set is empty
3. For each row table\_name, column\_name from step 1
      - SELECT sql FROM sqlite\_master WHERE tbl\_name = 'rtree\_' ||
	  result\_set\_table\_name || '\_' || result\_set\_column\_name
      - Not testable if result set is empty
      - Fail if returned sql != 'CREATE VIRTUAL TABLE rtree\_' ' ||
	  result\_set\_table\_name || '\_' || result\_set\_column\_name || USING rtree(id, minx,
	  maxx, miny, maxy)
      - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND tname =
	  'rtree\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name || '\_insert'
      - Fail if returned sql != result of populating insert triggers template in Table 39
	  using result\_set\_table\_name for &lt;t&gt; and result\_set\_column\_name for &lt;c&gt;
      - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND name LIKE
	  'rtree\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name || '\_update%'
      - Fail if returned sql != result of populating 4 update triggers templates in Table
	  39 using result\_set\_table\_name for &lt;t&gt; and result\_set\_column\_name for &lt;c&gt;
      - SELECT sql FROM sqlite\_master WHERE type='trigger' AND name =
	  'rtree\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name || '\_delete'
      - Fail if returned sql != result of populating delete trigger template in Table 39
	  using result\_set\_table\_name for &lt;t&gt; and result\_set\_column\_name for &lt;c&gt;
      - Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 3.1.3.1.1 Req 73:

*Test Type*:     Capability
 
###### Spatial Indexes - Extensions Name


**Test Case ID**: /reg\_ext/features/spatial\_indexes/extension\_name

*Test Purpose*: Verify that the "gpkg\_rtree\_index" extension name is used to register spatial
 index extensions.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
  table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type ==
  'features'))
2. Not testable if result set is empty
3. For each row table\_name, column\_name from step 3
      - SELECT sql FROM sqlite\_master WHERE tbl\_name = 'rtree\_' ||
	  result\_set\_table\_name || '\_' || result\_set\_column\_name
      - Not testable if returns an empty result set
      - /opt/extension\_mechanism/extensions/data/table\_def
      - Fail if failed
      - SELECT extension\_name from gpkg\_extensions WHERE table\_name =
	  result\_set\_table\_name AND column\_name = result\_set\_column\_name
      - Log pass if result is "gpkg\_rtree\_index"
      - Fail otherwise

4. Pass if logged pass and no fails

*Reference*:     Clause 3.1.3.1.2 Req 74:

*Test Type*:     Basic

###### Spatial Indexes - Extensions Row


**Test Case ID**: /reg\_ext/features/spatial\_indexes/extension\_row

*Test Purpose*: Verify that spatial index extensions are registered using the
 "gpkg\_rtree\_index" name in the gpkg\_extensions table.

*Test Method*:

/reg\_ext/features/spatial\_indexes/extension\_name


*Reference*:     Clause 3.1.3.1.3 Req 75:

*Test Type*:     Capability
 
#### Geometry Type Triggers

##### Data

###### Geometry Type Triggers Implementation


**Test Case ID**: /reg\_ext/features/geometry\_type\_triggers/implementation

*Test Purpose*: Verify that user feature data table geometry type triggers are implemented
 correctly.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
  table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type ==
  'features'))
2. Not testable if returns an empty result set
3. For each row table\_name, column\_name from step 1
      - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND tbl\_name =
	  'fgti\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name
      - Not testable if returns an empty result set
      - Fail if sql != result of populating the first trigger template in Table 17 with &lt;t&gt;
	  as result\_set\_table\_name and &lt;c&gt; as result\_set\_column\_name
      - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND tbl\_name =
	  'fgtu\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name
      - Fail if sql != result of populating the second trigger template in Table 17 with
	  &lt;t&gt; as result\_set\_table\_name and &lt;c&gt; as result\_set\_column\_name
      - Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 3.1.4.1.1 Req 76:

*Test Type*:     Capability

###### Geometry Type Triggers - Extensions Name


**Test Case ID**: /reg\_ext/features/geometry\_type\_triggers/extension\_name

*Test Purpose*: Verify that the "gpkg\_geometry\_type\_trigger" extension name is used to
 register geometry type triggers.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
  table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type ==
  'features'))
2. Not testable if result set is empty
3. For each row table\_name, column\_name from step 1
  - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND tbl\_name =
      'fgti\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name
  - Not testable if result set is empty
  - /opt/extension\_mechanism/extensions/data/table\_def
  - Fail if failed
  - SELECT extension\_name from gpkg\_extensions WHERE table\_name =
      result\_set\_table\_name AND column\_name = result\_set\_column\_name
  - Log pass if result is "gpkg\_geometry\_type\_trigger"
  - Fail otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 3.1.4.1.2 Req 77:

*Test Type*:     Basic

###### Geometry Type Triggers - Extensions Row


**Test Case ID**: /reg\_ext/features/geometry\_type\_triggers/extension\_row

*Test Purpose*: Verify that geometry type triggers are registered using the
 "gpkg\_geometry\_type\_trigger" extension name.

*Test Method*:

/reg\_ext/features/geometry\_type\_triggers/extension\_name


*Reference*:     Clause 3.1.4.1.3 Req 78:

*Test Type*:     Capability

#### SRS\_ID Triggers

#####   Data

###### SRS\_ID Triggers - Implementation


**Test Case ID**: /reg\_ext/features/srs\_id\_triggers/implementation

*Test Purpose*: Verify that user feature data table srs\_id triggers are implemented correctly.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
  table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type ==
  'features'))
2. Not testable if result set is empty
3. For each row table\_name, column\_name from step 1
      - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND tbl\_name =
	  'fgsi\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name
      - Not testable if result set is empty
      - Fail if sql != result of populating the first trigger template in Table 18 with &lt;t&gt;
	  as result\_set\_table\_name and &lt;c&gt; as result\_set\_column\_name
      - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND tbl\_name =
	  'fgsu\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name
      - Fail if sql != result of populating the second trigger template in Table 18 with
	  &lt;t&gt; as result\_set\_table\_name and &lt;c&gt; as result\_set\_column\_name
      - Log pass otherwise
4. Pass if logged pass and no fails



*Reference*:     Clause 3.1.5.1.1 Req 79:

*Test Type*:     Capability

###### SRS\_ID Triggers - Extensions Name


**Test Case ID**: /reg\_ext/features/srs\_id\_triggers/extension\_name

*Test Purpose*: Verify that the "gpkg\_srs\_id\_trigger" extension name is used to register
 srs\_id triggers.

*Test Method*:

1. SELECT table\_name, column\_name FROM gpkg\_geometry\_columns WHERE
  table\_name IN (SELECT table\_name FROM gpkg\_contents WHERE data\_type ==
  'features'))
2. Not testable if result set is empty
3. For each row table\_name, column\_name from step 1
  - SELECT sql FROM sqlite\_master WHERE type = 'trigger' AND tbl\_name =
      'fgsi\_' || result\_set\_table\_name || '\_' || result\_set\_column\_name
  - Not testable if result set is empty
  - /opt/extension\_mechanism/extensions/data/table\_def
  - Fail if failed
  - SELECT extension\_name from gpkg\_extensions WHERE table\_name =
      result\_set\_table\_name AND column\_name = result\_set\_column\_name
  - Pass if result is "gpkg\_srs\_id\_trigger"
  - Fail otherwise

*Reference*:     Clause 3.1.5.1.2 Req 80:

*Test Type*:     Basic

###### SRS\_ID Triggers - Extensions Row

**Test Case ID**: /reg\_ext/features/srs\_id\_triggers/extension\_row

*Test Purpose*: Verify that srs\_id triggers are registered using the "gpkg\_srs\_id\_trigger"
 extension name.

*Test Method*:

/reg\_ext/features/srs\_id\_triggers/extension\_name


*Reference*:     Clause 3.1.5.1.3 Req 81:

*Test Type*:     Capability

###   Tiles

#### Zoom Levels

##### Data

###### Zoom Other Intervals—Extensions Name


**Test Case ID**: /reg\_ext/tiles/zoom\_levels/data/zoom\_other\_ext\_name

*Test Purpose*: Verify that the "gpkg\_zoom\_other" extension name is used to register tiles
 tables with other than powers of two zoom intervals.

*Test Method*:

1. SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles'
2. Not testable if empty result set
3. For each row table\_name from step 1
      - SELECT zoom\_level, pixel\_x\_size, pixel\_y\_size FROM tile\_matrix\_metadata
	  WHERE table\_name = selected table name ORDER BY zoom\_level ASC
      - Not testable if returns empty result set
      - Not testable if there are not two rows with adjacent zoom levels
      - Not testable if no pair of rows for adjacent zoom levels have pixel\_x\_size or
	  pixel\_y\_size values that differ by other than powers of two
      - /opt/extension\_mechanism/extensions/data/table\_def
      - Fail if failed
      - SELECT * FROM gpkg\_extensions WHERE table\_name = selected table
	  name AND extension\_name = 'gpkg\_zoom\_other'
      - Fail if returns an empty result set
      - Log pass otherwise
4. Pass if logged pass and no fails



*Reference*:     Clause 3.2.1.1.2 Req 82:

*Test Type*:     Basic

###### Zoom Other Intervals - Extensions Row


**Test Case ID**: / reg\_ext/tiles/zoom\_levels/data/zoom\_other\_ext\_row

*Test Purpose*: Verify that tiles tables with other than powers of two zoom intervals are
 registered using the "gpkg\_zoom\_other" extension name.

*Test Method*:

/reg\_ext/tiles/zoom\_levels/data/zoom\_other\_ext\_name


*Reference*:     Clause 3.2.1.1.3 Req 83:

*Test Type*:     Capabilty

#### Tile Encoding WEBP

#####    Data

###### WEBP - Extensions Name


**Test Case ID**: /reg\_ext/tiles/tile\_encoding\_webp/data/webp\_ext\_name

*Test Purpose*: Verify that the "gpkg\_webp" extensions name is used to register WEBP tile
 encoding implementations.

*Test Method*:

1. SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles'
2. Not testable if empty result set
3. For each row table\_name from step 1
      - Select tile\_data FROM row table\_name
      - For each row tile\_data from step a
	      + Log webp if tile data in MIME type image/webp
      - Not testable if no logged webps
      - /opt/extension\_mechanism/extensions/data/table\_def
      - Fail if failed
      - SELECT * FROM gpkg\_extensions WHERE table\_name = selected table
	  name AND extension\_name = 'gpkg\_webp'
      - Fail if returns an empty result set
      - Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 3.2.2.2.1 Req 84:

*Test Type*:     Basic

##### WEBP - Extensions Row


**Test Case ID**: /reg\_ext/tiles/tile\_encoding\_webp/data/webp\_ext\_row

*Test Purpose*: Verify that WEBP tile encodings are registered using the "gpkg\_webp"
 extensions name.

*Test Method*:

/reg\_ext/tiles/tile\_encoding\_webp/data/webp\_ext\_name


*Reference*:     Clause 3.2.2.2.2 Req 85:

*Test Type*:     Capability

#### Tile Encoding TIFF

##### Data

###### TIFF - Extensions Name


**Test Case ID**: /reg\_ext/tiles/tile\_encoding\_tiff/data/tiff\_ext\_name

*Test Purpose*: Verify that the "gpkg\_tiff" extensions name is used to register TIFF tile
 encoding implementations.

*Test Method*:

1. SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles'
2. Not testable if empty result set
3. For each row table\_name from step 3
      - Select tile\_data FROM row table\_name
      - For each row tile\_data from step a
	      + Log tiff if tile data in MIME type image/tiff
      - Not testable if no logged webps
      - /opt/extension\_mechanism/extensions/data/table\_def
      - Fail if failed
      - SELECT * FROM gpkg\_extensions WHERE table\_name = selected table
	  name AND extension\_name = 'gpkg\_tiff'
      - Fail if returns an empty result set
      - Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 3.2.3.1.2 Req 86:

*Test Type*:     Basic

###### TIFF - Extensions Row


**Test Case ID**: /reg\_ext/tiles/tile\_encoding\_tiff/data/tiff\_ext\_row

*Test Purpose*: Verify that TIFF tile encodings are registered using the "gpkg\_tiff"
 extensions name.

*Test Method*:

/reg\_ext/tiles/tile\_encoding\_tiff/data/tiff\_ext\_name


*Reference*:     Clause 3.2.3.1.3 Req 87:

*Test Type*:     Capability

#### Tile Encoding NITF

##### Data

###### NITF - Extensions Name


**Test Case ID**: /reg\_ext/tiles/tile\_encoding\_nitf/data/nitf\_ext\_name

*Test Purpose*: Verify that the "gpkg\_nitf" extensions name is used to register NITF tile
 encoding implementations.

*Test Method*:

1. SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles'
2. Not testable if empty result set
3. For each row table\_name from step 3
      - Select tile\_data FROM row table\_name
      - For each row tile\_data from step a
	      + Log nitf if tile data in MIME type application/vnd.NITF
      - Not testable if no logged webps
      - /opt/extension\_mechanism/extensions/data/table\_def
      - Fail if failed
      - SELECT * FROM gpkg\_extensions WHERE table\_name = selected table
	  name AND extension\_name = 'gpkg\_nitf'
      - Fail if returns an empty result set
      - Log pass otherwise
4. Pass if logged pass and no fails

*Reference*:     Clause 3.2.4.1.2 Req 88:

*Test Type*:     Basic

###### NITF - Extensions Row


**Test Case ID**: /reg\_ext/tiles/tile\_encoding/nitf/data/nitf\_ext\_row

*Test Purpose*: Verify that NITF tile encodings are registered in the gpkg\_extensions table
 using the "gpkg\_nitf" extensions name.

*Test Method*:

/reg\_ext/tiles/tile\_encoding\_nitf/data/nitf\_ext\_name


*Reference*:     Clause 3.2.4.1.3 Req 89:

*Test Type*:     Capability

#### Tile Encoding Other

##### Data

###### Other Mime Type - Extensions Name


**Test Case ID**: /reg\_ext/tiles/tile\_encoding/other/data/other\_ext\_name

*Test Purpose*: Verify that an extension name in the form
 &lt;author\_name&gt;\_&lt;other&gt;\_mime\_type is defined for an author name other than "gpkg" for
 each other MIME image format used for tile\_data columns in tile matrix set user data tables,
 where &lt;other&gt; is replaced by the other MIME type abbreviation in uppercase.

*Test Method*:

1. SELECT table\_name FROM geopackage\_contents WHERE data\_type = 'tiles'
2. Not testable if empty result set
3. For each row table\_name from step 3
      + Select tile\_data FROM row table\_name
      + For each row tile\_data from step a
		- Log other MIME type name if tile data not in MIME type png, jpeg, webp, tiff or nitf
      + Not testable if no logged others
      + /opt/extension\_mechanism/extensions/data/table\_def
      + Fail if failed
      + For each other logged MIME type name for this table\_name
		- SELECT extension\_name FROM gpkg\_extensions WHERE
		    table\_name = result set table name AND column\_name = 'tile\_data'
		    AND substr(lower(extension\_name),1,4. !- 'gpkg') AND
		    instr(extension\_name, logged MIME type name) != 0
		- Fail if returns an empty result set
	        - Separate extension\_name into &lt;author&gt; and &lt;extension&gt; at the first "\_"
	        - Separate &lt;extension&gt; into &lt;mime&gt; and &lt;ext&gt; at the first "\_"
		- Fail if &lt;mime&gt; not logged MIME type
	        - Fail if &lt;ext&gt; not "mime\_type"
	        - Log pass otherwise
4. Pass if logged pass and no fails"

*Reference*:     Clause 3.2.5.1.2 Req 90:

*Test Type*:     Basic

###### Other Mime Type - Extensions Row


**Test Case ID**: /reg\_ext/tiles\_tile\_encoding/other/data/other\_ext\_row

*Test Purpose*: Verify that other mime image type tile encodings are registered in the
 gpkg\_extensions table using names of the form &lt;author\_name&gt;\_&lt;other&gt;\_mime\_type.

*Test Method*:

/reg\_ext/tiles/tile\_encoding/other/data/other\_ext\_name


*Reference*:    Clause 3.2.5.1.3 Req 91:

*Test Type*:    Capability

### Any Tables

#### Other Trigger

##### Data

###### Other Trigger - Extensions Name


**Test Case ID**: /reg\_ext/any/other\_triggers/data/ext\_name

*Test Purpose*: Verify that an extension name in the form &lt;author\_name&gt;\_&lt;extension&gt; is
 defined for an author name other than "gpkg" for each other trigger implementation that
 uses SQL functions other than those provided by SQLite or the GeoPackage Minimal
 Runtime SQL Functions.

*Test Method*:

1. SELECT sql, tbl\_name FROM sqlite\_master WHERE type='trigger'
2. For each row sql, tbl\_name from step 1
      - If sql contains an SQL function other than those provided by SQLite or the
	  GeoPackage Minimal Runtime SQL Functions
		+ Log trigger
	        + /opt/extension\_mechanism/extensions/data/table\_def
	        + Fail if failed
	        + SELECT extension\_name FROM gpkg\_extensions WHERE
		  table\_name = tbl\_name AND substr(lower(extension\_name),1,4. !-
		  'gpkg')
	        + Fail if returns an empty result set
	        + Log pass otherwise
3. Not testable if no logged triggers
4. Pass if logged pass and no fails

*Reference*:    Clause 3.3.1.1.2 Req 92:

*Test Type*:    Basic

###### Other Trigger - Extensions Row

**Test Case ID**: /reg\_ext/any/other\_triggers/data/ext\_row

*Test Purpose*: Verify that other trigger implementations that use SQL functions other than
 those provided by SQLite or the GeoPackage Minimal Runtime SQL Functions.are
 registered with &lt;author\_name&gt;\_&lt;extension&gt; names in the gpkg\_extensions table.

*Test Method*:

/reg\_ext/any/other\_triggers/data/ext\_name


*Reference*:    Clause 3.3.1.1.3 Req 93:

*Test Type*:   Capability
