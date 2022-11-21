from __future__ import annotations
import pandas as pd
from frame import rows, columns, ifNone
from table import DataTable, SetOption
from analysis import Mb, S2rest, Srest, average_approximation_error, line_regress, F_fact_criterion, RMSD, cov2, line_regress, mean, cov, dispersion, regression_a, regression_b, line_regress_func, correlation_coefficient, R2, F_criterion, t_Student


def test1():
  test1: str = r"TEST.xlsx"
  frame: pd.DataFrame = pd.read_excel(test1, na_filter=False)
  table = DataTable(frame)
  print(table.for_row("mean", mean).for_column("mean", mean).dataframe())


def test2():
  test2: str = r"TEST 2.xlsx"
  frame: pd.DataFrame = pd.read_excel(test2, na_filter=False)
  table = DataTable(frame, header_row=True, header_column=True)
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
  print(result)
  # result.to_excel("newFile.xlsx")

def test3():
  test3: str = r"TEST3.xlsx"
  frame: pd.DataFrame = pd.read_excel(test3)
  table = DataTable(frame, header_row=True)
  result = (
    table
    .for_column("q2", dispersion)
    .for_column("q", RMSD)
    .from_columns(cov2)
    .from_columns(correlation_coefficient)
    .from_columns(regression_b)
    .from_columns(R2)
    .from_columns(F_fact_criterion(7))
    .from_columns(line_regress)
    .from_columns(S2rest(1))
    .from_columns(Srest(1))
    .from_columns(Mb(1))
    .from_columns(t_Student(1))
    .from_columns(average_approximation_error)
    .dataframe())
  result.to_excel("Задание8.xlsx")
  # print(result)
  

def main():
  test3()

if __name__ == "__main__":
  main()


