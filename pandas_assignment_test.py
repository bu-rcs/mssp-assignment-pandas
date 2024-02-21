import pandas_assignment as pa
import pandas as pd
import pytest

def test_problem1():
    df = pa.problem1("dataset/2022-2023_NBA_Player_Stats_Regular.csv")
    assert(len(df) == 679)
    assert(df.loc[0, "Player"] == "Precious Achiuwa")
    
def test_problem2():
    df = pa.problem2("dataset/2022-2023_NBA_Player_Stats_Regular.csv")
    assert(df.iloc[0, 1] == "Jayson Tatum")
    assert(df.iloc[1, 1] == "Jaylen Brown")

def test_problem3():
    df = pa.problem3("dataset/2022-2023_NBA_Player_Stats_Regular.csv")
    assert(isinstance(df, pd.DataFrame)) 
    assert(df.loc["C"].iloc[0] == pytest.approx(26.52) )
    assert(df.loc["PG"].iloc[0] == pytest.approx(26.95))

def test_problem4():
    df = pa.problem4("dataset/2022-2023_NBA_Player_Stats_Regular.csv")
    assert(isinstance(df, pd.DataFrame))
    assert(len(df) == 539)
    assert(df["Tm"].loc[6].iloc[0] == "TOT, UTA, MIN")