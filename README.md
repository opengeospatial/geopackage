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

For more about GeoPackage, including implementations and sample data, 
go to the public page at http://www.geopackage.org. 
An HTML version of the specification is available at http://www.geopackage.org/spec/.
The asciidoc source for the specification is in the [spec/](spec/) folder.

About
-----

This GitHub repository was originally extracted from the Microsoft Word version of the Candidate 
GeoPackage Standard [version 0.8](https://portal.opengeospatial.org/files/?artifact_id=54838) 
released for [public comment](http://www.opengeospatial.org/standards/requests/105) on August 6, 2013. 
With this repository the OGC invites collaboration and comments directed at the development 
and enhancement of this candidate standard. 

The repo tracks the latest version of the specification as it evolves. Pull requests for fixes are
appreciated, and new functionality will still be considered even though version 1.0 has been adopted. The spec
is done in [asciidoc](http://www.methods.co.nz/asciidoc/) a format supported by GitHub, similar to markdown
but with some features that make it better for specifications, like automatic section numbering.

**Editor: Paul Daisey**

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
the desired changes. Please make one pull request per logical requested change and be sure to
include a comment in the PR with any justification or reasoning on why the change is needed.

For more general comments (that don't include actual text changes to the spec) please create a GitHub
[issue](https://github.com/opengeospatial/geopackage/issues) for that topic.

Complex changes and feature requests must go throught the [change request](http://portal.opengeospatial.org/public_ogc/change_request.php) process. The details entered
in the change request form will help the SWG adjudicate and prioritize the request.

For more detailed guidance, or if you are new to GitHub, see the [Process page](process.md) for additional 
information on editing.
