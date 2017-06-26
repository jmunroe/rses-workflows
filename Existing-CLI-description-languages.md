# Taverna

How to make and edit Tool Services in their GUI
http://dev.mygrid.org.uk/wiki/display/tav250/Tool+service
http://dev.mygrid.org.uk/wiki/display/tav250/Command

No description of the tool definition file format exists.

# Galaxy

https://wiki.galaxyproject.org/Admin/Tools/ToolConfigSyntax
XML; use of embedded Python pulls in Galaxy specific semantics.

# EMBOSS's ACD

They ship tool definition files with all of their tools. Great docs, uses EDAM. Specific to EMBOSS style tools only, though.

http://emboss.sourceforge.net/developers/acd/syntax.html

# IMPACT
https://github.com/impactcentre/interoperability-framework/blob/master/toolwrapper/src/main/resources/toolspec.xsd

# SCAPE
(fork of IMPACT)

https://github.com/openplanets/scape-toolwrapper/blob/master/toolwrapper-data/src/main/resources/tool-1.1_draft.xsd

https://github.com/openplanets/scape-toolwrapper

# CLIMate
http://cli-mate.lumc.nl/
https://git.lumc.nl/humgen/cli-mate

The actual ontology is not available for download and the authors have not responded to repeated emails.

# Rabix

https://github.com/rabix/experiments/blob/master/schemas/tool.json

# Mobyle

Relax-NG schema definitions:
https://projets.pasteur.fr/projects/mobyle/repository/show/tags/release_1_5_3/Schema
`program.rnc` defines command line tools, but import generic aspects of Mobyle services that are shared with workflows or widgets by importing `common.rnc`

Documentation:
https://projets.pasteur.fr/projects/mobyle/repository/entry/tags/release_1_5_3/Doc/service_description_guide.pdf

# BioDT

https://biodatomics.atlassian.net/wiki/display/BioDTv2DOC/Create+a+Tool
https://biodatomics.atlassian.net/wiki/display/BioDTv2DOC/Workflow
https://biodatomics.atlassian.net/wiki/display/BioDTv2DOC/Advanced+Programming

Not opensource.

# DiscoveryEnvironment
from the iPlantCollaborative
No serialized format for import/export.

# PISE
http://code.google.com/p/openinquiry/source/browse/trunk/open_inquiry/misc/pise.dtd
http://openinquiry.googlecode.com/svn/trunk/open_inquiry/misc/pise.xsd

# AGAVE API
http://agaveapi.co/live-docs/

# Arvados
http://doc.arvados.org/user/topics/run-command.html

# Sense
(Not actually a CLI wrapper, more like a wrapper for an interactive sessions of a language, but still interesting)
https://github.com/SensePlatform/sense-engine

# CmdSynopsis

Not used as wrapper in any tool, but seems to be a rather general CLI description language, used to generate the man pages for commandline tools, etc.

http://www.docbook.org/tdg51/en/html/cmdsynopsis.html

# docopt

http://docopt.org/

# Biopieces

http://maasha.github.io/biopieces/

# Common Tool Description / Common Tool Descriptor

Used by all http://www.seqan.de applications; from OpenMS/SeqAn

http://workflowconversion.github.io/#designer-templates

https://github.com/WorkflowConversion/CTDSchema/blob/master/CTD.xsd

http://www.slideshare.net/AustralianBioinformatics/bridging-the-gap-enabling-top-research-in-translational-research/51

https://www.knime.org/files/ugm2013_talks/knime_ugm_2013_knutreinert_final.pdf

https://www.knime.org/files/kos-11/CADD_GenericNodes.pdf#page=15

http://ceur-ws.org/Vol-993/paper9.pdf

# AlgoRun

http://algorun.org/documentation

# YABI

http://yabi.readthedocs.io/en/latest/tools.html#tool-description
