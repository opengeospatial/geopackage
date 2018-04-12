_Go [back](../getting-started.md)_

### [Nonlinear Geometry Types Extension](http://www.geopackage.org/spec120/#extension_geometry_types)
This extension allows the use of [extended geometry types](http://www.geopackage.org/spec120/#geometry_types_extension). 

#### `gpkg_extensions`
Add a row to this table for each geometry type in use

| Column        | Value           |
| ------------- |-------------|
| `table_name`  | _table containing extended geometry_ |
| `column_name` | _column containing extended geometry_ |
| `extension_name` | `gpkg_geom_<gname>` where `<gname>` is the uppercase name of the extended geometry type |
| `definition`  | http://www.geopackage.org/spec120/#extension_geometry_types |
| `scope`   | _read-write_  |

#### Features tables
When using this extension, use the appropriate type code in the geometry type byte of the geometry. The `X` bit is _0_ (an `X` bit of _1_ only applies when using the now-deprecated [User Defined Geometry Types Extension of GeoPackageBinary Geometry Encoding](http://www.geopackage.org/spec110/#extension_geometry_encoding)).