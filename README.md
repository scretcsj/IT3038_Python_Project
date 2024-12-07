## Nist.py

This script is designed to help a secuirty professional quickly get details on the NIST CSF functions. The user only needs to provide a control ID such as ID.AM-01. The scrip will then return the description from the NIST control sheet

> Sample execution

```python
python .\nist.py .\nistcontrolsheet.csv GV.SC-04
```

> Basic idea behind primary function. User feeds the function a nist_control value and the script searches the specicified .csv file for a matching description. Regex is used to verify the format

```python
def NIST_Control_Description(file, nist_control):
    return information
```
