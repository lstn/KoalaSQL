# import inspect
from koalas.db import koalasql

class DataFrame:
    def koalas_cursor(self):
        # _cf = inspect.currentframe()
        # try:
            # _caller = _cf.f_back
            # print(_caller.f_builtins)
            # print(_caller.f_globals)
            # print(_caller.f_locals)
            # print("Call")
        # finally:
            # del _cf
        return koalasql.Cursor({ "self": self })