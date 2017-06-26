# Description of a Project

https://github.com/edumbill/doap

# Software Package Data Exchange

https://spdx.org/

# EDAM

http://edamontology.org

# Workflow 4ever

https://wf4ever.github.io/ro/

# Prov-O

http://www.w3.org/TR/prov-o/

# Open Provenance Model

http://openprovenance.org/

# Ontologies that might be used in CWL Metadata

Document related:
* "earl": "http://www.w3.org/ns/earl#"
* "duv": "http://www.w3.org/TR/vocab-duv/"
* "foaf": [friend of a friend](http://xmlns.com/foaf/0.1/)
* "doap": [Description of a Project](http://usefulinc.com/ns/doap)
* "adms": [Asset Description Metadata Schema - Application Profile(ADMS-AP)](http://purl.org/adms/)
* "admssw": [Asset Description Metadata Schema for Software (ADMS.SW)](http://purl.org/adms/sw/)

Articles publications 
* http://purl.org/spar/cito/
* http://purl.org/spar/fabio/

Biology:
* http://www.uniprot.org/core/
* http://rdf.wwpdb.org/schema/pdbx-v40.owl#
* [Atlas RDF schema](https://www.ebi.ac.uk/fgpt/ontologies/gxaterms.html)

Note: http://packages.qa.debian.org/packagename has a corresponding RDF/XML 
http://packages.qa.debian.org/b/bowtie.rdf

Example:
```yaml

"@context":
  "foaf": "http://xmlns.com/foaf/0.1/"
  "doap": "http://usefulinc.com/ns/doap"
  "adms": "http://purl.org/adms/"
  "admssw": "http://purl.org/adms/sw/"

adms:Asset
  admssw:SoftwareProject
    doap:name: "STAR"
    doap:description: >
      Aligns RNA-seq reads to a reference genome using uncompressed suffix arrays.
      STAR has a potential for accurately aligning long (several kilobases) reads that are
      emerging from the third-generation sequencing technologies.
    doap:homepage: "https://github.com/alexdobin/STAR"
    doap:repository:
      - doap:GitRepository:
        doap:location: "https://github.com/alexdobin/STAR.git"
    doap:release:
      - doap:revision: "2.5.0a"
    doap:license: "GPL"
    doap:category: "commandline tool"
    doap:programming-language: "C++"
    foaf:Organization:
      - foaf:name: "Cold Spring Harbor Laboratory, Cold Spring Harbor, NY, USA"
      - foaf:name: "2Pacific Biosciences, Menlo Park, CA, USA"
    foaf:publications:
      - foaf:title: "(Dobin et al., 2013) STAR: ultrafast universal RNA-seq aligner. Bioinformatics."
        foaf:homepage: "http://www.ncbi.nlm.nih.gov/pubmed/23104886"
    doap:developer:
      - foaf:Person:
        foaf:name: "Alexander Dobin"
        foaf:mbox: "mailto:dobin at cshl.edu"
        foaf:fundedBy: "This work was funded by NHGRI (NIH) grant U54HG004557"
  adms:AssetDistribution
    doap:name: "STAR.cwl"
    doap:specification: "http://common-workflow-language.github.io/draft-3/"
    doap:release: "cwl:draft-3.dev2"
    doap:homepage: "https://github.com/common-workflow-language/workflows/blob/master/tools/STAR.cwl"
    doap:repository:
      - doap:GitRepository:
        doap:location: "https://github.com/common-workflow-language/workflows"
    doap:maintainer:
      foaf:Person:
        foaf:openid: ""
        foaf:name: ""
```