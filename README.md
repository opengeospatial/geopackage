![OGC Logo](http://portal.opengeospatial.org/files/?artifact_id=11976&format=gif "OGC Logo")

GeoPackage Specification
==========

This specification describes an open, standards-based, platform-independent, portable, self-describing, 
compact format for transferring geospatial information. It specifies a set of conventions for SQLite to
store interoperable [Features](spec/2_features.md) and/or [Tiles](spec/3_tiles.md) on a common [base](spec/1_base.md).
The core document additionally describes optional [Metadata](spec/5_metadata.md), and [Schema](spec/4_schema)
information to build richer applications. An [Extension Mechanism](spec/7_extension_mechanism.md) is 
specified to provide implementors a way to include additional functionality in their GeoPackages, with a 
number of optional [extensions](spec/8_extensions.md) included.

About
-----

This GitHub repository has been extracted from the Microsoft Word version of the Candidate 
GeoPackage Standard [version 0.8](https://portal.opengeospatial.org/files/?artifact_id=54838) 
released for [public comment](http://www.opengeospatial.org/standards/requests/105) on August 6, 2013. 
With this repository the OGC invites collaboration and comments directed at the development 
and enhancement of this candidate standard. 

**Editor: Paul Daisey**

Reading the document
--------------------
The main specification is in the [spec/](spec/) folder. 

Contributing
------------
The contributor understands that any contributions, if accepted by the OGC Membership, shall 
be incorporated into the formal OGC GeoPackage standards document and that all copyright and 
intellectual property shall be vested to the OGC.

Editing and commenting
----------------------
The GeoPackage SWG is accepting public comments and suggested revisions to the specification 
via GitHub. This is the first time OGC has supported this mechanism for public comment and review. 
To suggest changes to the specification please fork the repository and submit a pull request with
changes to the document. Please make one pull request per logical requested change, and be sure to
include a comment in the PR with any justification or reasoning on why the change is needed.

For more general comments (that don't include actual text changes to the spec) we recommend the 
traditional OGC comment process on the [GeoPackage RFC](http://www.opengeospatial.org/standards/requests/105). 

For more detailed guidance, or if you are new to github, see the [Process page](process.md) for additional 
information on editing.

