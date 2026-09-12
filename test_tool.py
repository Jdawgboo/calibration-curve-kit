import unittest
from tool import brier,ece,reliability
class CalibrationTests(unittest.TestCase):
 def test_scores(self):
  self.assertEqual(brier([0,1],[0,1]),0); self.assertAlmostEqual(brier([.5,.5],[0,1]),.25); self.assertEqual(len(reliability([.2,.8],[0,1],2)),2); self.assertGreater(ece([.2,.8],[0,1],2),0)
if __name__=='__main__': unittest.main()
