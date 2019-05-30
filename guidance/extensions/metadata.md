_Go [back](../getting-started.md)_

### [Metadata](http://www.geopackage.org/spec120/#extension_metadata)
This extension provides a means to store metadata in a GeoPackage and to relate it to content already in the GeoPackage. 

#### `gpkg_extensions`
To use this extension, add the following rows to this table.

| *table_name* | *column_name* | *extension_name* | *definition* | *scope* |
| ------------ | ------------- | ---------------- | ------------ | ------- |
| `gpkg_metadata`   | NULL  | `gpkg_metadata`   | http://www.geopackage.org/spec120/#extension_metadata | _read-write_  |
| `gpkg_metadata_reference`   | NULL  | `gpkg_metadata`   | http://www.geopackage.org/spec120/#extension_metadata | _read-write_  |

#### `gpkg_metadata`
Add a row to this table for each metadata document.

| Column        | Value       |
| ------------- |-------------|
| `id`  | primary key |
| `md_scope` | [Metadata Scope](http://www.geopackage.org/spec120/#metadata_scopes) - default "dataset" |
| `md_standard_uri` | URI reference to the metadata structure definition authority (e.g., http://metadata.ces.mil/dse/ns/GSIP/nmis/2.2.0/doc for NMIS) |
| `mime_type` | MIME encoding of metadata (e.g., text/xml)|
| `metadata` | The actual metadata document |

#### `gpkg_metadata_reference`
Add a row to this table for each GeoPackage, table, column, row, or row/column that has a metadata document. Multiple rows can refer to a single `gpkg_metadata` entry. It is also possible for an element (geopackage, table, column, row, or row/column) to have multiple metadata documents.

| Column        | Value       |
| ------------- |-------------|
| `reference_scope`  | one of "geopackage", "table", "column", "row", or "row/col" |
| `table_name` | _user-defined table name_ (or NULL for whole GeoPackage)|
| `column_name` | for `reference_scope` of "column" or "row/col", _column name in user-defined table_ (NULL otherwise) |
| `row_id_value` | for `reference_scope` of "row" or "row/col", the row ID (NULL otherwise) |
| `timestamp` | timestamp value in ISO 8601 format |
| `md_file_id` | Foreign key to `gpkg_metadata` |
| `md_parent_id` | Foreign key to the parent metadata document (if applicable, NULL otherwise) |

