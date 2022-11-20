from __future__ import annotations
import pandas as pd
from frame import rows, columns, ifNone
from table import DataTable
from analysis import RMSD, cov2, line_regress, mean, cov, dispersion, regression_a, regression_b, line_regress_func, correlation_coefficient, R2, F_criterion


def test1():
  test1: str = r"TEST.xlsx"
  frame: pd.DataFrame = pd.read_excel(test1, na_filter=False)
  table = DataTable(frame)
  print(table.for_row("mean", mean).for_column("mean", mean).dataframe())


def test2():
  test2: str = r"TEST 2.xlsx"
  frame: pd.DataFrame = pd.read_excel(test2, na_filter=False)
  table = DataTable(frame)
  result = (table
            .from_rows(cov)
            .from_rows(cov2)
            .for_row("dispersion", dispersion)
            .for_row("RMSD", RMSD)
            .from_rows(F_criterion(1))
            .from_rows(R2)
            .from_rows(line_regress)
            .from_rows(regression_a)
            .from_rows(regression_b)
            .from_rows(line_regress_func)
            .from_rows(correlation_coefficient)
            .dataframe())
  result.to_excel("newFile.xlsx")
  

def main():
  test2()

if __name__ == "__main__":
  main()


