from tkinter import Label
from pandas import DataFrame, Series
from typing import Any, List, Dict

def rows(frame: DataFrame, have_header=True) -> Dict[str, float]:
  d = {
      True: _rows_with_header_,
      False: _rows_}
  return switch(have_header, d)(frame)

def _rows_with_header_(frame: DataFrame) -> Dict[str, float]:
  kv = {}
  for row in list(frame.iloc):
    kv[row.values[0]] = list(row.values[1:])
  return kv

def _rows_(frame: DataFrame) -> Dict[str, float]:
  kv = {}
  indexes = list(frame.iloc)
  for (row, index) in zip(indexes, range(len(indexes))):
    kv[index] = list(row)
  return kv
  

def columns(frame: DataFrame) -> Dict[str, float]:
  kv = {}
  for column in frame.columns[1:]:
    kv[column] = list(frame[column].values)
  return kv

def _columns_(frame: DataFrame) -> Dict[str, float]:
  kv = {}
  for column in frame.columns[1:]:
    kv[column] = list(frame[column].values)
  return kv


# def _columns_(frame: DataFrame) -> Dict[str, float]:
#   kv = {}
#   for (column, index) in zip(list(frame.columns), range(len(frame.columns))):
#     kv[index] = list(frame[column].values)
#   return kv


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
