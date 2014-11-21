#!/usr/bin/env python

'''
Dicom-Parser
~~~~~~~~~~~~
Reads a dicom file and returns the  attributes as a dictionary
:copyright: Hrishikesh K B , 2014
:license: MIT License, see lincense.txt for more details

'''
from collections import defaultdict
import dicom

def dparser(filename):
    dicomvalues = defaultdict(list)
    if type(filename) is str:
        data = dicom.read_file(filename)
        for key in data.dir():
            value = getattr(data, key, '')
            if type(value) is dicom.UID.UID or key == "PixelData":
                continue
            dicomvalues[key].append(value)
    else:
        raise Exception("FileName should be a string") 
        return
    return dicomvalues       
if __name__ == "__main__":
    fname = raw_input("Please enter dicom filename(give 'exampledata/sample.dcm' for testing) : ")
    print dict(dparser(fname))
        


