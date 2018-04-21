_Go [back](../index.html)_

## GeoPackage Implementation Guide
The purpose of this guide is present a set of capabilities that could be implemented through GeoPackage software. 
While the GeoPackage Encoding Standard does not specify software requirements, there are certain expectations that GeoPackage creators had when the standard was developed.
This guide attempts to articulate those expectations so that developers produce software that is consistent with what GeoPackage creators envisioned. 
Where appropriate, the roles of GeoPackage-writing software (producers and editors) are differentiated from clients.

> NOTE: For the purposes of this guide, client operations are by definition _read-only_ even though clients may of course edit GeoPackages.
> If there is no considerable difference between reading and writing software, the generic term _GeoPackage software_ is used.

Where possible, the guidelines are presented in a _tiered_ approach using multiple _capability levels_. 
Capability Level 0 indicates a fair and reasonable use of GeoPackage for closed scenarios but that will not provide interoperability with other use cases or applications and therefore falls short of what can be considered compliant. 
Capability Level 1 indicates the minimum level of interoperability. Capability Level 2 indicates an increased level of capability and compliance and Capability Level 3 generally indicates the long-term vision for GeoPackage support.
Where possible, the guide also presents an example client operation for each capability level.
If a GeoPackage client can perform the indicated operation, it is capable of meeting this capability level.
The compliance of GeoPackage-writing software is easier to define; if it can produce a GeoPackage that can be used in place of the file referenced in the sample, then it is compliant.

This approach allows developers to develop their software incrementally, achieving useful capabilities at a pace aligned with their own roadmaps and business models.
There is no expectation that any particular piece of software support any particular capability or capability level.
Consider this more of a catalog or taxonomy for GeoPackage support capabilities, things that could be supported in GeoPackage software.

> Note: This approach also gives guidance back to the SWG – some capability levels are not achievable today and these should be given highest priority in future SWG activities.

### Contents
GeoPackages are self-describing and GeoPackage software should use this feature of the format to express (for GeoPackage-writing software) and determine (for clients) what content to load.

###### Level 0
GeoPackage client loads and utilize one or more sets of contents (tiles or features) using hard-coded table names.

###### Level 1
GeoPackage client loads and utilizes a single set of contents (tiles or features) by picking the first item in `gpkg_contents`.

> Example (tiles): 
> 
> Open https://portal.opengeospatial.org/files/?artifact_id=74983.
> 
> Client loads the tiles without interaction with the user.

###### Level 2
GeoPackage client loads the contents from `gpkg_contents`, presents the user a list of contents to utilize, and allows the user to open one or more of them.

> Example: 
> 
> Open https://portal.opengeospatial.org/files/?artifact_id=74984
> 
> Client presents a list with two contents (one tiles, one feature).
>
> User can select one or both contents for use.

###### Level 3
GeoPackage client loads a list of OWS Context files, each representing a specific use case or scenario, and allows the user to select one for use.

> NOTE: The specification for this capability is still being developed.

### Spatial Reference System (SRS)
GeoPackages are expected to use SRSs to ensure the consistency of coordinates.

###### Level 0
GeoPackage contents are utilized without recognition of SRSs.

###### Level 1
GeoPackage software supports the three SRSs of EPSG::4326 (WGS-84), 0 (undefined geographic coordinate reference systems), and -1 (undefined Cartesian coordinate reference systems) that are listed by default in the `gpkg_spatial_ref_sys` table.

> Example: 
> 
> Open https://portal.opengeospatial.org/files/?artifact_id=74984.
> 
> This GeoPackage contains tiles and features, both in EPSG::4326. The client should be able to use these contents normally.

###### Level 2
GeoPackage software supports arbitrary SRSs that are listed in `gpkg_spatial_ref_sys`. The software performs any transformations needed if multiple SRSs are in use at the same time.

> Example 1 (features):
> 
> Open http://www.geopackage.org/data/sample1_2.gpkg.
> 
> This GeoPackage contains features in different SRSs. The client should be able to use these contents normally.

###### Level 3
GeoPackage software supports arbitrary SRSs that are encoded in [CRS WKT2](http://docs.opengeospatial.org/is/12-063r5/12-063r5.html), using the [WKT for CRS Extension](extensions/wkt_for_crs.md).

> Example 1 (features):
> 
> Open http://www.geopackage.org/data/sample1_2F10.gpkg.
> 
> This GeoPackage contains features in different SRSs encoded using CRS WKT2. The client should be able to use these contents normally.

### Features
The actual utilization of feature data is very open-ended. Many systems visualize feature data, but feature data is also well-suited to a number of analysis operations.

#### Geometries

###### Level 0
GeoPackage software supports at least one simple geometry type (point, line, or polygon).

###### Level 1
GeoPackage software supports all six "simple features" primitive geometry types (point, line, polygon, multipoint, multiline, and multipolygon).

> Example:
> 
> Open http://www.geopackage.org/data/sample1_2.gpkg.
> 
> The client should be able to handle all of the 2D features (point2d, linestring2d, etc.) in this GeoPackage.

###### Level 2
GeoPackage software supports geometry collections (of arbitrary size and complexity) and generic geometries. It also supports 3D and 4D geometries using the Z and M coordinates. GeoPackage-writing software also supports the [RTree Spatial Index Extension](extensions/rtree_spatial_indexes.md) and uses this extension to improve spatial querying performance for clients.

> Example:
> 
> Open http://www.geopackage.org/data/sample1_2.gpkg.
> 
> The client should be able to handle all of the features in this GeoPackage.

###### Level 3
GeoPackage software supports extended geometry types using the [Nonlinear Geometry Types Extension](extensions/nonlinear_geometry_types.md).

> Example:
> 
> Open http://www.geopackage.org/data/gdal_sample_v1.2_spi_nonlinear_webp_elevation.gpkg.
> 
> The client should be able to handle all of the features in this GeoPackage.

#### Attributes of Feature Data

###### Level 0
GeoPackage software supports hard-coded attributes.

###### Level 1
GeoPackage software supports arbitrary attributes of any name and [supported data type](http://www.geopackage.org/spec120/#table_column_data_types). GeoPackage clients read these attributes from the user-defined feature table and present them to the user or utilize them where appropriate.

> Example:
> 
> Open http://www.geopackage.org/data/sample1_2.gpkg.
> 
> The client should be able to use all of the attributes on the features and their attributes in the "counties" layer.

###### Level 2
GeoPackage software supports arbitrary attributes that are defined using the [Schema Extension](extensions/schema.md). Where appropriate, the schema defines metadata that improves the readability of visualizations and query results.

> NOTE: There is currently no example available at this time.

#### Feature Visualization
Not all GeoPackage clients visualize feature data, but those that do must consider how the styles (portrayal rules) are produced and selected by the user.

###### Level 1
Feature geometries and/or attributes are visualized using hard-coded styling rules.

> Example: 
> 
> Open https://portal.opengeospatial.org/files/?artifact_id=74984 and select the vegetation layer.
> 
> The client then renders the features using hard-coded styling rules.

###### Level 2
Feature geometries and/or attributes are styled through the GeoPackage client using styling rules that are provided by the client or defined by the user through the client. 

> Example: 
> 
> Open https://portal.opengeospatial.org/files/?artifact_id=74984 and select the vegetation layer.
> 
> The client asks the user to select a styling rules set or to create one.
>
> The client then renders the features using the selected styling rules.

###### Level 3
Feature styles are encoded as part of Contexts (see above) that are included as part of the GeoPackage.

> NOTE: This capability is still under development.

### Attributes
Attributes tables are non-spatial data that may be joined as part of a view. This eliminates a potential source of redundancy and bloat in GeoPackage files.

###### Level 0
Attribute information is duplicated across multiple feature tables instead of being stored in a separate attributes table.

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

> Example:
> 
> Load the "rivers_tiles" tile pyramid from http://geopackage.org/data/rivers.gpkg. 
> Zoom levels 1-6 should be available.

###### Level 2
GeoPackage software supports any tile matrix set that has a power-of-2 interval between zoom levels.

> Example:
> 
> Load the "MGCPPREVIEW5SKU" tile pyramid from https://portal.opengeospatial.org/files/?artifact_id=74863.
>
> Zoom levels 9-16 should be available.

###### Level 3
GeoPackage software supports tile matrix sets with arbitrary zoom levels using the [Zoom Other Intervals](extensions/zoom_other_intervals.md) extension. When useful, this extension is used to preserve the quality of the highest zoom level and minimize the bloat of the GeoPackage.

> NOTE: There is currently no example available at this time.

#### Tile Encoding

###### Level 1
GeoPackage software supports PNG and JPG tiles.

> NOTE: Client support for JPG and PNG is so ubiquitous that it is unlikely that a visualization client would not be able to display either.

###### Level 2
GeoPackage-writing software produces heterogeneous tile sets for imagery overlays, using JPG files (with their superior compression) for central tiles and PNG (with alpha channel transparency) for border tiles so that the user is able to see the underlying layers at the edge of the imagery coverage area.

> NOTE: Because of the aforementioned ubiquity of PNG and JPG support, this is more of a challenge for GeoPackage-writing software.

###### Level 3
GeoPackage software supports the WebP format using the [Tiles Encoding WebP Extension](extensions/tiles_encoding_webp.md). GeoPackage-writing software uses this format to reduce GeoPackage size when the expected clients are known to support it.

> Example:
> 
> Load the "byte_webp" tile pyramid from http://www.geopackage.org/data/gdal_sample_v1.2_spi_nonlinear_webp_elevation.gpkg.
>
> A single tile should be available.

#### Tile Visualization
This section applies to generic map capabilities of a GeoPackage client.

###### Level 0
A GeoPackage client can render a fixed view of tiled raster data.

###### Level 1
A GeoPackage client can display the raster data (centered on the extents specified in the corresponding row of `gpkg_contents`), pan, switch zoom levels, and zoom to global extent.

> NOTE:  Any tiles example could be used to demonstrate the desired behavior.

###### Level 2
A GeoPackage client can display multiple tile matrix sets simultaneously, transforming into a single SRS if needed.

> NOTE: There is currently no example available at this time.

###### Level 3
When a GeoPackage is loaded for visualization via an OWS Context (see above), the default view is read from the Context.

> Note: The specification for this capability is still being developed.

### Metadata
###### Level 1
GeoPackage-writing software fully populates the `gpkg_contents` table for each set of contents and GeoPackage clients present this information to the user.

> NOTE:  Any compliant GeoPackage could be used to demonstrate the desired behavior.

###### Level 2
GeoPackage software supports the [Metadata Extension](extensions/metadata.md). GeoPackage-writing software populates the two metadata tables with information regarding each dataset and GeoPackage clients make this metadata available to the user upon request. 

> Example:
> 
> Load 
https://portal.opengeospatial.org/files/?artifact_id=74984.
>
> There is metadata for the whole GeoPackage and for the "Veg_DC" layer.

-----------

> NOTE: There are a number of metadata formats available. Support or conformance to these formats is outside the scope of this document.


###### Level 3
GeoPackage software supports hierarchical metadata in conjunction with the [Metadata Extension](extensions/metadata.md). Metadata is traceable from the tile or feature level up to the GeoPackage level.

> NOTE: There is currently no example available at this time.

