import pickle
import sys
sys.path.append("/home/mdupont/experiments/")
sys.path.append("/home/mdupont/experiments/gcc_py_introspector")

import gcc_py_introspector

def load_file(fn):
    f = open (fn,"rb")
    node_objs = pickle.load(f)
    gcc_py_introspector.nodes.nodes = node_objs

    #for x in sorted(list(node_objs.keys()), key=int):
    #    print (x)
    return sorted(node_objs.keys())
