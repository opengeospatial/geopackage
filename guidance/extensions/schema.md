### [Schema](http://www.geopackage.org/spec120/#extension_schema)
This extension provides a means to describe the columns of tables in a GeoPackage with more detail than can be captured by the SQL table definition directly. The information provided by this extension can be used by applications to, for instance, present data contained in a GeoPackage in a more user-friendly fashion or implement data validation logic. The extension was originally designed to describe the schema of _features_ but it could apply to any user-defined table with user-defined columns. 

#### `gpkg_extensions`
To use this extension, add the following rows to this table.

| *table_name* | *column_name* | *extension_name* | *definition* | *scope* |
| ------------ | ------------- | ---------------- | ------------ | ------- |
| `gpkg_data_columns`   | NULL  | `gpkg_schema`   | http://www.geopackage.org/spec120/#extension_schema | _read-write_  |
| `gpkg_data_column_constraints`   | NULL  | `gpkg_schema`   | http://www.geopackage.org/spec120/#extension_schema | _read-write_  |

#### `gpkg_data_columns`
Add a row to this table for each column that needs to be further described.

| Column        | Value           |
| ------------- |-------------|
| `table_name`  | _user-defined table name_ |
| `column_name` | _user-defined column name_|
| `name` | A human-readable identifier (e.g. short name) for the column_name content |
| `title` | A human-readable formal title for the column_name content |
| `description` | A human-readable description for the column_name content |
| `mime_type` | MIME type of column_name if BLOB type, or NULL for other types |
| `constraint_name` | Column value constraint name (lowercase) specified by reference to gpkg_data_column_constraints.constraint name (see below) |


#### Using This Extension
###### Defining an Enumeration
To define an enumeration ( for a column, add one row to `gpkg_data_column_constraints` for each enumerated value as follows (other values can be NULL and are to be ignored). 

| Column        | Value           |
| ------------- |-------------|
| `constraint_name`  | Name of constraint (lowercase) |
| `constraint_type` | `enum` |
| `value` | Specified case sensitive value |
| `description` | Description of the enum value |

###### Defining a Range
To define a numeric range for an column, add one row to `gpkg_data_column_constraints` as follows (other values can be NULL and are to be ignored).

| Column        | Value           |
| ------------- |-------------|
| `constraint_name`  | Name of constraint (lowercase) |
| `constraint_type` | `range` |
| `min` | Minimum value |
| `min_is_inclusive` | 0 (false) if min value is exclusive, or 1 (true) if min value is inclusive |
| `max` | Maximum value |
| `max_is_inclusive` | 0 (false) if max value is exclusive, or 1 (true) if min value is inclusive |
| `description` | Description of the constraint |

###### Defining a GLOB
A [GLOB](https://www.sqlite.org/lang_expr.html#glob) is a pattern-matching expression. You can add a GLOB constraint for a column to constrain values to those that match the specified pattern. To do this, add one row to `gpkg_data_column_constraints` as follows:

| Column        | Value           |
| ------------- |-------------|
| `constraint_name`  | Name of constraint (lowercase) |
| `constraint_type` | `glob`|
| `value` | actual GLOB expression |
| `description` | Description of the constraint |

###### Defining a MIME Type for a BLOB
To constraint a BLOB column to a specific MIME type, set the `mime_type` column for that row in `gpkg_data_columns`. (The `constraint_name` column of `gpkg_data_columns` can be NULL and the `gpkg_data_column_constraints` table does not apply.) 

> Note: this constraint must be controlled through software – it is not possible for SQLite to control this directly.



