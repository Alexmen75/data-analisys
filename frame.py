from tkinter import Label
from pandas import DataFrame, Series
from typing import Any, List, Dict

def rows(frame: DataFrame) -> Dict[str, float]:
  kv = {}
  for row in list(frame.iloc):
    kv[row.values[0]] = list(row.values[1:])
  return kv

def columns(frame: DataFrame) -> Dict[str, float]:
  kv = {}
  for column in frame.columns[1:]:
    kv[column] = list(frame[column].values)
  return kv

def ifNone(item1: Any, item2: Any):
  result = item1 if item1 != None else item2
  return result

def empty_list(number: int) -> List[str]:
  result = []
  for _ in range(number):
    result.append("")
  return result

def switch(value: Any, case: Dict[Any, Any]):
  return case[value]

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
  
def powLst(lst: List[int], degree: int=2) -> List[float]:
  powX = []
  for x in lst:
    powX.append(pow(x, degree))
  return powX
