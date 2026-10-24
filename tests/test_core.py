import unittest,subprocess,sys,os,json
from rendezvous_churn_ledger import run
from rendezvous_churn_ledger.core import score
class Tests(unittest.TestCase):
 def test_removing_node_only_changes_keys_that_used_it(self):
  r=run({'keys':[str(i)for i in range(100)],'before_nodes':['a','b','c'],'after_nodes':['a','b'],'replicas':1})
  for p in r['placements']:
   if p['before'][0]!='c':self.assertEqual(p['before'],p['after'])
 def test_addition_preserves_existing_relative_order(self):
  r=run({'keys':[str(i)for i in range(50)],'before_nodes':['a','b','c'],'after_nodes':['a','b','c','d'],'replicas':3})
  for p in r['placements']:self.assertEqual([n for n in p['after']if n!='d'],[n for n in p['before']if n in p['after']])
 def test_length_prefix_avoids_concatenation_alias(self):self.assertNotEqual(score('ab','c'),score('a','bc'))
 def test_python_hashseed_does_not_change_placement(self):
  code='import json;from rendezvous_churn_ledger import run;print(json.dumps(run({"keys":["x"],"before_nodes":["a","b"],"after_nodes":["b","a"]}),sort_keys=True))';outputs=[]
  for seed in ('1','19'):outputs.append(subprocess.check_output([sys.executable,'-c',code],env={**os.environ,'PYTHONHASHSEED':seed},text=True))
  self.assertEqual(*outputs)
