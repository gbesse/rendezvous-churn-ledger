import hashlib
from .common import integer,identifier

def score(key,node):
 a=key.encode();b=node.encode();return int.from_bytes(hashlib.sha256(len(a).to_bytes(4,'big')+a+len(b).to_bytes(4,'big')+b).digest(),'big')
def run(data):
 keys=data['keys'];before=data['before_nodes'];after=data['after_nodes'];replicas=integer(data.get('replicas',1),1,20)
 for values in(keys,before,after):
  if not isinstance(values,list)or len(values)!=len(set(values))or len(values)>5000:raise ValueError('identifiers')
  for v in values:identifier(v)
 if not before or not after or max(len(before),len(after))>100 or len(keys)*(len(before)+len(after))>100000:raise ValueError('bounds')
 def place(key,nodes):return sorted(nodes,key=lambda n:(-score(key,n),n))[:min(replicas,len(nodes))]
 changes=[];moved=0;replaced=0
 for key in keys:
  a=place(key,before);b=place(key,after);count=len(set(b)-set(a));moved+=a!=b;replaced+=count;changes.append({'key':key,'before':a,'after':b,'new_replica_nodes':count,'primary_changed':a[0]!=b[0]})
 return {'placements':changes,'keys_with_changed_ordered_placement':moved,'new_replica_assignments':replaced,'model':'unweighted_sha256_highest_random_weight_hashing_top_r_no_runtime_load_measurement'}
