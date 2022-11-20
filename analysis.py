from math import sqrt
from typing import List, Dict, Tuple
from frame import powLst, toFixed

from table import SetOption


def mean(lst: List) -> float:
  return sum(lst)/len(lst)


def meanIndex(lst: List[int]) -> List[float]:
  meanI = mean(lst)
  result = []
  for value in lst:
    result.append(value - meanI)
  return result

def cov(lst: List[List[int]]) -> Tuple[str, List[float], SetOption]:
  result = _cov_(lst[0], lst[1])
  return ("cov", [result], SetOption.NEXT)

def cov2(lst: List[List[int]]) -> Tuple[str, List[float], SetOption]:
  result = _cov2_(lst[0], lst[1])
  return ("cov2", [result], SetOption.NEXT)


def _cov2_(x: List[int], y: List[int]) -> float:
  xy = []
  meanX = mean(x)
  meanY = mean(y)
  for (x1, y1) in zip(x, y):
    xy.append(x1 * y1)
  _meanXY = mean(xy)

  return _meanXY - meanX * meanY

def _cov_(x: List[int], y: List[int]) -> float:
  mean_index_x = meanIndex(x)
  mean_index_y = meanIndex(y)
  product = []
  for (meanX, meanY) in zip(mean_index_x, mean_index_y):
    product.append(meanX * meanY)
  result = sum(product) / (len(product)-1)
  return result

def dispersion(lst: List[int]) -> float:
  avgX = meanIndex(lst)
  avg_pow = []
  for i in avgX:
    avg_pow.append(pow(i, 2))
  return sum(avg_pow)/len(lst)

def RMSD(lst: List[int]) -> float:
  return sqrt(dispersion(lst))

def regression_b(lst: List[List[int]]) -> Tuple[str, List[float], SetOption]:
  result = _regression_b_(lst[0], lst[1])
  return ("b", [result], SetOption.NEXT)

def regression_a(lst: List[List[int]]) -> float:
  result = _regression_a_(lst[0], lst[1])
  return ("a", [result], SetOption.NEXT)

def _regression_a_(x: List[int], y: List[int]) -> float:
  meanX = mean(x)
  meanY = mean(y)
  b = _regression_b_(x, y)
  a = meanY - b * meanX
  return a 

def line_regress_func(lst: List[List[int]]) -> Tuple[str, List[str], SetOption]:
  x = lst[0]
  y = lst[1]
  a = _regression_a_(x, y)
  b = _regression_b_(x, y)
  return ( "line_regress_func", [f"y = {toFixed(a, 2)} + {toFixed(b, 2)}*x"], SetOption.NEXT )

def line_regress(lst: List[List[int]]) -> Tuple[str, List[float], SetOption]:
  x = lst[0]
  y = lst[1]
  f = _line_regress_(x, y)
  result = []
  for v in x:
    result.append(f(v))
  return ("y^", result, SetOption.COLUMN)

def _line_regress_(x: List[int], y: List[int]):
  a = _regression_a_(x, y)
  b = _regression_b_(x, y)
  return lambda v : a + b * v

  

def _regression_b_(x: List[int], y: List[int]) -> float:
  powX = powLst(x)
  meanX = sum(powX)/len(powX)
  mean_sumX = pow(sum(x) / len(x), 2)
  q = meanX - mean_sumX
  _cov = _cov2_(x, y) # rofl
  return _cov / q

def correlation_coefficient(lst: List[List[int]]) -> Tuple[str, List[float], SetOption]:
  result = _correlation_coefficient_(lst[0], lst[1])
  return ("коэффициент Пирсона", [result], SetOption.NEXT) 

def _correlation_coefficient_(x: List[int], y: List[int]) -> float:
  _cov2 = _cov2_(x, y)
  rmsdX = RMSD(x)
  rmsdY = RMSD(y)
  return (_cov2 / (rmsdX * rmsdY))

def R2(lst: List[List[int]]) -> Tuple[str, List[float], SetOption]:
  result = _R2_(lst[0], lst[1])
  return ("R2", [result], SetOption.NEXT)

def _R2_(x: List[int], y: List[int]) -> float:
  sse = _SSE_(x, y)
  sst = _SST_(y)
  return 1 - (sse/sst)

def _SSE_(x: List[int], y: List[int]) -> float:
  regress_f = _line_regress_(x, y)
  regressY = []
  for v in x:
    regressY.append(regress_f(v))
  result = []
  for (y1, yR) in zip(regressY, y):
    result.append(pow(y1 - yR, 2))
  return sum(result)

def _SST_(y: List[int]) -> float:
  meanY = meanIndex(y)
  powY = []
  for v in meanY:
    powY.append(pow(v, 2))
  return sum(powY)

def F_criterion(n): # n - количество наблюдений 
  return lambda lst: ("F критерий", [_F_criterion_(lst[0], lst[1])(n)], SetOption.NEXT)

def _F_criterion_(x: List[int], y: List[int]):
  s2fact = _S2fact_(x, y)
  S2rest_f = _S2rest_(x, y)
  return lambda n: s2fact/(S2rest_f(n))

def _S2fact_(x: List[int], y: List[int]) -> float:
  regress_f = _line_regress_(x, y)
  regressY = []
  for v in x:
    regressY.append(regress_f(v))
  meanY = mean(y)
  result = [] 
  for v in regressY:
    result.append(pow(v - meanY, 2))
  return sum(result)/len(x)


def _S2rest_(x: List[int], y: List[int]): # формула расчета факторной дисперсии
  sse = _SSE_(x, y)
  return lambda n: sse/(n - len(x) - 1)









