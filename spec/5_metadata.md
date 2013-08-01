## 2.4. Metadata

The optional capabilities defined in sub clauses and requirement statements of this clause MAY be implemented by any **GeoPackage file**.

#### 2.4.1. Introduction 

Two tables in a GeoPackage file provide a means of storing metadata in MIME
[25] encodings that are defined in accordance with any authoritative metadata specifications, and
relating it to the features, rasters, and tiles data in a GeoPackage. These tables are intended to
provide the support necessary to implement the hierarchical metadata model defined in ISO 19115
[40], Annex B B.5.25 MD_ScopeCode, Annex I and Annex J, so that as GeoPackage data is captured and
updated, the most local and specific detailed metadata changes associated with the new or modified
data MAY be captured separately, and referenced to existing global and general metadata.

The `gpkg_metadata` table that contains metadata is described in clause 2.4.2, and the
`gpkg_metadata_reference` table that relates `gpkg_metadata` to GeoPackage data is described in clause
2.4.3. There is no GeoPackage requirement that such metadata be provided or that defined metadata be
structured in a hierarchical fashion[^1] with more than one level, only that if it is, these tables
SHALL be used. Such metadata[^2] and data that relates it to GeoPackage contents SHALL NOT be stored in
other tables as defined in clause 2.5.

#### 2.4.2. Metadata Table
##### 2.4.2.1. Data
##### 2.4.2.1.1. Table Definition

> *Req 50:* A GeoPackage file MAY contain a table or updateable view named gpkg_metadata. If present it SHALL be defined per clause2.4.2.1.1, Table 10 and Table 33.

The first component of GeoPackage metadata is the `gpkg_metadata` table that MAY contain metadata in
MIME [25] encodings structured in accordance with any authoritative metadata specification, such as
ISO 19115 [40], ISO 19115-2 [B31], ISO 19139 [B32], Dublin Core [B33], CSDGM [B34], DDMS [B35],
NMF/NMIS [B36], etc. The GeoPackage interpretation of what constitutes “metadata” is a broad one
that includes UML models [B37] encoded in XMI [B38], GML Application Schemas [B39], ISO 19110
feature catalogues [B40], OWL [B41] and SKOS [B42] taxonomies, etc.

*Table 10: Metadata Table or View Definition*

|Column Name | Column Type | Column Description | Null | Default | Key |
|------------|-------------|--------------------|------|---------|-----|
| `id` | integer | Metadata primary key | no | | PK |
| `md_scope` | text | Name of the data scope to which this metadata applies; see table 11 below | no | ‘dataset’ | |
| `md_standard_uri` | text | URI reference to the metadata structure definition authority | no | http://schemas.opengis.net/iso/19139/ |
| `mime_type` | text | MIME [25] encoding of metadata | no | text/xml | |
| `metadata` | text | metadata | no | ’’ |

See Annex C: Table Definition SQL clause C.9 gpkg_metadata.

##### 2.4.2.1.2. Table Data Values

The `md_scope` column in the `gpkg_metadata` table is the name of the applicable scope for the
contents of the metadata column for a given row. The list of valid scope names and their definitions
is provided in Table 11 below. The initial contents of this table were obtained from the ISO 19115
[40], Annex B B.5.25 MD_ScopeCode code list, which was extended [^3] for use in the GeoPackage
specification by addition of entries with “NA” as the scope code column in Table 10.

*Table 11: Metadata Scopes*

| Name (md_scope) | Scope Code | Definition |
|-----------------|------------|------------|
| undefined | NA | Metadata information scope is undefined |
| fieldSession | 012 | Information applies to the field session |
| collectionSession | 004 | Information applies to the collection session | 
| series | 006 | Information applies to the (dataset) series4 | 
| dataset | 005 | Information applies to the (geographic feature) dataset |
| featureType | 010 | Information applies to a feature type (class) | 
| feature | 009 | Information applies to a feature (instance) |
| attributeType | 002 | Information applies to the attribute class |
| attribute | 001 | Information applies to the characteristic of a feature (instance) |
| tile | 016 | Information applies to a tile, a spatial subset of geographic data |
| model | 015 | Information applies to a copy or imitation of an existing or hypothetical object |
| catalog | NA | Metadata applies to a feature catalog [^5] |
| schema | NA | Metadata applies to an application schema [^6] |
| taxonomy | NA | Metadata applies to a taxonomy or knowledge system [^7] |
| software | 013 | Information applies to a computer program or routine |
| service | 014 | Information applies to a capability which a service provider entity makes available to a service user entity through a set of interfaces that define a behaviour, such as a use case |
| collectionHardware | 003 | Information applies to the collection hardware class |
| nonGeographicDataset | 007 | Information applies to non-geographic data |
| dimensionGroup | 008 | Information applies to a dimension group |

> **Req 51:** Each `md_scope` column value in a `gpkg_metadata` table or updateable view SHALL be one of the name column values from 11 in clause 2.4.2.1.2.

#### 2.4.3. Metadata Reference Table
#####2.4.3.1. Data
######2.4.3.1.1. Table Definition

> **Req 52:** A GeoPackage file that contains a gpkg_metadata table SHALL contain a gpkg_metadata_reference table per clause 2.4.3.1.1, Table 12 and Table 34.

The second component of GeoPackage metadata is the `gpkg_metadata_reference` table that links metadata in the `gpkg_metadata` table to data in the feature, and tiles tables defined in clauses 2.1.6 and 2.2.7. The `gpkg_metadata_reference` table is not required to contain any rows.

*Table 12: Metadata Reference Table or View Definition*

|Column Name | Col Type | Column Description | Null | Default | Key |
|------------|----------|--------------------|------|---------|-----|
|`reference_scope` | text | Metadata reference scope; one of ‘geopackage’, ‘table’,‘column’, ’row’, ’row/col’ | no |  |  | 
| `table_name` | text | Name of the table to which this metadata reference applies, or NULL for reference_scope of ‘geopackage’. | yes |  |  | 
| `column_name` | text | Name of the column to which this metadata reference applies; NULL for `reference_scope` of ‘geopackage’,‘table’ or ‘row’, or the name of a column in the `table_name` table for `reference_scope` of ‘column’ or ‘row/col’ | yes |  |  | 
| `row_id_value`[^8] | integer | NULL for `reference_scope` of ‘geopackage’, ‘table’ or ‘column’, or the rowed of a row record in the `table_name` table for `reference_scope` of ‘row’ or ‘row/col’ | yes |  |  | 
| `timestamp` | text | timestamp value in ISO 8601 format as defined by the strftime function '%Y-%m-%dT%H:%M:%fZ' format string applied to the current time | no | strftime('%Y-%m-%dT%H:%M:%fZ', CURRENT_TIMESTAMP) |  | 
| `md_file_id` | integer | `gpkg_metadata` table id column value for the metadata to which this `gpkg_metadata_reference` applies | no |  | FK | 
| `md_parent_id` | integer | `gpkg_metadata` table id column value for the hierarchical parent `gpkg_metadata` for the `gpkg_metadata` to which this `gpkg_metadata_reference` applies, or NULL if `md_file_id` forms the root of a metadata hierarchy | yes |  | FK | 

Every row in `gpkg_metadata_reference` that has null value as `md_parent_id` forms the root of a metadata hierarchy [^9].

See Annex C: Table Definition SQL clause C.10 `gpkg_metadata_reference`.

##### 2.4.3.1.2. Table Data Values

> **Req 53:** Every `gpkg_metadata_reference` table reference scope column value SHALL be one of ‘geopackage’, ‘table’,‘column’, ’row’, ’row/col’.

> **Req 54:** Every `gpkg_metadata_reference` table row with a `reference_scope` column value of ‘geopackage’ SHALL have a `table_name` column value that is NULL. Every other `gpkg_metadata_reference` table row SHALL have a `table_name` column value that references a value in the `gpkg_contents` `table_name` column.

> **Req 55:** Every `gpkg_metadata_reference` table row with a `reference_scope` column value of ‘geopackage’,‘table’ or ‘row’ SHALL have a `column_name` column value that is NULL. Every other `gpkg_metadata_reference` table row SHALL have a `column_name` column value that contains the name of a column in the SQLite table or view identified by the `table_name` column value.

> **Req 56:** Every `gpkg_metadata_reference` table row with a `reference_scope` column value of ‘geopackage’, ‘table’ or ‘column’ SHALL have a `row_id_value` column value that is NULL. Every other `gpkg_metadata_reference` table row SHALL have a `row_id_value` column value that contains the ROWID of a row in the SQLite table or view identified by the `table_name` column value.

> **Req 57:** Every `gpkg_metadata_reference` table row timestamp column value SHALL be in ISO 8601 [41]format containing a complete date plus UTC hours, minutes, seconds and a decimal fraction of a second, with a ‘Z’ (‘zulu’) suffix indicating UTC.[^10]

> **Req 58:** Every `gpkg_metadata_reference` table row `md_file_id` column value SHALL be an id column value from the `gpkg_metadata` table.

> **Req 59:** Every `gpkg_metadata_reference` table row `md_parent_id` column value that is NOT NULL SHALL be an id column value from the `gpkg_metadata` table that is not equal to the `md_file_id` column value for that row.

[^1]: Informative examples of hierarchical metadata are provided in Annex I. 

[^2]: An informative example of raster image metadata is provided in Annex J.

[^3]: The scope codes in Table 13 include a very wide set of descriptive information types as “metadata” to describe data.

[^4]: ISO 19139 format metadata [B32] is recommended for general-purpose description of geospatial data at the series and dataset metadata scopes.

[^5]: The “catalog” `md_scope` MAY be used for Feature Catalog [B40] information stored as XML metadata that is linked to features stored in a GeoPackage.

[^6]: The “schema” `md_scope` MAY be used for Application Schema [B37][B38][B39][B44] information stored as XML metadata that is linked to features stored in a GeoPackage.

[^7]: The “taxonomy” md_scope MAY be used for taxonomy or knowledge system [B41][B42] “linked data” information stored as XML metadata that is linked to features stored in a GeoPackage.

[^8]: In SQLite, the rowid value is always equal to the value of a single-column primary key on an integer column [B30] and is not changed by a database reorganization performed by the VACUUM SQL command.

[^9]: Such a metadata hierarchy MAY have only one level of defined metadata.

[^10]: The following statement selects an ISO 8601 timestamp value using the SQLite strftime function: `SELECT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))`.