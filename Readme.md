This provides a script for converting a JSTOR data for research (http://dfr.jstor.org/) citations file (.csv) into a BibTex file (.bib) for importation into Zotero (or to any reference manager that understands BibTeX, for that matter).

Having your files in Zotero (https://www.zotero.org/) has all kinds of benefits, of course. One is that you can then use PaperMachines (http://papermachines.org/) to explore your files with word clouds, topic models, and more (it is very easy to use, and provides some good overviews, though less documentation than one might wish.)

This script assumes .txt files named as they come from JSTOR Data for Research.

This script assumes that the csv file has the following fields in the following order:

```
id, doi, title, author, journaltitle, volume, issue, pubdate, pagerange, publisher, type, reviewed-work, abstract
```

This should be the case for recently created JSTOR files. Fields that are ignored:

```
doi, publisher, type, reviewed-work, abstract
```

