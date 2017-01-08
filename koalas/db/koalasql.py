import pandas as pd

class Cursor:
    _cur_val = None

    def __init__(self, tables):
        self.db = {k: tables[k] for k in tables.keys() if isinstance(tables[k], pd.DataFrame)}

    def execute(self):
        pass
    
    def fetchall(self):
        return self._cur_val

    def get_df(self, name):
        return self.db.get(name, None)