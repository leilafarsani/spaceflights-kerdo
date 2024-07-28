"""
This is a boilerplate pipeline 'dataprocessing'
generated using Kedro 0.19.6
"""

import pandas as pd

def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"

def _parse_percentage(x: pd.Series)-> pd.Series:
      return x.str.replace('%','').astype(float)
  
def _parse_money(x: pd.Series)-> pd.Series:
      return x.str.replace('$','').str.replace(',','').astype(float)