from __future__ import annotations
from typing import Dict, List
from pandas import DataFrame
from copy import deepcopy, copy
from frame import rows, columns, ifNone, switch, empty_list
from enum import Enum

class SetOption(Enum):
  ROW = 1
  COLUMN = 2
  NEXT = 3
  AUTO = 4




class DataTable(object):
  
  def __init__(self, frame: DataFrame, header_row=False, header_column=False):
    self.frame = frame
    self.rows = rows(frame, header_row)
    self.columns = columns(frame)
    self.columns_result: Dict[str, List[float]] = {}
    self.rows_result: Dict[str, List[float]] = {}
    self.special: Dict[str, List[float]] = {}
    self.header_row = header_row
    self.header_column = header_column

  @property
  def count_column(self):
    return len(self.columns)
  
  @property
  def count_row(self):
    return len(self.rows)
  
  @property
  def count_column_result(self):
    return len(self.columns_result)
  
  @property
  def count_rows_result(self):
    return len(self.rows_result)

    
  @property
  def count_special(self):
    return len(self.special)

  def from_rows(self, func: function) -> DataTable:
    (key, value, option) = func(list(self.rows.values()))
    result = {}
    result[key] = value
    set_option = SetOption.COLUMN if option == SetOption.AUTO else option
    return self.set_result(set_option, result)

  def from_columns(self, func: function) -> DataTable:
    (key, value, option) = func(list(self.columns.values()))
    result = {}
    result[key] = value
    set_option = SetOption.ROW if option == SetOption.AUTO else option
    return self.set_result(set_option, result)

  def for_row(self, key: str, func: function) -> DataTable:
    result = { key: [] }
    for row in self.rows.values():
      result[key].append(func(row))
    return self.set_result(SetOption.ROW, result)

  def for_column(self, key: str, func: function) -> DataTable:
    result = { key: [] }
    for column in self.columns:
      result[key].append(func(self.columns[column]))
    return self.set_result(SetOption.COLUMN, result)

  def from_custom_column(self, columns: List[str], func: function, name: str) -> DataTable:
    columns = self.get_lists(columns, self.columns)
    (_, value, option) = func(columns)
    result = {}
    result[name] = value
    set_option = SetOption.ROW if option == SetOption.AUTO else option
    return self.set_result(set_option, result)

  def custom(self, func:function) -> DataTable:
    (key, value, option) = func(self.columns, self.rows, self.columns_result, self.rows_result, self.special)
    result = {}
    result[key] = value
    return self.set_result(option, result)

    pass

  def get_lists(self, keys: List[str], dict: Dict[str, int]) -> List[List[int]]:
    result:List[List[int]] = []
    for key in keys:
      result.append(dict[key])
    return result
     

  def dataframe(self) -> DataFrame:
    frame = copy(self.frame)
    for column in self.columns_result:
      frame.loc[column] = [""] + self.columns_result[column]
    
    for row in self.rows_result:
      frame[row] = self.rows_result[row] + empty_list(self.count_column_result)
    
    for special in self.special:
      frame.loc[special] = self.special[special] + empty_list(self.count_column + self.count_rows_result)

    return frame 

  def set_result(self, option: SetOption, result: Dict[str, List[float]]):
    d = {
      SetOption.ROW: lambda : self.add_row(result),
      SetOption.COLUMN: lambda : self.add_column(result),
      SetOption.NEXT: lambda : self.add_special(result)}
    return switch(option, d)()
    
  def add_row(self, kv: Dict[str, List[float]]):
    result = copy(self.rows_result)
    for k in kv:
      result[k] = kv[k]
    return self._with(rows_result=result)

  def add_column(self, kv: Dict[str, List[float]]):
    result = copy(self.columns_result)
    for k in kv:
      result[k] = kv[k]
    return self._with(columns_result=result)

  def add_special(self, kv: Dict[str, List[float]]):
    result = copy(self.special)
    for k in kv:
      result[k] = kv[k]
    return self._with(special=result)

  def _with(self, frame = None, rows = None, columns = None, columns_result = None, rows_result = None, special = None) -> DataTable:
    result = deepcopy(self)
    result.frame = ifNone(frame, self.frame)
    result.rows = ifNone(rows, self.rows)
    result.columns = ifNone(columns, self.columns)
    result.columns_result = ifNone(columns_result, self.columns_result)
    result.rows_result = ifNone(rows_result, self.rows_result)
    result.special = ifNone(special, self.special)
    return result
    
  


  

  

