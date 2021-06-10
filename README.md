
# PyCGADExample2

Shows a second concrete implementation of Py-CGAD. The upload download script
is a simple script that allows you to upload and download files to the repo 
and its wiki. 

To test it

```Bash
python3 -m pytest
```

To see tests with printed output 

```Bash
python3 -m pytest -s
```

To run the upload_download.py script

```Bash
PYTHONPATH=$PYTHONPATH:upload_download python3 ./bin/upload_download.py --help
```
