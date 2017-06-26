This is a review of possible distro-agnostic non-root solutions to workflow execution isolation.

The broad idea is to provide Docker-style isolation and reproducibility in places where:

 - we have no way of becoming root, even to install packages or set up containers
 - we don't have write access outside $HOME
 - we don't run a given distro or kernel version

The main use case for this is on large HPC installations, often running old CentOS or similar, and with limited or no ability for users to install or request installation of new software.

Authors:

 - @kdmurray91
 - @mr-c

Candidates:
-----------
 
### [PRoot](proot.me)

Proot is a userspace implementation of chroot and associated tools. It allows purely-userspace chroot-ing into a pre-build root dir, e.g. one created using `fakeroot debootstrap`.

There is also Heng Li's [proot.pl](https://github.com/lh3/proot-wrapper/blob/master/proot.pl), which wraps some parts of the process nicely (e.g. things like sanitizing PATH).



### [Fakechroot](https://github.com/dex4er/fakechroot)

And we go down the rabbit hole....

Fakechroot allows one to use chroot with fakeroot.

As a normal user one can do:

   fakechroot fakeroot debootstrap sid /tmp/rootfs

### [psuedo](https://www.yoctoproject.org/tools-resources/projects/pseudo)



Docker image integration
-------------------------

It is possible to export a rootfs tarball from a running docker container. This is as "easy" as:

```
ID=$(docker run -idt diblab/khmer)
docker export ${ID} > khmer-docker.tar
docker kill ${ID}
docker rm -f ${ID}
mkdir khmer-docker
tar xf khmer-docker.tar -C khmer-docker
```

TODO: investigate if this kind of export is possible straight from an image, and ideally straight from something like the docker registry or quay.io. The [OpenContainer format](http://blog.docker.com/2015/07/open-container-format-progress-report/) could be interesting in this regard also. But all we need is a tarball of the filesystem.

CWL Usage
---------

The overall picture would involve a drop-in replacement for a dockerised tool container based upon userspace containers on systems where these are either forbidden, or impractical. 

The aim is to run Docker-enabled tools and workflows in isolated environments without root (or docker), targeting HPC clusters.


Roadmap
-------

1. Trial `fakechroot` on HPC Systems, document success and/or hacks required:
   - [ ] `raijin.nci.org.au`: CentOS 6 PBS Pro Cluster
   - [ ] `edmund.anu.edu.au`: Debian 8 SMP machine (single node)
2. Trial Docker image -> rootfs tarball conversion, write script to perform this?
    - Dockerfile -> build container on Debian -> rootfs??
    - A rootfs registry?
    - OpenContainer Initiative?
    - pull straight from docker hub/registry/quay.io?
3. Implement an orchestrator of the setup/run/teardown cycle for userspace containers, aiming at CWL feature parity with Docker.
4. Determine optimal cluster-based CWL implementation for this behaviour, or write into spec as an optional extension?

Progress
--------

### Getting userspace containers working on ancient RHEL

It looks that proot is the best option across all systems. Fakeroot/fakechroot and friends have system dependencies and I coudn't get them working on RHEL 6.

What I got to work on raijin.nci.org.au (Running RHEL 6):

```bash
wget -O ~/bin/proot http://portable.proot.me/proot-x86_64
chmod +x ~/bin/proot
mkdir containers
cd containers
mkdir debian-sid
wget -O debian-sid-rootfs.tar.xz https://github.com/tianon/docker-brew-debian/raw/0a2d20ca8e26f7bf6a5cc3ce2727eb6cc1894ef9/unstable/rootfs.tar.xz
tar xf debian-sid-rootfs.tar.xz -C debian-sid
proot -S debian-sid
# now within container
apt-get update && apt-get upgrade && apt-get install vim
```

Gitter snippets
---------------
LUSTRE FS locking:

> @kdmurray91 yeah. Just be aware that if localflock is in operation then software uses locking, assumes it's fully consistent - but you don't really have that (only consistent on each node). So always potential for weird behavior if a workflow uses same dirs/files from different nodes on a localflock FS. Various weird bugs in workflows related to non-deterministic clashes at the FS level, not due to the workflow or workflow engine.

> @dctrud @kdmurray91 so in terms of CWL semantics, the tool is disallowed from modify anything other than the designated output directory ($PWD), the designated temporary directory ($TMPDIR) and the system temporary directory (/tmp)

> <kdmurray91> The other thing worth noting is that proot -R/-S does some magic with binds that may include certain paths (e.g. $HOME) that shouldn't be bound for CWL purposes. It may be worth wrapping proot.



The links
---------

The below are links of interest or possible interest. No guarantee of relevance or correctness.


- https://pypi.python.org/pypi/sandboxlib/0.3.1
- http://ivoire.dinauz.org/blog/post/2013/11/21/Pretending-to-be-root-inside-PRoot
- https://github.com/CodethinkLabs/sandboxlib
- https://unix.stackexchange.com/questions/6433/how-to-jail-a-process-without-being-root
- http://chdir.org/~nico/seccomp-nurse/
- http://fakeroot-ng.lingnu.com/index.php/Home_Page
- https://github.com/appc/spec/
- https://stackoverflow.com/questions/4249063/run-an-untrusted-c-program-in-a-sandbox-in-linux-that-prevents-it-from-opening-f
- https://git.gnome.org/browse/linux-user-chroot/tree/
- http://wiki.baserock.org/
