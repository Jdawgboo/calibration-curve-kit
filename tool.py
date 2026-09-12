"""Reliability-bin and Brier score calculations."""
from __future__ import annotations

def brier(probabilities:list[float], outcomes:list[int])->float:
 if len(probabilities)!=len(outcomes): raise ValueError('length mismatch')
 return sum((p-y)**2 for p,y in zip(probabilities,outcomes))/len(probabilities) if probabilities else 0.0

def reliability(probabilities:list[float], outcomes:list[int], bins:int=10)->list[dict]:
 result=[]
 for index in range(bins):
  lower,upper=index/bins,(index+1)/bins; pairs=[(p,y) for p,y in zip(probabilities,outcomes) if lower<=p<(upper if index<bins-1 else upper+1e-12)]
  if pairs: result.append({'lower':lower,'upper':upper,'count':len(pairs),'mean_probability':sum(p for p,_ in pairs)/len(pairs),'event_rate':sum(y for _,y in pairs)/len(pairs)})
 return result

def ece(probabilities:list[float],outcomes:list[int],bins:int=10)->float:
 groups=reliability(probabilities,outcomes,bins); total=len(probabilities)
 return sum(group['count']/total*abs(group['mean_probability']-group['event_rate']) for group in groups) if total else 0.0
if __name__=='__main__':
 import json,sys; p=json.load(sys.stdin); print(json.dumps({'brier':brier(p['probabilities'],p['outcomes']),'ece':ece(p['probabilities'],p['outcomes'])},indent=2))
