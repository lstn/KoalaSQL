import pandas as pd

class Cursor:
    _cur_val = None
    arraysize = 1
    description = None
    rowcount = -1

    def __init__(self, tables):
        self.db = {k: tables[k] for k in tables.keys() if isinstance(tables[k], pd.DataFrame)}

    def close(self):
        pass

    def execute(self, operation, *args, **kwargs):
        pass
        
    def executemany(self):
        pass

    def fetchone(self):
        return self._cur_val

    def fetchmany(self, size=None):
        size = self.arraysize if size is None else size
        return self._cur_val

    def fetchall(self):
        return self._cur_val
    
    def setinputsizes(self, sizes):
        pass
    
    def setoutputsizes(self, size, column=None):
        pass

    def get_df(self, name):
        return self.db.get(name, None)