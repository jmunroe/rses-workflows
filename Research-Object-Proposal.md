This is a proposal document for Research Objects to capture provenance of CWL workflow runs, as well as associated metadata. 

Draft notes by: @FarahZKhan, @stain

Random link collection (**TODO** Describe and organize)

* **Previous CWL discussions**
  * https://github.com/common-workflow-language/common-workflow-language/issues/84

    @ntijanic Proposed that we specify the properties to extend [wfprov](http://wf4ever.github.io/ro/#wfprov) to include information about command line and environment setup used for the workflow run. He further suggested we can use [EDAM](http://edamontology.org/page), an ontology of bioinformatics operations, types of data and identifiers, application domains and formats. 

    @stain suggested [**Research Object**](http://www.researchobject.org/) [bundle](https://w3id.org/bundle/) including all the files generated as a result of a workflow run and copies of CWL workflow and tool descriptions at the time of running. We can also have a discussion about specifications, use and principles,  in their [**gitter channel**](https://gitter.im/ResearchObject/ResearchObject). Few points from his comment: 

    1. `cwl:CommandLineTool` can be represented as [wfdesc:ProcessImplementation](http://wf4ever.github.io/ro/2016-01-28/wfdesc/#hasImplementation)
    2. `wfdesc:Workflow` can be similar to [wfdesc:WorkflowDefinition](http://wf4ever.github.io/ro/2016-01-28/wfdesc/#WorkflowDefinition)and the Workflow as a structure can have a common UUID identifier. In addition, when a workflow is used as a nested workflow more than once, we can make an identifier for each of the sub-workflow to match the outer `cwl:Step`, where both identifiers will refer to same `wfdesc:hasWorkflowDefinition`. **We might face problems with tracking provenance of the sub-workflow runs as two runs will be associated with the same parameter name.**
    3. If `cwl:Step` is a sub-workflow, then the equivalent [wfdesc:ProcessRun](http://wf4ever.github.io/ro/2016-01-28/wfprov/#ProcessRun)s gets 'upgraded' to [wfdesc:WorkflowRun](http://wf4ever.github.io/ro/2016-01-28/wfprov/#WorkflowRun)s  which would have inner `ProcessRun`s linked to it with [wfprov:wasPartOfWorkflowRun](http://wf4ever.github.io/ro/2016-01-28/wfprov/#wasPartOfWorkflowRun). 

We can also benefit from existing resources such as many experiments represented as research object bundle using [ROHUB](http://www.rohub.org/portal/home) (Research Object Digital Library) to better capture the required details in the bundle and preserve it for future use. A significant characteristic of ROHUB is keeping track of history of RO to identify the points of difference between two versions of any study. In addition, the quality checks are also worth exploring as this is similar to what we talked about (guiding the user to capture all the necessary domain specific details by providing quality checks of the RO).  A key example case study using RO to aggregate data and metadata that enrich the workflow specifications is [a workflow based experiment](https://doi.org/10.1016/j.websem.2015.01.003) investigating aspects of Huntington’s disease. 

  * https://github.com/common-workflow-language/common-workflow-language/issues/214

    @stain suggests re-using existing vocabularies such as [JSON-LD context](https://w3id.org/bundle/#json-ld) and adding provenance properties such as `retrievedFrom` and `authoredBy` to core CWL JSON-LD context to facilitate usage without prefixes. 


* [**Exported provenance in Taverna**](https://github.com/apache/incubator-taverna-engine/tree/master/taverna-prov#structure-of-exported-provenance):

This document details the provenance bundle provided as a downloadable object for any Taverna workflow. It contains all the components required to fully understand a workflow run. [wfdesc](http://wf4ever.github.io/ro/2016-01-28/wfdesc/) is used to represent the workflow in abstract representation which we can use to generate an abstract visual representation of the workflow for better readability. In addition, the bundle contains a provenance file for that particular workflow run for which the bundle was created. This file uses provenance vocabularies such as [PROV-O](https://www.w3.org/TR/prov-o/), [wfprov](https://w3id.org/ro/2016-01-28/wfprov) and tavernaprov to capture details of inputs, outputs, intermediate results and parameters. There are four more sub-directories in the bundle named as `inputs`, `outputs`, `intermediates` and `.ro` containing inputs to the workflow run, outputs produced as a result of workflow execution, intermediate results from the processes of the workflow, manifest and abstract workflow description (mentioned above). `This document can definitely be used to build upon and add other provenance related factors such as compute and storage requirements (such requirements can be extracted from CWL description and annotated in the provenance file) to provide more information to the users before they enact the workflow.`  

* [**Biocompute Objects**](http://tinyurl.com/bcospec):

Biocompute Objects aim to store and transfer inter operable information about NGS computational analysis (mainly carried out chaining different tools together in a workflow) such as version and parameter setting of the tools in a pipeline, availability/reference of the input and output data for authenticity and verification of the results and the pipeline and other important metadata resulting in improved standards for evaluation, validation and verification of the bioinformatics analysis. Currently everything is saved in one JSON file. We can think of ways to connect to the other files for keeping track of the provenance information. A CWL executable workflow with BCO packaged in an RO will hopefully cover enough information and will be inter operable ans portable as suggested by [Stian](https://hive.biochemistry.gwu.edu/prd/htscsrs//content/slideDecks/19_Soiland-Reyes_Stian_Session2ADay2.pdf) in this [workshop](https://hive.biochemistry.gwu.edu/htscsrs/workshop_2017_agenda). 

[Current work](https://view.commonwl.org) produces a RO bundle when provided the link to the workflow specification (an example can be visualized [here](https://view.commonwl.org/workflows/github.com/ProteinsWebTeam/ebi-metagenomics-cwl/tree/2104dc3/tools/rRNA_selection.cwl)). The viewer provides [visual representation](https://view.commonwl.org/workflows/5915270d857aba0001d389cc/graph/svg) of the workflow specification which includes nodes for sub-workflows as well. The resulting bundle contains the workflow specification, manifest file containing metadata and `prospective provenance` aspects that can be shared as a zipped folder for later use. This can be extended to track `retrospective provenance` for the workflow run. In this process, the intermediate files can be tracked along with their checksums and metadata using the file system structure called [**BagIt**](https://w3id.org/ro/bagit) for transferring and archiving files. 

* [**PROV Model Primer**](http://www.w3.org/TR/prov-primer/)


* * https://www.w3.org/Submission/prov-json/
* * https://lucmoreau.github.io/ProvToolbox/ 
* https://json-ld.org/
* * https://github.com/apache/incubator-taverna-databundle-viewer
..