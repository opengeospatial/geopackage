_Go [back](../getting-started.md)_

### [Tiled Gridded Coverage Data](http://docs.opengeospatial.org/is/17-066r1/17-066r1.html)
The "GeoPackage Extension for Tiled Gridded Coverage Data” extension (previously titled Elevation Extension) defines how to encode and store tiled regular gridded data, such as a digital elevation model, in a GeoPackage. The tiles contain values, such as elevation, temperature or pressure, and are stored in one of two encodings:
* The PNG encoding uses PNG files to store 16-bit integer values and a scale and offset may be applied to fine-tune the coverage range.
* The TIFF encoding uses TIFF files to support 32-bit floating point data. To simplify development, this encoding constrains many of the TIFF options to the minimal set needed to meet the floating-point requirement.

#### [`gpkg_extensions`](http://docs.opengeospatial.org/is/17-066r1/17-066r1.html#gpkg_extensions)
To use this extension, add the following rows to this table.

| *table_name* | *column_name* | *extension_name* | *definition* | *scope* |
| ------------ | ------------- | ---------------- | ------------ | ------- |
| `gpkg_2d_gridded_coverage_ancillary`   | NULL  | `gpkg_2d_gridded_coverage`   | http://docs.opengeospatial.org/is/17-066r1/17-066r1.html | _read-write_  |
| `gpkg_2d_gridded_tile_ancillary`   | NULL  | `gpkg_2d_gridded_coverage`   | http://docs.opengeospatial.org/is/17-066r1/17-066r1.html | _read-write_  |
| _tile pyramid user data table name_   | `tile_data`  | `gpkg_2d_gridded_coverage`   | http://docs.opengeospatial.org/is/17-066r1/17-066r1.html | _read-write_  |

#### [`gpkg_contents`](http://docs.opengeospatial.org/is/17-066r1/17-066r1.html#gpkg_contents)
Like any other content type, add a row for each coverage, using a `data_type` of "2d-gridded-coverage".

#### [`gpkg_spatial_ref_sys`](http://docs.opengeospatial.org/is/17-066r1/17-066r1.html#gpkg_spatial_ref_sys)
Like any other content type, the CRS for your contents must be registered in this table. A GeoPackage complying with this extension must have an entry for EPSG::4979 (WGS-84 with height above ellipsoid), but use of this SRS is not required.

#### [`gpkg_2d_gridded_coverage_ancillary`](http://docs.opengeospatial.org/is/17-066r1/17-066r1.html#coverage-ancillary)
Add a row to this table for each coverage.

| Column        | Value           |
| ------------- |-------------|
| `id`  | primary key |
| `tile_matrix_set_name` | _tile pyramid user data table name_ |
| `datatype` | "integer" or "float" |
| `scale`* | Scale as a multiple relative to the unit of measure (Default 1) |
| `offset`* | The offset to the 0 value (Default 0) |
| `precision` | The smallest value that has meaning for this dataset |
| `data_null` | The value that indicates NULL |
| `grid_cell_encoding` | "grid-value-is-center" (default), "grid-value-is-area", or "grid-value-is-corner" |
| `uom` | Units of Measure for values in the grid coverage (see [UCUM](http://unitsofmeasure.org/ucum.html)) |
| `field_name` | Type of Gridded coverage data (default is "Height") |
| `quantity_definition` | Description of the values contained in the gridded overage (default is "Height") |
\* Only used for "integer" datatype

#### [`gpkg_2d_gridded_tile_ancillary`](http://docs.opengeospatial.org/is/17-066r1/17-066r1.html#_tile_ancillary)
Add a row to this table for each tile for each coverage.

| Column        | Value           |
| ------------- |-------------|
| `id`  | primary key |
| `tpudt_name` | _tile pyramid user data table name_ |
| `tpudt_id` | Foreign key to `id` in _tile pyramid user data table_ |
| `scale`* | Scale as a multiple relative to the unit of measure (Default 1) |
| `offset`* | The offset to the 0 valuet (Default 0) |
| `min`** | Minimum value of this tile |
| `max`** | Maximum value of this tile |
| `mean`** | The arithmetic mean of values in this tile |
| `std_dev`** | The standard deviation of values in this tile |
\* Only used for "integer" datatype

\*\* These values are natural, not scaled or offset

#### Using Scale and Offset
Integer values may be scaled and offset in order to make more efficient use of 16-bit integer space available in PNG files. The scale and offset may be applied to the entire coverage and/or the individual tile. The scale and offset do not apply to the `data_null` value.

Actual cell values are be calculated by:
1. multiplying the stored value by the gpkg_2d_gridded_tile_ancillary_table.scale value and then adding the gpkg_2d_gridded_tile_ancillary_table.offset,
2. multiplying that value by the gpkg_2d_gridded_coverage_ancillary.scale value and then adding the gpkg_2d_gridded_coverage_ancillary.offset.

In pseudo-code, this conversion would look like:

```
elevationInUnitOfMeasure = (SomeGrid_RegularCoverage.tile_data→pngpixels[i] *
   gpkg_2d_gridded_tile_ancillary.scale + gpkg_2d_gridded_tile_ancillary.offset) *
   gpkg_2d_gridded_coverage_ancillary.scale + gpkg_2d_gridded_coverage_ancillary.offset;
```

#### PNG Encoding
Encode integer data using the PNG format. Pixel values are 16-bit unsigned integer (single channel - "greyscale").

#### TIFF Encoding
Encode floating point data using the TIFF format.
Tiles are encoded as a single-band image using one 32-bit floating point component per pixel.
Each TIFF encoded tile is a baseline TIFF as defined in the Part 1 of the TIFF standard. 

This implies a number of constraints which are listed below:
* Only one band per TIFF tile, i.e., for any pixel in the TIFF tile, there SHALL be only one component
* All pixels in the tile SHALL be set with a valid component value
* Other TIFF tags are derived from the other constraints in this extension
* No multi-image/tiling extensions

The only allowed encoding extensions are:
* IEEE floating point
* LZW compression

