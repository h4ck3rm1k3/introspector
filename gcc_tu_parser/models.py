import django
from django.db import models

    
from compositefk.fields import CompositeForeignKey, RawFieldValue, LocalFieldValue, CompositeOneToOneField

class SourceFile(models.Model):
    filename = models.CharField(max_length=228)
    
class Node(models.Model):
    source_file= models.ForeignKey(SourceFile,
                                   blank=True,
                                   null=True,
                                   on_delete=models.SET_NULL)
    node_id= models.CharField(max_length=9)
    node_type = models.CharField(max_length=40)
    class MyMeta:
        ref_fields = [
            'refs_E',
            'refs_OP0',
            'refs_OP1',
            'refs_OP2',
            'refs_args',
            'refs_argt',
            'refs_body',
            'refs_bpos',
            'refs_chain',
            'refs_chan',
            'refs_cnst',
            'refs_cond',
            'refs_csts',
            'refs_decl',
            'refs_domn',
            'refs_elts',
            'refs_expr',
            'refs_flds',
            'refs_fn',
            'refs_idx',
            'refs_init',
            'refs_labl',
            'refs_low',
            'refs_max',
            'refs_min',
            'refs_mngl',
            'refs_name',
            'refs_prms',
            'refs_ptd',
            'refs_purp',
            'refs_refd',
            'refs_retn',
            'refs_scpe',
            'refs_size',
            'refs_type',
            'refs_unql',
            'refs_val',
            'refs_valu',
            'refs_vars'
        ]
        ref_fields2={
            'E' : 'refs_E',
            'OP0' : 'refs_OP0',
            'OP1' : 'refs_OP1',
            'OP2' : 'refs_OP2',
            'args' : 'refs_args',
            'argt' : 'refs_argt',
            'body' : 'refs_body',
            'bpos' : 'refs_bpos',
            'chain' : 'refs_chain',
            'chan' : 'refs_chan',
            'cnst' : 'refs_cnst',
            'cond' : 'refs_cond',
            'csts' : 'refs_csts',
            'decl' : 'refs_decl',
            'domn' : 'refs_domn',
            'elts' : 'refs_elts',
            'expr' : 'refs_expr',
            'flds' : 'refs_flds',
            'fn' : 'refs_fn',
            'idx' : 'refs_idx',
            'init' : 'refs_init',
            'labl' : 'refs_labl',
            'low' : 'refs_low',
            'fmax' : 'refs_max',
            'fmin' : 'refs_min',
            'mngl' : 'refs_mngl',
            'name' : 'refs_name',
            'prms' : 'refs_prms',
            'ptd' : 'refs_ptd',
            'purp' : 'refs_purp',
            'refd' : 'refs_refd',
            'retn' : 'refs_retn',
            'scpe' : 'refs_scpe',
            'size' : 'refs_size',
            'ftype' : 'refs_type',
            'unql' : 'refs_unql',
            'val' : 'refs_val',
            'valu' : 'refs_valu',
            'fvars' : 'refs_vars',
            }
        
    class Meta:


        unique_together = (('source_file', 'node_id'),)
    attrs_string = models.CharField(max_length=228)
    
    
    #nid = models.CharField(null=True, blank=True,max_length=9)
    #refs_argt = models.CharField(null=True, blank=True,max_length=9)
    #type = models.CharField(null=True, blank=True,max_length=9)
    attrs_addr = models.CharField(max_length=12)
    attrs_note = models.CharField(max_length=4)
    attrs_type = models.CharField(max_length=21)
    attrs_type_name = models.CharField(max_length=3)
    attrs_type_size = models.CharField(max_length=35)


    refs_E = models.IntegerField(null=True, blank=True)
    refs_OP0 = models.IntegerField(null=True, blank=True)
    refs_OP1 = models.IntegerField(null=True, blank=True)
    refs_OP2 = models.IntegerField(null=True, blank=True)
    refs_args = models.IntegerField(null=True, blank=True)
    refs_body = models.IntegerField(null=True, blank=True)
    refs_bpos = models.IntegerField(null=True, blank=True)
    refs_chain = models.IntegerField(null=True, blank=True)
    refs_chan = models.IntegerField(null=True, blank=True)
    refs_cnst = models.IntegerField(null=True, blank=True)
    refs_cond = models.IntegerField(null=True, blank=True)
    refs_csts = models.IntegerField(null=True, blank=True)
    refs_decl = models.IntegerField(null=True, blank=True)
    refs_domn = models.IntegerField(null=True, blank=True)
    refs_elts = models.IntegerField(null=True, blank=True)
    refs_expr = models.IntegerField(null=True, blank=True)
    refs_flds = models.IntegerField(null=True, blank=True)
    refs_fn = models.IntegerField(null=True, blank=True)
    refs_idx = models.IntegerField(null=True, blank=True)
    refs_init = models.IntegerField(null=True, blank=True)
    refs_labl = models.IntegerField(null=True, blank=True)
    refs_low = models.IntegerField(null=True, blank=True)
    refs_max = models.IntegerField(null=True, blank=True)
    refs_min = models.IntegerField(null=True, blank=True)
    refs_mngl = models.IntegerField(null=True, blank=True)
    refs_name = models.IntegerField(null=True, blank=True)
    refs_prms = models.IntegerField(null=True, blank=True)
    refs_ptd = models.IntegerField(null=True, blank=True)
    refs_purp = models.IntegerField(null=True, blank=True)
    refs_refd = models.IntegerField(null=True, blank=True)
    refs_retn = models.IntegerField(null=True, blank=True)
    refs_scpe = models.IntegerField(null=True, blank=True)
    refs_size = models.IntegerField(null=True, blank=True)
    refs_type = models.IntegerField(null=True, blank=True)
    refs_unql = models.IntegerField(null=True, blank=True)
    refs_val = models.IntegerField(null=True, blank=True)
    refs_valu = models.IntegerField(null=True, blank=True)
    refs_vars = models.IntegerField(null=True, blank=True)
    refs_argt = models.IntegerField(null=True, blank=True)
    
    # E = models.ManyToManyField('self',  related_name='Es')
    # OP0 = models.ManyToManyField('self',  related_name='op0s')
    # OP1 = models.ManyToManyField('self',  related_name='op1s')
    # OP2 = models.ManyToManyField('self',  related_name='op2s')
    # args = models.ManyToManyField('self',  related_name='args_set')
    # body = models.ManyToManyField('self',  related_name='bodys')
    # bpos = models.ManyToManyField('self',  related_name='bposs')
    # chain = models.ManyToManyField('self',  related_name='chains')
    # chan = models.ManyToManyField('self',  related_name='chans')
    # cnst = models.ManyToManyField('self',  related_name='cnts')
    # cond = models.ManyToManyField('self',  related_name='conds')
    # csts = models.ManyToManyField('self',  related_name='csts_set')
    # decl = models.ManyToManyField('self',  related_name='decls')
    # domn = models.ManyToManyField('self',  related_name='domns')
    # elts = models.ManyToManyField('self',  related_name='elts_set')
    # expr = models.ManyToManyField('self',  related_name='exprs')
    # flds = models.ManyToManyField('self',  related_name='flds_set')
    # fn = models.ManyToManyField('self',  related_name='fns')
    # idx = models.ManyToManyField('self',  related_name='idxs')
    # init = models.ManyToManyField('self',  related_name='inits')
    # labl = models.ManyToManyField('self',  related_name='labls')
    # low = models.ManyToManyField('self',  related_name='lows')
    # fmax = models.ManyToManyField('self',  related_name='maxs')
    # fmin = models.ManyToManyField('self',  related_name='mins')
    # mngl = models.ManyToManyField('self',  related_name='mngls')
    # name = models.ManyToManyField('self',  related_name='names')
    # prms = models.ManyToManyField('self',  related_name='prms_set')
    # ptd = models.ManyToManyField('self',  related_name='ptds')
    # purp = models.ManyToManyField('self', related_name='purps')
    # refd = models.ManyToManyField('self', related_name='refds')
    # retn = models.ManyToManyField('self', related_name='retns')
    # scpe = models.ManyToManyField('self', related_name='scpes')
    # size = models.ManyToManyField('self', related_name='sizes')
    # ftype = models.ManyToManyField('self', related_name='types')
    # unql = models.ManyToManyField('self', related_name='unqls')
    # val = models.ManyToManyField('self', related_name='vals')
    # valu = models.ManyToManyField('self', related_name='valus')
    # fvars = models.ManyToManyField('self', related_name='vars_set')
    # argt = CompositeForeignKey('self',
    #                             related_name='argts_set',
    #                            #null=True,
    #                            # unique=False,
    #                            on_delete=models.SET_NULL,
    #                            to_fields={
    #                                'source_file':'source_file',
    #                                'node_id':'refs_argt',
    #                             }
    # )
    E = CompositeForeignKey('self',
                            related_name='E_set',
                            default='',
                            on_delete=models.SET_NULL,
                            to_fields={
                                'source_file':'source_file',
                                'node_id':'refs_E',
        })
    OP0 = CompositeForeignKey('self',
        related_name='OP0_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_OP0',
        })
    OP1 = CompositeForeignKey('self',
        related_name='OP1_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_OP1',
        })
    OP2 = CompositeForeignKey('self',
        related_name='OP2_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_OP2',
        })
    args = CompositeForeignKey('self',
        related_name='args_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_args',
        })
    argt = CompositeForeignKey('self',
        related_name='argt_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_argt',
        })
    body = CompositeForeignKey('self',
        related_name='body_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_body',
        })
    bpos = CompositeForeignKey('self',
        related_name='bpos_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_bpos',
        })
    chain = CompositeForeignKey('self',
        related_name='chain_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_chain',
        })
    chan = CompositeForeignKey('self',
        related_name='chan_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_chan',
        })
    cnst = CompositeForeignKey('self',
        related_name='cnst_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_cnst',
        })
    cond = CompositeForeignKey('self',
        related_name='cond_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_cond',
        })
    csts = CompositeForeignKey('self',
        related_name='csts_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_csts',
        })
    decl = CompositeForeignKey('self',
        related_name='decl_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_decl',
        })
    domn = CompositeForeignKey('self',
        related_name='domn_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_domn',
        })
    elts = CompositeForeignKey('self',
        related_name='elts_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_elts',
        })
    expr = CompositeForeignKey('self',
        related_name='expr_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_expr',
        })
    flds = CompositeForeignKey('self',
        related_name='flds_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_flds',
        })
    fn = CompositeForeignKey('self',
        related_name='fn_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_fn',
        })
    idx = CompositeForeignKey('self',
        related_name='idx_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_idx',
        })
    init = CompositeForeignKey('self',
        related_name='init_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_init',
        })
    labl = CompositeForeignKey('self',
        related_name='labl_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_labl',
        })
    low = CompositeForeignKey('self',
        related_name='low_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_low',
        })
    fmax = CompositeForeignKey('self',
        related_name='max_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_max',
        })
    fmin = CompositeForeignKey('self',
        related_name='min_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_min',
        })
    mngl = CompositeForeignKey('self',
        related_name='mngl_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_mngl',
        })
    name = CompositeForeignKey('self',
        related_name='name_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_name',
        })
    prms = CompositeForeignKey('self',
        related_name='prms_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_prms',
        })
    ptd = CompositeForeignKey('self',
        related_name='ptd_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_ptd',
        })
    purp = CompositeForeignKey('self',
        related_name='purp_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_purp',
        })
    refd = CompositeForeignKey('self',
        related_name='refd_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_refd',
        })
    retn = CompositeForeignKey('self',
        related_name='retn_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_retn',
        })
    scpe = CompositeForeignKey('self',
        related_name='scpe_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_scpe',
        })
    size = CompositeForeignKey('self',
        related_name='size_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_size',
        })
    ftype = CompositeForeignKey('self',
        related_name='type_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_type',
        })
    unql = CompositeForeignKey('self',
        related_name='unql_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_unql',
        })
    val = CompositeForeignKey('self',
        related_name='val_set',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_val',
        })
    valu = CompositeForeignKey('self',
                               related_name='valu_set',
                               #db_column='refs_valu',
                               on_delete=models.SET_NULL,
                               default='',
                               to_fields={
                                   'source_file':'source_file',
                                   'node_id':'refs_valu',
                               })
    fvars = CompositeForeignKey('self',
        related_name='vars_set',
        on_delete=models.SET_NULL,
                                default='',
                                #db_column='refs_vars'             ,
        to_fields={
        'source_file':'source_file',
        'node_id':'refs_vars',
        })


class FuncParams(models.Model):
    source_file= models.ForeignKey(SourceFile,
                                   blank=True,
                                   null=True,
                                   #db_column='source_file_n',
                                   on_delete=models.SET_NULL)
    function_decl  = models.IntegerField(null=False)
    #source_file_num  = models.IntegerField(null=False)
    param_pos  = models.IntegerField(null=False)
    function_param = models.IntegerField(null=False)
    function = CompositeForeignKey('Node',
                                   related_name='func_param_header',
                                   on_delete=models.SET_NULL,
                                   default='',
                                   to_fields={
                                       'source_file':'source_file',
                                       'node_id':'function_decl',
                                })
    parameters = CompositeForeignKey('Node',
        related_name='func_params',
        on_delete=models.SET_NULL,        default='',
        to_fields={
        'source_file':'source_file',
        'node_id':'function_param',
        })
    class Meta:
        unique_together = ('source_file', 'function_param','param_pos','function_param')
