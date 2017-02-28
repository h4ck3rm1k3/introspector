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
        to_table = argv[7]

        mdl = gcc_tu_parser.models.NamedList,
        
        if operation == 'color':
            f2= gcc_tu_parser.models.Node.MyMeta.ref_fields2[field]

            types = gcc_tu_parser.models.Node.objects.filter(
                **{
                    'node_type' : from_type,
                    '%s__node_type' % field : to_type                    
                })

            queue = []
            
            for t in types:
                fromid = t.__dict__['node_id']
                nextid = t.__dict__[f2]
                fid = t.__dict__['source_file_id']                
                fid2 = gcc_tu_parser.models.SourceFile(fid)
                
                pos = 0
                n = mdl(
                    source_file=fid2,
                    starting_node=fromid,
                    item_pos=pos,
                    node_type=to_table,
                    value=nextid)
                #n.save()
                queue.append(n)
                while nextid is not None:
                    pos = pos + 1
                    types = gcc_tu_parser.models.Node.objects.filter(
                        **{
                            'node_id' : nextid,
                        })
                    t = types.first()
                    if t:
                        #pprint.pprint(t.__dict__)
                        nextid = t.refs_chan
                        if nextid :                        
                            #print ("next %s %s %s" % (fromid, pos, nextid))                            
                            n = mdl(
                                source_file=fid2,
                                starting_node=fromid,
                                item_pos=pos,
                                node_type=to_table,
                                value=nextid)
                            #n.save()
                            queue.append(n)
                    else:
                        nextid = None
                if len(queue) > 10000:
                    print ("Creating!")
                    gcc_tu_parser.models.FuncParams.objects.bulk_create(queue)
                    queue = []
                     
            mdl.objects.bulk_create(queue)
