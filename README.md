[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ab64f00aeca946ada1c3c7cc7cabcda0)](https://www.codacy.com/gh/JoshuaSBrown/PyCGADExample2/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JoshuaSBrown/PyCGADExample2&amp;utm_campaign=Badge_Grade)
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
