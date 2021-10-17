# ropro-nao
experiments performed with the nao robot

## NAO Robot Python SDK Installation Guide 

We used the following setup for programming our robot: 

1. Connect the PC and robot to the same (wireless) network. This is required because only then we can connect to the robot using it’s IP address.   

2. Use the official Python SDK available in the softbanks robotics site 

 
## Windows 

1. Download the correct SDK file from the downloads page. 

2. Create a python2.7 environment. 

3. Copy the folder downloaded from 1 and paste into the environment folder/Lib/ 

4. Create an environment variable with the following: 
```PYTHONPATH=environment folder/Lib/SDK_Folder/lib/ ```

5. Open Python from the environment created in step 2. 
```python
import naoqi 
```
 

## Mac or Linux 

1. Only the python2.7.10 downloaded from python.org works, so we downloaded that. 

2. Add environment variable with the following: 
```bash
$ export PYTHONPATH=${PYTHONPATH}:path_to_sdk/lib/python2.7/site-packages 

$ export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:~/Downloads/pynaoqi/lib 

$ export QI_SDK_PREFIX=~/Downloads/pynaoqi 
```
3. Open Python2.7.10
```bash
import naoqi
```

 

 

 
