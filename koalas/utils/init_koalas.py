from sys import modules as sm
from types import ModuleType
import pandas as pd
from koalas.hooks import frame

__smg = lambda: sm.get('pandas._ext', None)

def patch_pandas_ext_ns():
    if __smg() is None:
        modu = ModuleType('pandas._ext')
        sm['pandas._ext'] = modu
        setattr(sm['pandas'], '_ext', modu)
        setattr(sm['pandas._ext'], 'koalas', sm['koalas'])
    

def patch_df():
    if __smg() is None and 'koalas' not in dir(__smg()):
        setattr(pd.core.frame.DataFrame,
                frame.DataFrame.koalas_cursor.__name__,
                frame.DataFrame.koalas_cursor)