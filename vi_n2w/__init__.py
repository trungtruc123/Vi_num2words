import sys

# Check python version
try:
    version_info = sys.version_info
    if version_info < (3, 7, 0):
        raise RuntimeError("Vinflection requires Python 3.7 or later")
except Exception:
    pass



###########################################################
# TOP-LEVEL MODULES
###########################################################

from vi_n2w.w2n import w2n
from vi_n2w.n2w import n2w

__all__ = ['w2n', 'n2w']
