Proposal by Niels Drost & Michael R. Crusoe:

Python API to generate Python objects that wrap a CWL Process (a CommandLineTool, Workflow, or ExpressionTool)

Can be used to configure and run that Process in a Pythonic way

Useful in [Jupyter Notebooks](http://jupyter.org/)

A notebook that intersperses running these CWL Processes with their own computation could be exported into a pure CWL workflow with the in between steps turned into Python scripts (wrapped in a CWL CommandLineTool).

## Pseudocode

```python
helloworld = cwlWrap("helloworld.cwl")
result = helloworld(name="Fred")
print result["greeting"]
```

> Hello, Fred!

## Actual code
``` python
import cwltool.factory
f = cwltool.factory.Factory()
echo = f.make("v1.0/v1.0/echo-tool.cwl")
out = echo(in="foo")
```

## Related

* [Running Taverna Workflows from iPython Notebook](http://www.taverna.org.uk/2014/05/20/calling-taverna-workflows-from-ipython-notebook/)
* https://www.youtube.com/watch?v=QVQwSOX5S08
* http://software.broadinstitute.org/cancer/software/genepattern/genepattern-notebook-for-jupyter-users