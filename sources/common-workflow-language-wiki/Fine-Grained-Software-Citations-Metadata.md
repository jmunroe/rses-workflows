CWL's linked data functionality can be used to show how to cite the software being described in a CWL tool description.

Linked data means we aren't making up our own vocabulary to describe things. In the example below we use a single vocabulary: [schema.org](http://schema.org/).

Example. Note that two publications from the main authors are included and a publication for a third-party library.

```
#!/usr/bin/env cwl-runner
cwlVersion: cwl:draft-3
class: CommandLineTool

$namespaces:
  schema: http://schema.org/
$schemas:
- http://schema.org/docs/schema_org_rdfa.html

schema:publication:
- class: schema:ScholarlyArticle
  id: http://doi.org/10.12688/f1000research.6924.1
- class: schema:ScholarlyArticle
  id: http://arxiv.org/abs/1203.4802
- class: schema:ScholarlyArticle
  id: http://doi.org/10.1186/1471-2105-9-11

[rest of command line description]
```

What if the citation is only appropriate if a particular command line option is used? Easy, move the citation within the tool definition to that command line option.

TODO:

1. Simple script to extract citations from CWL tool descriptions 
2. Bibtex export for the above
3. Give example of real-world fine-grained citation
4. Give example of tool outputting CWL compatible metadata at run time

Credits:

Initial work on CWL metadata by [Andrey Kartashov](https://github.com/portah). Linked data support in the CWL reference implementation by [Peter Amstutz](https://github.com/tetron). Citation feature inspired by the [Galaxy Project](https://docs.google.com/presentation/d/114yvrK0Veasc_ns_rg484j2xxRi1h7wNlU2XKONuUqY/edit#slide=id.g361e343a7_00), first implemented at 2014 BOSC codefest by John Chilton, Michael Crusoe, Peter Cock, Daniel Blankenberg, Matt Shirley.