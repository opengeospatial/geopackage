# GeoPackage Tiles Specification Requirements

### Introduction

This document is a complementary document to the main [GeoPackage Tiles Spec] (spec.md). 
It contains all the requirements of the specification, in a single document, instead of
mixed through out the main specification. The conformance classes could also go here.

### Requirements

| Requirement Number | Type | Requirement |
|--------------------|------|-------------|
| REQ 13 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/core/tile_table_metadata_table <br/><br/> A GeoPackage SHALL include a tile_table_metadata table as defined in clause 6.5.3.1 and table 11.|
| REQ 14 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/core/tile_matrix_metadata_table <br/><br/> A GeoPackage SHALL include a tile_matrix_metadata table as defined in clause 6.3.5.2 and table 12.|
| REQ 20 | **Core** | http://www.opengis.net/spec/GPKG/1.0/req/core/tiles_table  <br/><br/> All tile matrix sets in a GeoPackage SHALL be contained in tiles tables defined as specified in clause 6.3.6.3 and table 15 and exemplified by table xx|
| REQ 21 | **Core**| http://www.opengis.net/spec/GPKG/1.0/req/core/times_two_zoom <br/><br/> A GeoPackage SHALL support tile matrix set zoom levels for pixel sizes that differ by powers of two between adjacent zoom levels.|


