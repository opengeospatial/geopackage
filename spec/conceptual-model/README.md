# Standard template

## Content

This folder contains the text for the standard

* standard_document.adoc - the main standard document with references to all sections
* remaining adocs - each section of the standard document is in a separate document: follow directions in each document to populate
* figures - figures go here
* images - Image files for graphics go here. Image files for figures go in the "figures" directory. Only place in here images not used in figures (e.g., as parts of tables, as logos, etc.)
* requirements - directory for requirements and requirement classes to be referenced in clause_7_normative_text.adoc
* code - sample code to accompany the standard, if desired
* abstract_tests - the Abstract Test Suite comprising one test for every requirement, optional
* UML - UML diagrams, if applicable

## Building

To produce the HTML of the standard run 

> asciidoctor --safe -a data-uri -r asciidoctor-diagram -o standard_document.html standard_document.adoc

To produce the PDF of the standard run 

> asciidoctor-pdf --safe -a data-uri -r asciidoctor-diagram -o standard_document.pdf standard_document.adoc

