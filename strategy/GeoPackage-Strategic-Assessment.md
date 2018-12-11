This document identifies GeoPackage-related capabilities, how well we are doing at achieving those capabilities, and what activities will help us attain them. Ideally this document will help us to identify the highest priority items for future investment. We intend to maintain the document continuously so that it will continue to remain relevant.

---

## Encoding Standard 
Generally believed to be in good shape, but regular maintenance continues to be needed.
### 1.2.1
* [x] GitHub Version
* [x] Release Notes
* [x] SWG Motion
* [x] TC Vote
* [x] [Publication](http://www.geopackage.org/spec121/)
* [ ] Press release - none was issued

### 1.3.0
* [ ] Issues
  * [ ] [Views](https://github.com/opengeospatial/geopackage/issues/446)
  * [ ] [Assignable geometries](https://github.com/opengeospatial/geopackage/issues/445)
  * [x] [SRS ID alignment](https://github.com/opengeospatial/geopackage/issues/444)
  * [ ] [Geometry in WKB extents](https://github.com/opengeospatial/geopackage/issues/443)
  * [ ] https://github.com/opengeospatial/geopackage/issues/442

### Unfiled
* [ ] [Open tickets](https://github.com/opengeospatial/geopackage/issues)
* [ ] Tile Matrix Set - waiting for further movement from OGC. The OAB approved releasing a draft standard for an open comment period but the commencement of this period was delayed.
* [ ] Requirements Classes - this would provide consistency with other standards and make capabilities and requirements easier to organize.
* [ ] Versioning of extensions. There is not currently a clear way to update extensions and maintain reverse compatibility. The SWG took a look at this issue and decided to delay action, but the time may come where further action is necessary.

### Tiled Gridded Coverage Extension
This was released as a [separate document](http://docs.opengeospatial.org/is/17-066r1/17-066r1.html) so that it could be maintained separately. There are no plans to produce another version but this could change.
* [x] [Update the names of the tests in the ATS (change "elevation" to "coverage")](https://github.com/opengeospatial/geopackage-tiled-gridded-coverage/issues/43)

### Related Tables Extension
* [x] GitHub Version
* [x] Release Notes
* [x] SWG Motion
* [x] [Online draft](http://www.geopackage.org/18-000.html)
* [ ] TC Vote
* [ ] Publication
* [ ] Press release

### Standards Revision Process
The process has been working well. We have been able to produce new revisions of the standard roughly every year. Individual changes are managed through [Github Issues](https://github.com/opengeospatial/geopackage/issues) and [pull requests](https://github.com/opengeospatial/geopackage/pulls). The process for creating a new GeoPackage revision is as follows:

1. Create a release notes document.
   1. Reserve an [OGC document number](https://portal.opengeospatial.org/?m=public&subtab=request&tab=1)
   1. Create a GitHub repository by duplicating an existing repository (e.g., https://github.com/jyutzler/ogc18-024)
2. Make one or more changes. 
   1. Open a GitHub issue.
   1. Commit the GitHub pull request. This causes the [working version](http://www.geopackage.org/spec/) of the standard to be updated. 
   2. Create a release notes entry. Administrative changes get a line in a table. Substantive changes get a more detailed description.
3. When the SWG is satisfied that there are enough contents for a change, the SWG moves to approve the release. After that, do the following:
   1. Mark a [GitHub release](https://github.com/opengeospatial/geopackage/releases)
   2. Produce a revision system notes is created
4. OGC approves the revision. For corrigenda, this is basically a rubber-stamp process by the TC. For a minor release, the process is more detailed.
   1. OAB Review
   1. Public Comment Period
   1. Adjudication of public comments
   1. TC vote

### GitHub Pipeline
We have a pipeline to manage our [GitHub content](https://github.com/opengeospatial/geopackage). 

* [x] The `gh-pages` branch gets published to geopackage.org.
* [x] The pipeline will automatically convert any Markdown to HTML.
* [x] Every time a change is made to the `master` branch, the pipeline generates `spec/index.html` on the `gh-pages` branch from the contents of the `spec` directory on the `master` branch.
* [ ] Migration to AsciiDoc will allow us to improve the presentation of the various geopackage.org pages. Does the pipeline automatically convert AsciiDoc to HTML like it does with Markdown? Does AsciiDoc support inline checkboxes on bullets?

---

## Outreach
Like any other capability, GeoPackage requires outreach so that members of the geospatial community understand the format and how it can be used as an enabling technology for challenges they are trying to meet. Some ways that we perform outreach include the following:
* http://geopackage.org
* Social media
* Public appearances
* Public articles

### Data
We want people to be able to find relevant data in the GeoPackage format quickly and easily. We are not seeing as much public data published in the GeoPackage format as we would like.

* [x] [data page](http://www.geopackage.org/data.html) - currently very sparse
  * [x] New Zealand
  * [x] Minnesota - currently 423 datasets, but a fairly primitive search interface
  * [x] Australian Bureau of Statistics
  * [x] Energydata.info
  * [ ] NRL
  * [ ] http://geoplatform.gov has not prioritized GeoPackage support
* [x] Social Media - minimal impact so far
* [x] TC Plenary announcement
* [x] [OGC Meeting Topic](https://github.com/ogcscotts/TC-Meeting-topics/issues/41)
* [ ] Others?

### Implementations
The [implementations page](http://www.geopackage.org/implementations.html) provides a curated list of organizations that have indicated GeoPackage support. (This is completely different from the [OGC-maintained list](http://www.opengeospatial.org/resource/products/stats).) There is still more work to be done to indoctrinate GPKG as a solution.
* [ ] [ATAK](https://atakmap.com/)
* [ ] others

### Guidance
Guidance informs potential users of the format, making it easier to use it appropriately and with as little unnecessary effort as possible. This area will continue to evolve. It is difficult to get people to write useful documentation but we will use whatever we can get.

* [x] [getting started guide](http://www.geopackage.org/guidance/getting-started.html) - where new developers should look to understand how GeoPackages are organized. This guide now includes information for the core and all adopted extensions. It is getting positive feedback.
* [x] [Community Extensions](http://www.geopackage.org/extensions.html) - this page contains a curated list of all known community extensions
* [x] [Implementation Guide](http://www.geopackage.org/guidance/implementation_guide.html) - this page catalogs a taxonomy of GeoPackage capabilities and indicates a set of capability levels for each capability, along with samples aligned to each capability level. This is a relatively new idea and it remains to be seen whether we have the right approach or not.
  * [ ] Self-assessment tool? See [Interoperability Suite](#interoperability-suite).
  * [ ] Publicity campaign?
* [ ] **Howto Guide** - how to produce certain samples. __Is it possible to do this in a way that is vendor agnostic?__ Maybe the SWG should not be responsible for publishing this.
  * [ ] SHP -> GPKG
  * [ ] WMS -> GPKG
  * [ ] tile pyramid -> GPKG
  * [ ] others? 
* Articles for poorly understood extensions
  * [ ] [Zoom Other Intervals](http://www.geopackage.org/spec/#extension_zoom_other_intervals) to allow non-powers of two tile pyramids (TileMill integration?)
  * [ ] [Schema](http://www.geopackage.org/spec/#extension_schema)
  * [ ] [Metadata](http://www.geopackage.org/spec/#extension_metadata)
* [Guidance](http://www.geopackage.org/guidance.html) page containing articles for frequently asked questions and non-obvious solutions. Maybe we should also curate a list of public articles. We are starting to see more articles published publicly.
  * [x] [Data Modeling](http://www.geopackage.org/guidance/modeling.html)
  * [ ] **Views - we were recently asked about this and we should try to turn something around as quickly as possible**

### Online Standard
We want users to be able to find and use the standard as quickly and easily as possible. People appear to be happy with what we have here.

* geopackage.org publishing
  * [x] [_working version_](http://www.geopackage.org/spec/)
  * [x] [1.2.1](http://www.geopackage.org/spec121/) 
  * [x] [1.2.0](http://www.geopackage.org/spec120/)
  * [x] [1.1.0](http://www.geopackage.org/spec110/) 
  * [x] [1.0.1](http://www.geopackage.org/spec101/)
* PDF publishing
  * [x] [1.2.1](https://portal.opengeospatial.org/files/12-128r15) 
  * [x] [1.2.0](https://portal.opengeospatial.org/files/12-128r14)
  * [x] [1.1.0](https://portal.opengeospatial.org/files/?artifact_id=64506) 
  * [x] [1.0.1](https://portal.opengeospatial.org/files/?artifact_id=63378&version=1)
* Release Notes
  * [ ] 1.2.1 
  * [x] [1.2.0](https://portal.opengeospatial.org/files/16-126r8)
  * [x] [1.1.0](https://portal.opengeospatial.org/files/?artifact_id=67120) 

### Blog Postings
I occasionally post articles on http://geopackage.blogspot.com. These tend to be more process and management-based than technical. 

---

## Verification and Validation
### Executable Test Suite (ETS)
This is software that allows the user to load a GeoPackage and receive a report on any standard compliance issues. It is currently built on top of the OGC TEAM Engine.

#### Adoption
Currently the ETS is in beta. We would like it to become official so that we can maintain proper lists of compliant software implementations.
* [x] GitHub
* [x] [Beta Site](http://cite.opengeospatial.org/te2/about/gpkg12/1.2/site/)
* [ ] Three implementations
  * [x] Esri
  * [x] NGA/BITS
  * [ ] ???
* [ ] OGC approval

#### Maintenance
* [x] [Open tickets](https://github.com/opengeospatial/ets-gpkg12/issues)
* [ ] Better reporting
  * [ ] Clearer output report
  * [ ] Version of file
  * [ ] Warnings
* [x] Integration with Simple Features test
* Acquire additional samples (ongoing)

### Interoperability Suite
This is software that allows the user to load a GeoPackage. It will report both standard compliance issues and interoperability issues that fall outside of what can be governed by the standard. We do not currently have an advocate for this activity.

### Implementations list
OGC maintains a list of [registered implementations](http://www.opengeospatial.org/resource/products/compliant). These can be self-selected, but organizations who have gone through the full certification process are identified appropriately.

### Interoperability Tests
This section describes activities where representatives of software development teams get together and attempt to prove the interoperability of their software with files produced by other groups.

#### [Geospatial to the Edge Plugfest](http://www.opengeospatial.org/projects/initiatives/geoedgeplugfest)
This activity is focused primarily on National System for GEOINT (NSG) profiles but it also addresses some infrequently explored parts of the standard.

---

## Future Capabilities
### Related Tables Extension
* [x] [GitHub Repository](https://github.com/opengeospatial/geopackage-related-tables)
* [ ] Interoperability Experiment Engineering Report
  * [x] Initiation
  * [x] Technology Integration Experiments
  * [x] Engineering Report approval by OGC TC
  * [ ] Engineering Report publication
* [x] [Draft standard](http://www.geopackage.org/18-000.html)
* [x] SWG resolution of [discussion topics](https://github.com/opengeospatial/gpkg-rte-ie-er/blob/master/7-discussion.adoc) - these did not lead to any substantive changes
* [x] [Getting Started Guide](https://github.com/opengeospatial/geopackage-related-tables/wiki/Getting-Started)
  * [x] [Semantics](https://github.com/opengeospatial/geopackage-related-tables/issues/58)
  * [ ] ~[Cardinality](https://github.com/opengeospatial/geopackage-related-tables/issues/59)~
  * [ ] ~[External References](https://github.com/opengeospatial/geopackage-related-tables/issues/60)~
  * [ ] ~[UUIDs](https://github.com/opengeospatial/geopackage-related-tables/issues/61)~
  * [x] [Avoiding data duplication](https://github.com/opengeospatial/geopackage-related-tables/issues/62)
* [x] SWG motion
* [ ] OAB review
* [ ] Open comment period
* [ ] Comment resolution
* [ ] **TC vote - target of December TC**

### OWS Context
Image Matters has indicated interest in this. It would allow Context files to be stored in GeoPackages. A context can represent a single common operational picture. This would allow for a separation of GeoPackage data and its presentation.
* [x] Proof of concept
* [x] [Discussion Paper](http://docs.opengeospatial.org/dp/18-037r1/18-037r1.html)
* [ ] **Dependency on updated portrayal standards (style encoding)**
* [x] Community Extension
* [ ] Interoperability Experiment or other test activity
* [ ] Draft Standard

### Tiled Vector Data
Through the [Vector Tiles Pilot](http://www.opengeospatial.org/projects/initiatives/vt-pilot-2018), OGC is developing interoperable solutions for tiled vector data. There are five (small) proposed extensions as part of this effort:
1. Vector Tiles
1. Mapbox Vector Tiles
1. GeoJSON Vector Tiles
1. OWS Context (see above)
1. Vector Tiles Attributes (extends Related Tables Extension)

* GeoPackage Vector Tiles Extensions Engineering Report
   * [x] Draft posted to pending
   * [ ] TC adoption
   * [ ] OGC Publication
* Vector Tiles Pilot (focusing on portrayal)
   * [ ] Consensus development
   * [ ] Draft ER posted to pending
   * [ ] TC ER adoption
   * [ ] OGC ER Publication
* Next steps?

### 3D Tiles
Compusult has indicated interest in an extension based on 3D Tiles, which is now an [OGC Community Extension](https://portal.opengeospatial.org/files/?artifact_id=79136). It should be fairly straightforward to implement this in GeoPackage, although SWG members may have differing points of view on implementation details.
* [x] Proof of concept
* [x] Presentation to GPKG SWG
* [x] [Community Extension](http://www.compusult.net/html/OGC/3DTile_GeoPackage_Ext_Draft.html) 
* [ ] Interoperability Experiment
* [ ] Draft Standard

### Multi-resolution vector data
Compusult has presented this idea, but it is unclear whether there is any need to standardize it. Maybe a community extension and/or article will be sufficient?
* [x] Proof of concept
* [x] Presentation to GPKG SWG
* [ ] Community Extension
* [ ] Interoperability Experiment
* [ ] Draft Standard

### Concepts with no advocate
* styling / symbology (does this now fall under OWS Context?)
* point clouds (this may come for free with 3D tiles)
* non-SQLite implementations
* compression
* synchronization / replication
* 4D / augmented reality
