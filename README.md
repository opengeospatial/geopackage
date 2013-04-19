GeoPackage Tiles Specification
==========

This is an experiment in using GitHub to create specifications. It is focused on the 'tiles' portion
of the public GeoPackage OGC draft specification. 

The main specification is in the [spec.md] (spec.md) file. It currently has all of Section 10 of the specification. 
Most of the long SQL statements have been moved to the [safe-gpkg.md] (safe-gpkg.md) file, which will
eventually expand to explain how to use additional sql to make geopackages that are automatically constrained.
The requirements have also been moved out of the main specification, in to [requirements.md] (requirements.md). 
This should eventually include the conformance classes. The inline notes were also moved to the end of the 
document, it may make sense to move them to their own document, an 'implementation notes' or something.

To contribute find an issue in the [tracker] (http://github.com/cholmes/gpkg-tiles/issues) and make a pull request. 

If you are a github newbie then just hit 'edit' on the [spec.md page] (https://github.com/cholmes/gpkg-tiles/blob/master/spec.md). 
This will automatically 'fork' the repository in to your own copy. After editing there you can create 
a 'pull request' from your fork to submit the work for review and merging.

If you are making a more substantial set of changes please create a branch to work on the set. Pull requests
stay with the branches they are made on, so if you make more changes based on feedback that can all get 
pulled in when ready. Note you can create new branches as well as new files completely through the web.

For more on markdown there is a great [cheat sheet] (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
And note you can hit 'preview' at any time in edit mode to see if you got things right. 
