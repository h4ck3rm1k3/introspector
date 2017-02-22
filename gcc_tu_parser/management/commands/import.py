import os
import sys
import pickle
import pprint
import subprocess
import os.path


# Display pairs.
import time
from threading import Thread
import gcc.tree.tuast 
all_nodes = {}
fields = {}
#fields2 = {}
maxlen={}
def getlen(v2):
    if isinstance(v2, str):    
        return len(v2)
    else:
        if (isinstance(v2,gcc.tree.tuast.String2)):
            #print (type(v2))
            #pprint.pprint( v2.__dict__)
            #pprint.pprint(v2)
            return len(v2.val)
        else:
            raise Exception()

from gcc_tu_parser.models import SourceFile,Node
import gcc_tu_parser.models

def proc(directory, n):
    print ("running test %s" % n)

    f = "%s/%s.nodes.pickle" % (directory,n)
    if not os.path.isfile(f) :
        print ('skip:'+f)        
        return
    else:
        print ('import:'+f)
    try:
        file_obj= SourceFile.objects.get(filename=f)
    except SourceFile.DoesNotExist as e:
        file_obj= SourceFile.objects.create(filename=f)
        
    
    f2 = open (f,"rb")
    node_objs = pickle.load(f2)

    for x in node_objs.keys():

        try:
            nd = Node.objects.get(source_file=file_obj, node_id=x)
        except Node.DoesNotExist as e:
            nd = Node() #.objects.create(source_file=file_obj, node_id=x, refs_argt=0)

        
        nd.source_file=file_obj
        nd.node_id=x
        d = node_objs[x]
        ntype = d['type']
        nd.node_type=ntype

        skip = ('type','nid')
        for f in d:
            if f in skip:
                continue
            v = d[f]
            #print ("check",f,v)
            if isinstance(v, str):
                #nd.
                print ('str',f,v)
            else:
                if f =='refs':
                    for f2 in v:
                        v2 = v[f2]
                        d2 = node_objs[v2]
                        ntype2 = d2['type']

                        if f2.startswith('E'):
                            f2='E'
                        f2=f2.replace(' ','')
                        f2=f2.replace(':','')
                        f3 = f + '_'+ f2
                        #print ('refs',f3,f2,v2)
                        if f3 in nd.__dict__:
                            #print ('setting refs',f3,v2)
                            nd.__dict__[f3]=v2

                else:
                    for f2 in v:
                        f3 = f + '_'+ f2
                        v2 = v[f2]
                        if f3 in nd.__dict__:
                            #print ('setting refs',f3,v2)
                            nd.__dict__[f3]=v2
                        else:
                            print ('other',f2,v2)
        #pprint.pprint(nd.__dict__)
        nd.save()
        #raise Exception()

class Command:
    def run_from_argv(self, argv):
        directory = argv[-1]
        print(('going to read %s' % (directory)))

        # Get all files.
        list = os.listdir(directory)

        # Loop and add files to list.
        pairs = []
        for file in list:
            if (file.endswith(".tu") or file.endswith(".t")) and '#' not in file:
                # Use join to get full file path.
                location = os.path.join(directory, file)

                # Get size and add to list of tuples.
                size = os.path.getsize(location)
                pairs.append((size, file))
        pairs.sort(key=lambda s: s[0])

        threads = []
        for pair in pairs:
            n = pair[1]
            proc(directory,n)
            #t = Thread(target=proc, args=(directory, n,))
            #t.start()
            #threads.append(t)

        for t in threads:
            t.join()

        #pprint.pprint(fields)
        pprint.pprint(maxlen)
