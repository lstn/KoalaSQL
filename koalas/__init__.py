# import pkg_resources
# import pandas
from koalas.utils import init_koalas

init_koalas.patch_df()

# patch pandas namespace
init_koalas.patch_pandas_ext_ns()

