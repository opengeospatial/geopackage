### GeoPackage Implementation Guide
The purpose of this guide is present a set of capabilities that could be implemented through GeoPackage software. 
While the GeoPackage Encoding Standard does not specify client requirements, there are certain expectations that the developers of the standard had when it was developed.
Where possible, the guidelines are presented in a _tiered_ approach using multiple _capability levels_. Capability Level 0 indicates a fair and reasonable use of GeoPackage for closed scenarios but that will not provide interoperability with other use cases or applications and therefore falls short of what can be considered compliant. Capability Level 1 indicates the minimum level of interoperability and compliance and the levels increase from there. Capability Level 3 generally indicates the long-term vision for GeoPackage compliance.

This approach allows developers to develop their software incrementally, achieving useful capabilities at a pace aligned with their own roadmaps and business models.
The approach also gives guidance back to the SWG – some capability levels are not achievable today and these should be given highest priority in future SWG activities.

### Contents
The `gpkg_contents` table lists the contents that are available in a GeoPackage. A client should use this table to determine what content to load.

###### Level 0
Load and utilize one or more sets of contents (tiles or features) using hard-coded table names.

###### Level 1
Load and utilize a single set of contents (tiles or features) by picking the first item in `gpkg_contents`.

###### Level 2
Load the contents from `gpkg_contents`, present the user a list of contents to utilize, and allow the user to open one or more of them.

###### Level 3
Load a list of OWS Context files, each representing a specific use case or scenario, and allow the user to select one for use.

> Note: The specification for this capability is still being developed.

### Spatial Reference System (SRS)
The `gpkg_spatial_ref_sys` table lists the SRSs that are in use in a GeoPackage. 

###### Level 0
GeoPackage contents are utilized without recognition of SRSs.

###### Level 1
GeoPackage software supports the default SRSs of EPSG::4326 (WGS-84), 0 (undefined geographic coordinate reference systems), and -1 (undefined Cartesian coordinate reference systems).

###### Level 2
GeoPackage software supports arbitrary SRSs that are listed in `gpkg_spatial_ref_sys`. The software performs any transformations needed if multiple SRSs are in use at the same time.

###### Level 3
GeoPackage software supports arbitrary SRSs that are encoded in [CRS WKT2](http://docs.opengeospatial.org/is/12-063r5/12-063r5.html), using the [WKT for CRS Extension](extensions/wkt_for_crs.md).

### Features
The actual utilization of feature data is very open-ended. Many systems visualize feature data, but feature data is also well-suited to a number of analysis operations.

#### Geometries

###### Level 0
GeoPackage software supports at least one simple geometry type (point, line, or polygon).

###### Level 1
GeoPackage software supports all "simple features" primitive geometry types (point, line, polygon, multipoint, multiline, and multipolygon).

###### Level 2
GeoPackage software supports geometry collections of arbitrary size and complexity. It also supports 3D and 4D geometries using the Z and M coordinates. GeoPackage writing software also supports the [RTree Spatial Index Extension](extensions/rtree_spatial_indexes.md) and uses this extension to improve spatial querying performance.

###### Level 3
GeoPackage software supports extended geometry types using the [Nonlinear Geometry Types Extension](extensions/nonlinear_geometry_types.md).

#### Attributes of Feature Tables

###### Level 0
GeoPackage software supports hard-coded attributes.

###### Level 1
GeoPackage software supports arbitrary attributes of any name and [supported data type](http://www.geopackage.org/spec120/#table_column_data_types).

###### Level 2
GeoPackage software supports arbitrary attributes that are defined using the [Schema Extension](extensions/schema.md). Where appropriate, the schema defines metadata that improves the readability of visualizations and query results.

#### Feature Visualization

### Attributes
Attributes tables are non-spatial data that may be joined as part of a view. This eliminates a potential source of redundancy and bloat in GeoPackage files.

###### Level 1
GeoPackage-writing software creates views to join feature tables and attribute tables. (GeoPackage clients are then able to utilize these views as they would a table, but only in a read-only mode.)

###### Level 2
GeoPackage-writing software uses the ["updatable view" technique](https://www.sqlite.org/lang_createtrigger.html#instead_of_trigger) to produce updatable views that combine the flexibility of joining multiple tables together with the insert/update/delete capabilities of a table. (GeoPackage clients are then able to utilize these views as they would a table.)

> NOTE: While this capability is possible today, there is currently not clear guidance on how this should be done.

###### Level 3
GeoPackage software supports many-to-many relationships between features and attributes using the Related Tables Extension.

> NOTE: This capability is still under development.

### Tiles
Tiled raster data is primarily designed for visualization purposes.

#### Tile Matrix Sets

###### Level 0
GeoPackage software supports a hard-coded tile matrix set. 

###### Level 1
GeoPackage software supports the Google Maps-compatible Tile Matrix Set. 

###### Level 2
GeoPackage software supports any tile matrix set that has a power-of-2 interval between zoom levels.

###### Level 3
GeoPackage software supports tile matrix sets with arbitrary zoom levels using the [Zoom Other Intervals](extensions/zoom_other_intervals.md) extension. When useful, this extension is used to preserve the quality of the highest zoom level and minimize the bloat of the GeoPackage.

#### Tile Encoding

###### Level 1
GeoPackage software supports PNG and JPG tiles.

###### Level 2
GeoPackage-writing software produces heterogeneous tile sets for imagery overlays, using JPG files (with their superior compression) for central tiles and PNG (with alpha channel transparency) for border tiles so that the user is able to see the underlying layers at the edge of the imagery coverage area.

###### Level 3
GeoPackage software supports the WebP format using the [Tiles Encoding WebP Extension](extensions/tiles_encoding_webp.md). GeoPackage producers use this format to reduce GeoPackage size when the expected clients are known to support it.

#### Tile Visualization
###### Level 0
A GeoPackage client can render a fixed view of tiled raster data.

###### Level 1
A GeoPackage client can display the raster data (centered on the extents specified in the corresponding row of `gpkg_contents`), pan, switch zoom levels, and zoom to global extent.

###### Level 2
A GeoPackage client can display multiple tile matrix sets simultaneously, transforming into a single SRS if needed.

###### Level 3
When a GeoPackage is loaded for visualization via an OWS Context (see above), the default view is read from the Context.

> Note: The specification for this capability is still being developed.


