"""
This is a boilerplate pipeline 'dataprocessing'
generated using Kedro 0.19.6
"""

import pandas as pd


def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    return x.str.replace("%", "").astype(float)


def _parse_money(x: pd.Series) -> pd.Series:
    return x.str.replace("$", "").str.replace(",", "").astype(float)


# Let's create two preprocessing functions, one for companies and one for shuttles


def preprocess_companies(df: pd.DataFrame) -> pd.DataFrame:
    df["iata-approved"] = _is_true(df["iata-approved"])
    df["company_rating"] = _parse_percentage(df["company_rating"])
    return df


def preprocess_shuttles(df: pd.DataFrame) -> pd.DataFrame:
    df["d_check_complete"] = _is_true(df["d_check_complete"])
    df["moon_clearance_complete"] = _is_true(df["moon_clearance_complete"])
    df[["price"]] = _parse_money(df[["price"]])
