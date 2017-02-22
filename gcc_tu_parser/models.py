import django
from django.db import models

    
class SourceFile(models.Model):
    filename = models.CharField(max_length=228)
    
class Node(models.Model):
    source_file= models.ForeignKey(SourceFile,
                                   blank=True,
                                   null=True,
                                   on_delete=models.SET_NULL)
    node_id= models.IntegerField()
    node_type = models.CharField(max_length=40)
    
    class Meta:
        unique_together = (('source_file', 'node_id'),)
        
    refs_argt = models.IntegerField(null=True, blank=True)
    refs_prms = models.IntegerField(null=True, blank=True)
    attrs_string = models.CharField(max_length=228)
    refs_domn = models.IntegerField(null=True, blank=True)
    refs_retn = models.IntegerField(null=True, blank=True)
    refs_bpos = models.IntegerField(null=True, blank=True)
    refs_max = models.IntegerField(null=True, blank=True)
    refs_csts = models.IntegerField(null=True, blank=True)
    refs_valu = models.IntegerField(null=True, blank=True)
    refs_min = models.IntegerField(null=True, blank=True)
    refs_name = models.IntegerField(null=True, blank=True)
    refs_size = models.IntegerField(null=True, blank=True)
    refs_type = models.IntegerField(null=True, blank=True)
    refs_unql = models.IntegerField(null=True, blank=True)
    refs_val = models.IntegerField(null=True, blank=True)
    refs_args = models.IntegerField(null=True, blank=True)
    refs_elts = models.IntegerField(null=True, blank=True)
    refs_refd = models.IntegerField(null=True, blank=True)
    refs_low = models.IntegerField(null=True, blank=True)
    refs_body = models.IntegerField(null=True, blank=True)
    refs_purp = models.IntegerField(null=True, blank=True)
    refs_chan = models.IntegerField(null=True, blank=True)
    #type = models.IntegerField(null=True, blank=True)
    refs_cnst = models.IntegerField(null=True, blank=True)
    attrs_type_name = models.CharField(max_length=3)
    refs_fn = models.IntegerField(null=True, blank=True)
    refs_chain = models.IntegerField(null=True, blank=True)
    refs_ptd = models.IntegerField(null=True, blank=True)
    refs_mngl = models.IntegerField(null=True, blank=True)
    #nid = models.IntegerField(null=True, blank=True)
    refs_cond = models.IntegerField(null=True, blank=True)
    refs_vars = models.IntegerField(null=True, blank=True)
    refs_OP0 = models.IntegerField(null=True, blank=True)
    refs_OP1 = models.IntegerField(null=True, blank=True)
    refs_OP2 = models.IntegerField(null=True, blank=True)
    refs_E = models.IntegerField(null=True, blank=True)
    attrs_note = models.CharField(max_length=4)
    refs_idx = models.IntegerField(null=True, blank=True)
    refs_scpe = models.IntegerField(null=True, blank=True)
    refs_flds = models.IntegerField(null=True, blank=True)
    attrs_type_size = models.CharField(max_length=35)
    refs_init = models.IntegerField(null=True, blank=True)
    refs_expr = models.IntegerField(null=True, blank=True)
    attrs_addr = models.CharField(max_length=12)
    refs_decl = models.IntegerField(null=True, blank=True)
    refs_labl = models.IntegerField(null=True, blank=True)
    attrs_type = models.CharField(max_length=21)
