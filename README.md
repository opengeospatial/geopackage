![OGC Logo](https://static.ogc.org/assets/ogc/2021/ogc_logo_2021-flat_hr_blue_wh-157x80.png "OGC Logo")

GeoPackage Standard
==========
==========

GeoPackage is an open, standards-based, platform-independent, portable, self-describing, 
compact format for transferring geospatial information. The GeoPackage standard 
describes a set of conventions for storing the following within an SQLite database:
   * [vector features](spec/core/2a_features.adoc)
   * [tile matrix sets of imagery and raster maps at various scales](spec/core/2b_tiles.adoc)
   * [attributes (non-spatial data)](spec/core/2f_attributes.adoc)
   * [extensions](spec/core/annexes/extensions.adoc)

These capabilities are built on a common [base](spec/core/1_base.adoc) and an 
[Extension Mechanism](spec/core/2e_extensions-mechanism.adoc) is 
described to provide implementors a way to include additional functionality in their GeoPackages.

This OGC® Encoding Standard defines the schema for a GeoPackage, 
including table definitions, integrity assertions, format limitations, and content constraints. 
The allowable content of a GeoPackage is entirely defined in this standard.

For more information about GeoPackage, including implementations and sample data, 
go to the public page at http://www.geopackage.org. 
An HTML version of the standard is available at http://www.geopackage.org/spec/.
The asciidoc source for the standard is in the [spec/core/](spec/core/) folder.

About
-----

This GitHub repository was originally extracted from the Microsoft Word version of the Candidate 
GeoPackage Standard [version 0.8](https://portal.opengeospatial.org/files/?artifact_id=54838) 
released for [public comment](http://www.opengeospatial.org/standards/requests/105) on August 6, 2013. 
With this repository the OGC invites collaboration and comments directed at the development 
and enhancement of this candidate standard. 

The repo tracks the latest version of the standard as it evolves. Pull requests for fixes are
appreciated, and new functionality will still be considered even though version 1.0 has been adopted. The spec
is done in [asciidoc](http://www.methods.co.nz/asciidoc/) a format supported by GitHub, similar to markdown
but with some features that make it better for specifications, like automatic section numbering.

**Editor: Jeff Yutzler**

**Editor Emeritus: Paul Daisey**

Contributing
------------
The contributor understands that any contributions, if accepted by the OGC Membership, shall 
be incorporated into the formal OGC GeoPackage standards document and that all copyright and 
intellectual property shall be vested to the OGC.

The GeoPackage Standards Working Group (SWG) is the group at OGC responsible for the stewardship
of the standard, but is working to do as much GeoPackage work in public as possible.

The Geopackage SWG currently has the following email lists:
   - geopackage@lists.opengeospatial.org -- [sign up here](https://lists.ogc.org/mailman/listinfo/geopackage)
      - Public List, very little traffic.
      - Open archives
      - No Intellectual Property items should be discussed here.
   - geopackage.swg@lists.opengeospatial.org -- [sign up here](https://lists.ogc.org/mailman/listinfo/geopackage.swg)
      - Private List
      - Access controlled archives
      - Requires OGC membership and Observer Agreement to protect IPR (intellectual property rights)

**SWG Chair: Jeff Yutzler**

**SWG Vice Chair: Tracey Birch**


Editing and commenting
----------------------
The GeoPackage SWG is accepting public comments and suggested revisions to the standard 
via GitHub. This is the first time OGC has supported this mechanism for public comment and review. 
To suggest changes to the standard please fork the repository and submit a pull request with
the desired changes. Please make one pull request per logical requested change and be sure to
include a comment in the PR with any justification or reasoning on why the change is needed.

For more general comments (that don't include actual text changes to the spec) please create a GitHub
[issue](https://github.com/opengeospatial/geopackage/issues) for that topic.

Complex changes and feature requests must go through the [change request](http://portal.opengeospatial.org/public_ogc/change_request.php) process. The details entered
in the change request form will help the SWG adjudicate and prioritize the request.

For more detailed guidance, or if you are new to GitHub, see the [Process page](process.md) for additional 
information on editing.
