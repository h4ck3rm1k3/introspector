from django.shortcuts import render

#DIR='/home/mdupont/experiments/lsof'
DIR='/home/mdupont/experiments/gcc_py_introspector/tests/'

# Create your views here.
from os import listdir
from os.path import isfile, join
import json

from django.http import HttpResponse
def files(r):
    files=[]
    for f in listdir(DIR) :
        if isfile(join(DIR, f)):
            if f.endswith('.nodes.pickle'):
                files.append(f)
                
    return HttpResponse(json.dumps(files))

import gcc_tu_parser.loadpickle
def picklefile(r,f):
    d ={
        'file':f,
        'res': gcc_tu_parser.loadpickle.load_file(DIR + f)
    }
    return HttpResponse(json.dumps(d))
    
