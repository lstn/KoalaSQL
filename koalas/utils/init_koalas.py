import pandas as pd
from koalas.core import frame

def patch_df():
    setattr(pd.core.frame.DataFrame,
            frame.DataFrame.koalas_cursor.__name__,
            frame.DataFrame.koalas_cursor)