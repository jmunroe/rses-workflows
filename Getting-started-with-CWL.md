1. [Install the CWL reference implementation](https://github.com/common-workflow-language/cwltool)
 ```
 pip install cwl-runner
 ```

 If you haven't used `pip` before you will likely need to add the destination directory to your PATH:
 ```
 export PATH=${PATH}:~/.local/bin/ # fixes it now 
 echo 'export PATH=${PATH}:~/.local/bin/' >> ~/.bashrc # and fixes it the next time you log in
 ```
 Test your install with `cwltool --version`

2. Download the specification

 ```
 git clone https://github.com/common-workflow-language/common-workflow-language.git
 ```
3. Look at a simple CWL workflow description

 ```
 cd common-workflow-language/draft-3/draft-3/
 less sorttool.cwl # first tool
 less revtool.cwl # second tool
 less revsort.cwl # workflow that uses both tools
 less revsort-job.json # lists inputs to that workflow
 less whale.txt # the input text
 ```

4. Run the simple workflow

 ```
 cwltool --no-container revsort.cwl revsort-job.json 
 less output.txt # should be reversed & sorted
 ```
 Congratulations -- you have run your first CWL workflow!