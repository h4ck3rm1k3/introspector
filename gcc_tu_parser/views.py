from django.shortcuts import render

#DIR='/home/mdupont/experiments/lsof'
DIR='/home/mdupont/experiments/gcc_py_introspector/tests/'

# Create your views here.
from os import listdir
from os.path import isfile, join
import json
from gcc_tu_parser.models import SourceFile,Node
import gcc_tu_parser.models
import pprint
from django.db.models import Count
from django.db.models import Q
import gcc_tu_parser.models
from django.http import HttpResponse
from gcc_tu_parser.models import SourceFile,Node
import gcc_tu_parser.loadpickle

def files(r):
    files ={}
    file_obj= SourceFile.objects.all()
    for f in file_obj :
        files[f.id]=f.filename
                
    return HttpResponse(json.dumps(files))

def picklefile(r,f):
    d ={
        'file':f,
        'filename': SourceFile.objects.get(id=f).filename
    }
    return HttpResponse(json.dumps(        d    ))
    
def file_nodetype(r, fid, ntype):
    #print (fid,ntype)
    d = {}
    o = Node.objects.filter(source_file=fid, node_type=ntype)
    for o1 in o:
        for f in o1.__dict__:
            v = o1.__dict__[f]
            if v is not None:
                if v != '':
                    d[f]={'%s'%v:1}
    return HttpResponse(json.dumps(        d    ))    

def filter_none(x):
    d={}
    for k in x:
        v= x[k]
        if k == '_state':
            pass
        else:
            if v == '' or v is None:
                pass
            else:
                d[k]="%s" % v
    return d
    
def lookup(fid,node_id):
    if node_id != '':
        for x in Node.objects.filter(source_file=fid, node_id=node_id):            
            return filter_none(x.__dict__)
    

def func_decls(r, fid):
    d = {}
    o = Node.objects.filter(source_file=fid, node_type='function_decl')

    #  "node_type": {"function_decl": 1}, "refs_scpe": {"154": 1},  "refs_body": {"2644": 1}, "refs_type": {"3879": 1}, "refs_chain": {"3882": 1}, "attrs_addr": {"7ff24b357540": 1}, "refs_mngl": {"1012": 1}, "refs_name": {"3878": 1}, "refs_args": {"2643": 1}, "node_id": {"3880": 1}}
    for i in o:
        d1= {
            'o' : filter_none(i.__dict__),
            'name' : lookup(fid,node_id=i.refs_name),
            #'args' : lookup(fid,node_id=i.refs_args),
            #'type' : lookup(fid,node_id=i.refs_type),
            #'body' : lookup(fid,node_id=i.refs_body),
        }
        
        if 'nodes' not in d:
            d['nodes']=[
                d1
            ]
        else:
            d['nodes'].append(d1)
    #return HttpResponse(json.dumps(        d    ))
    return render(r,'funcdecls.jinja',{'objs':  d  })    

def lookup1(d1,fieldname):

    if fieldname not in d1:
        return

    if  d1[fieldname] == '':
        return

    node_id = d1[fieldname]
    
    for x in Node.objects.filter(source_file=d1['fid'], node_id=node_id):            
        return filter_none(x.__dict__)

def lookup2(d1,typename, fieldname):

    if typename not in d1:
        return

    if fieldname not in d1[typename]:
        return

    if  d1[typename][fieldname] == '':
        return

    node_id = d1[typename][fieldname]
    
    for x in Node.objects.filter(source_file=d1['fid'], node_id=node_id):            
        return filter_none(x.__dict__)

def lookup2r(d1,typename, fieldname, name, attr):
    fid = d1['fid']
    
    r = lookup2(d1,typename, fieldname)
    r[name]=r
    r['fid']=fid
    if fieldname in r:
        r2 = lookup2r(r,name, fieldname, name, attr)
        if attr in r2:
            if attr not in r:
                r[attr]=r2[attr]
    return r

def lookup3r(d1,fieldname, name, attr):
    if not d1:
        return None
    fid = d1['fid']
    
    r = lookup1(d1,fieldname)
    if r:
        r[name]=r
        r['fid']=fid
        if fieldname in r:
            r2 = lookup2r(r,name, fieldname, name, attr)
            if attr in r2:
                if attr not in r:
                    r[attr]=r2[attr]
    return r

def lookup4r(d1,fieldname, name):
    fid = d1['fid']
    
    r = lookup1(d1,fieldname)
    if r:
        r[name]=r
        r['fid']=fid
        if fieldname in r:
            r2 = lookup4r(r,name, fieldname, name)

    return r

def resolve_name(d1):
    if not d1:
        return None
    d1['name_obj']=lookup3r(d1,'refs_name','name','attrs_string')
    if d1['name_obj']:
        d1['name']=d1['name_obj']['attrs_string']

def resolve_ptr(d1):
    d1['pointer_obj']=lookup4r(d1,'refs_ptd','pointer')
    return d1['pointer_obj']

def func_decls2(r, fid, nodeid):
    d = {}
    o = Node.objects.filter(source_file=fid, node_id=nodeid)

    for i in o:
        d1= {
            'fid' : fid,
            'o' : filter_none(i.__dict__),
            'name' : lookup(fid,node_id=i.refs_name),
            'args' : lookup(fid,node_id=i.refs_args),
            'type' : lookup(fid,node_id=i.refs_type),
            'body' : lookup(fid,node_id=i.refs_body),
        }

        d1['ret_type']=lookup2(d1,'type','refs_retn')

        #d1['ret_type']['name']=lookup2r(d1,'ret_type','refs_name','name','attrs_string')
        d1['ret_type']['name_obj']=lookup2r(d1,'ret_type','refs_name','name','attrs_string')
        d1['ret_type']['name']=d1['ret_type']['name_obj']['attrs_string']
        
        d1['type_params']=lookup2(d1,'type','refs_prms')
        d1['type_params_list']=[]
        p = d1['type_params']
        p['fid']=fid
        while p :
            
            if 'refs_valu' in p :
                p2 = lookup1(p,'refs_valu')
                p2['fid']=fid
                resolve_name(p2)
                p3=resolve_ptr(p2) # resolve pointers
                resolve_name(p3)


            else:
                p2 = None
            p['val']=p2

            d1['type_params_list'].append(p)

            if 'refs_chan' in p :
                p = lookup1(p,'refs_chan')
                p['fid']=fid
            else:
                p = None
                    
        if 'nodes' not in d:
            d['nodes']=[
                d1
            ]
        else:
            d['nodes'].append(d1)
        return render(r,'funcdecl.jinja',{'obj':  d  })    

def types(r):
    return
    # d={
    #     'fields':{},
    #     'types':{},
    #     'types2':{}
    # }
    # d2={
    #     'types2':{}
    # }
    # for f in gcc_tu_parser.models.Node.MyMeta.ref_fields:
    #     d['fields'][f]=1
    # types = gcc_tu_parser.models.Node.objects.values('node_type').annotate(Count('node_type'))
    # for t in types:
    #     nt = t['node_type']
    #     nc = t['node_type__count']
    #     if nt.endswith('_type'):
    #         d['types'][nt]=nc
    # for t in d['types']:
    #     # for
    #     d2['types2'][t]={}
    #     for f in gcc_tu_parser.models.Node.MyMeta.ref_fields:
    #         #d2['types2'][t][f]=0            
    #         fc = gcc_tu_parser.models.Node.objects.exclude(
    #             **{
    #                 #'{0}__{1}'.format(f, 'isblank'): True
    #                 '{0}'.format(f): ''
    #         }).filter(
    #             **{
    #                 '{0}'.format('node_type'): t,
    #             }
    #         ).values('node_type').annotate(Count('node_type'))
    #         for x in fc:
    #             nt = x['node_type']
    #             nc = x['node_type__count']
    #             if nc > 0 :
    #                 d2['types2'][t][f]=nc                
    # return render(r,'types.jinja',{'obj':  d2  })    

def types2(r):

    d2={
        'fields':{},
        'types':{},
        'data':[]
    }
    for f in gcc_tu_parser.models.Node.MyMeta.ref_fields2.keys():
        f2= gcc_tu_parser.models.Node.MyMeta.ref_fields2[f]
        #d2['fields'][f]={}
        
        types = gcc_tu_parser.models.Node.objects.values(
            'node_type',
            '%s__node_type' % f).annotate(Count('%s__node_type' % f))
        for t in types:
            #for f in t:
            #    d2['types'][f]=1
            nt1 = t['node_type']
            nt = t['%s__node_type' %f]
            nc = t['%s__node_type__count' %f]
            if nt1 not in d2['fields']:
                d2['fields'][nt1]={
                    f:{nt:nc}
                }
            else:
                if f not in d2['fields'][nt1]:
                    d2['fields'][nt1][f]={nt:nc}
                else:
                    d2['fields'][nt1][f][nt]=nc
            #d2['data'].append(t)
                
    return render(r,'types.jinja',{'obj':  d2  })    

def types3(r):

    d2={
        'fields':{},
    }
    for f in gcc_tu_parser.models.Node.MyMeta.ref_fields2.keys():
        f2= gcc_tu_parser.models.Node.MyMeta.ref_fields2[f]
        d2['fields'][f]={}
                        
    return render(r,'types3.jinja',{'obj':  d2  })    


