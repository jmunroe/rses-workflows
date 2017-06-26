# Running CWL on Arvados
See [Running Common Workflow Language (CWL) workflows on Arvados](https://dev.arvados.org/projects/arvados/wiki/Running_Common_Workflow_Language_%28CWL%29_workflows_on_Arvados)

# [About Arvados](http://arvados.org)
<img align="right" src="http://i.imgur.com/niVZ8Qx.png">
The Arvados Project  is an open-source bioinformatics data analysis platform, funded by Boston-based startup [Curoverse](https://curoverse.com/). It's designed to be scalable, working on local and cloud-based systems.

> The Arvados core is a platform for production data science with very large data sets. It is made up of two major systems and a number of related services and components including APIs, SDKs, and visual tools.

> ### Keep
> Keep is a content-addressable storage system for managing and storing large collections of files with durable, cryptographically verifiable references and high-throughput processing. Keep works on a wide range of underyling file systems. [Learn More >](https://dev.arvados.org/projects/arvados/wiki/Keep)
> ### Crunch
> Is a containerized workflow engine for running complex, multi-part pipelines or workflows in a way that is flexible, scalable, and supports versioning, reproducibilty, and provenance. Crunch runs in virtualized computing environments.

The "core platform" has genomic specific projects such as [Lightning](https://dev.arvados.org/projects/lightning) (real-time queries and machine learning with population genomic datasets) and [Tapestry](https://dev.arvados.org/projects/tapestry) & [GET-Evidence](https://dev.arvados.org/projects/get-evidence) (web apps for managing open science research studies, in particular those collecting genomic data, for personal genomics projects worldwide).


## Goals

> *via Arvados Dev wiki: [Computation and Pipeline Processing](https://dev.arvados.org/projects/arvados/wiki/Computation_and_Pipeline_Processing)*

The Arvados dev pages list "notable goals and features" of the project as:

> * Make use of multiple cores and nodes to produce results faster
> * Integrate with [Keep](https://dev.arvados.org/projects/arvados/wiki/Keep) and git repositories to maintain provenance
> * Use off-the-shelf software tools in distributed computations
> * Efficient over a wide range of problem sizes
> * Maximum flexibility of programming language choice
> * Maximum flexibility of execution environment
> * Tools for building reusable pipelines
> * Lower entry barrier for users

## Pipeline processing

As Hadoop was initially designed to work with web data, Arvados uses "a purpose-built [MapReduce](http://en.wikipedia.org/wiki/MapReduce) engine that is optimized for analysis of biomedical data", and "approaches MapReduce from the perspective of a bioinformatician". [Bio]informatics problems are typically carried out as sequences of analysis and data transformation, .

> Each Arvados MapReduce job contains sets of job tasks which can be computed independently of one another, and can therefore be scheduled asynchronously according to available compute resources. Typically, jobs split input data into chunks which can be processed independently, and run a task for each chunk. This works well for genomic data.

> Arvados does not make a distinction between “map” and “reduce” tasks or provide synchronous communication paths between tasks. However, a job can establish sequencing constraints to achieve a similar result (i.e., ensure that all map tasks have completed before a reduce task starts). In practice, the “reduce” stages of genomic analyses tend to be so simple that there is little to gain by introducing the complexity of scheduling and real-time communication between map and reduce tasks. 

![](http://i.imgur.com/n48N1pd.png)

* **Pipeline** - set of related MapReduce jobs (related in terms of I/O transfer, e.g. BWA to GTK)
* **Pipeline template** - JSON description of job relationships (e.g. job A output = job B input), analogous to Makefile
  * constructed as a set of _pipeline components_, each of which designates name of a _job script_, data inputs and parameters
  * data inputs are specified as _Keep content addresses_
  * job scripts are stored in a Git repo, referenced using commit hash/tag
  * parameters and inputs can be defined in template, or upon invoking pipeline (a "*pipeline instance*")
* There is no constraint/verification of pipeline logic - nothing prevent use of different pipeline manager / manual build


The pipeline:
* determines dependencies are satisfied (like Make does)
* submits new jobs
* waits for jobs to finish
   * may repeat the above until successful at each pipeline component

If identical/equivalent job has already run, pipeline uses output of existing job rather than submitting anew - faster run, more efficient use of compute resources. This behaviour can be overridden by the client when repetition is desirable.

The Arvados _job dispatcher_ processes submitted jobs:
* executes each task
* enforces task sequence order and resource constraints [as dictated by the job]
* checks process exit codes and other failure indicators
   * re-attempts failed tasks when needed
* stores status updates in the Arvados system database as the job progresses

Each pipeline instance (and job) is recorded in the system DB to preserve provenance, and aid reproducing jobs even long after initial run
* job manager records runtime details (e.g. commit hash for job script, compute node O.S. version, ...) for reproducibility "as a rule rather than an exception"

Arvados is "*language and tool neutral*":
* suitable "*from binary-only tools or in-house C programs*" using universal APIs such as HTTP, and UNIX pipes
* job scripts can be written in any language, run in a normal UNIX environment <sup>(TODO: clarify?)</sup>

### Suggested benefits

> * **Efficient processing of small tasks** - Arvados MapReduce has very low task latency, making it practical to use for even very short single-task jobs. This makes it feasible for users and applications to routinely do all computations in MapReduce and thereby achieve the benefits of complete provenance, reproducibility, and scalability.

> * **Node-level resource allocation** - Arvados MapReduce uses a node as the basic computing resource unit: a compute node runs multiple asynchronous tasks, but only accepts tasks from one job at a time. This gives each job the flexibility to allocate CPU and RAM resources among its tasks to best suit the work being done, and avoids interference and resource competition between unrelated job tasks.

### Sources / see also:

* Twitter: [@arvados](https://twitter.com/arvados)
* [Getting Genetics Done: Curoverse raises $1.5M to develop & support an open-source bioinformatics data analysis platform](http://www.gettinggeneticsdone.com/2013/12/curoverse-raises-15m-to-develop-support.html) (December 18 2013)
* [Arvados developer site](https://dev.arvados.org/projects/arvados)
* [Arvados blog](https://dev.arvados.org/projects/arvados/blogs)
* [Arvados docs](http://doc.arvados.org/)