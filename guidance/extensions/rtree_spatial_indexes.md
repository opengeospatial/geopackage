### [RTree Spatial Indexes Extension](http://www.geopackage.org/spec120/#extension_rtree)
This extension adds a new capability for spatially indexing geometry columns. This extension uses the rtree implementation provided by the [SQLite R*Tree Module extension](http://www.sqlite.org/rtree.html).

#### `gpkg_extensions`
Add a row to this table for each geometry type to be indexed.

| Column        | Value           |
| ------------- |-------------|
| `table_name`  | _table containing geometry to index_ |
| `column_name` | _column containing geometry to index_ |
| `extension_name` | `gpkg_rtree_index` |
| `definition`  | http://www.geopackage.org/spec120/#extension_rtree |
| `scope`   | _write-only_  |

#### Virtual Tables and Triggers
The spatial index is established by creating a virtual table and a set of triggers.  These are detailed in [Appendix F.3](http://www.geopackage.org/spec120/#r77).

