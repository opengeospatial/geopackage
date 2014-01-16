![OGC Logo](http://portal.opengeospatial.org/files/?artifact_id=11976&format=gif "OGC Logo")

GeoPackage Specification
==========

This specification describes an open, standards-based, platform-independent, portable, self-describing, 
compact format for transferring geospatial information. It is a set of conventions for SQLite to
store interoperable [Features](spec/2_features.md) and/or [Tiles](spec/3_tiles.md) on a common [base](spec/1_base.md).
The core document additionally specifies optional [Metadata](spec/5_metadata.md) and [Schema](spec/4_schema.md)
information to build richer applications. An [Extension Mechanism](spec/7_extensions-mechanism.md) is 
described to provide implementors a way to include additional functionality in their GeoPackages, with a 
number of optional [extensions](spec/8_extensions.md) included.

HTML version of the spec is available at http://opengis.github.io/geopackage/

About
-----

This GitHub repository was originally extracted from the Microsoft Word version of the Candidate 
GeoPackage Standard [version 0.8](https://portal.opengeospatial.org/files/?artifact_id=54838) 
released for [public comment](http://www.opengeospatial.org/standards/requests/105) on August 6, 2013. 
With this repository the OGC invites collaboration and comments directed at the development 
and enhancement of this candidate standard. 

The repo tracks the latest version of the specification as it evolves. Pull requests for fixes are
appreciated, and new functionality will be considered after 1.0 is finalized (Q1 2014).

**Editor: Paul Daisey**

Reading the document
--------------------
The main specification can be read at http://opengis.github.io/geopackage/.

The asciidoc source for the specification is in the [spec/](spec/) folder.

Contributing
------------
The contributor understands that any contributions, if accepted by the OGC Membership, shall 
be incorporated into the formal OGC GeoPackage standards document and that all copyright and 
intellectual property shall be vested to the OGC.

The GeoPackage Standards Working Group (SWG) is the group at OGC responsible for the stewardship
of the specification, but is working to do as much GeoPackage work in public as possible.

The Geopackage SWG currently has the following email lists:
   - geopackage@lists.opengeospatial.org -- [sign up here](https://lists.opengeospatial.org/mailman/listinfo/geopackage)
      - Public List
      - Open archives
      - No Intellectual Property items should be discussed here.
   - geopackage.swg@lists.opengeospatial.org -- [sign up here](https://lists.opengeospatial.org/mailman/listinfo/geopackage.swg)
      - Private List
      - Access controlled archives
      - Requires OGC membership and Observer Agreement to protect IPR (intellectual property rights)

Editing and commenting
----------------------
The GeoPackage SWG is accepting public comments and suggested revisions to the specification 
via GitHub. This is the first time OGC has supported this mechanism for public comment and review. 
To suggest changes to the specification please fork the repository and submit a pull request with
changes to the document. Please make one pull request per logical requested change, and be sure to
include a comment in the PR with any justification or reasoning on why the change is needed.

For more general comments (that don't include actual text changes to the spec) just create a github
issue with the relevant information. With one issue per general change.

For more detailed guidance, or if you are new to github, see the [Process page](process.md) for additional 
information on editing.

Sample Implementations
----------------------

[Luciad](http://www.luciad.com/) has open sourced their implementation as [libgpkg](https://bitbucket.org/luciad/libgpkg). It is
quite complete, with support for features, tiles, spatial indexes, and more.

[GDAL](http://www.gdal.org/) has geopackage support in a [github repository](https://github.com/pramsey/gdal/tree/gpkg) under development.

Sample GeoPackage Data
----------------------

[Sigma Bravo](http://www.sigmabravo.com.au/services/it.aspx) created a smaple geopackage of [Haiti OSM tiles and points](https://portal.opengeospatial.org/files/?artifact_id=52605).


