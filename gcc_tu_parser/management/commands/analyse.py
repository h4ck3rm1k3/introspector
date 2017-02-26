import os
import sys
import pickle
import pprint
import subprocess
import os.path
import time
from threading import Thread
#import gcc.tree.tuast 
#from gcc_tu_parser.models import SourceFile,Node
import gcc_tu_parser.models
import pprint

class Command:

    def run_from_argv(self, argv):
        
        operation = argv[3]
        from_type = argv[4]
        field = argv[5]
        to_type = argv[6]
        if operation == 'color':
            f2= gcc_tu_parser.models.Node.MyMeta.ref_fields2[field]

            types = gcc_tu_parser.models.Node.objects.filter(
                **{
                    'node_type' : from_type,
                    '%s__node_type' % field : to_type
                    
                })
            
            for t in types:
                #pprint.pprint(t.__dict__)
                fromid = t.__dict__['node_id']
                nextid = t.__dict__[f2]
                fid = t.__dict__['source_file_id']                
                
                pos = 0
                print ("First %s %s %s" % (fromid, pos, nextid))
                n = gcc_tu_parser.models.FuncParams(
                    source_file_id=fid,
                    function_decl=fromid,
                    param_pos=pos,
                    function_param=nextid)
                n.save()
                while nextid is not None:
                    pos = pos + 1
                    types = gcc_tu_parser.models.Node.objects.filter(
                        **{
                            'node_id' : nextid,
                            #'refs_chan' : f2                        
                        })
                    t = types.first()
                    if t:
                        #pprint.pprint(t.__dict__)
                        nextid = t.refs_chan
                        if nextid :
                            
                            print ("next %s %s %s" % (fromid, pos, nextid))
                            
                            n = gcc_tu_parser.models.FuncParams(
                                source_file=fid,
                                function_decl=fromid,
                                param_pos=pos,
                                function_param=nextid)
                            n.save()
                    else:
                        nextid = None
                    
