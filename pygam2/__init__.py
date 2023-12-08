"""
GAM toolkit
"""

from __future__ import absolute_import

from pygam2.pygam import GAM
from pygam2.pygam import LinearGAM
from pygam2.pygam import LogisticGAM
from pygam2.pygam import GammaGAM
from pygam2.pygam import PoissonGAM
from pygam2.pygam import InvGaussGAM
from pygam2.pygam import ExpectileGAM

from pygam2.terms import l
from pygam2.terms import s
from pygam2.terms import f
from pygam2.terms import te
from pygam2.terms import intercept

__all__ = ['GAM', 'LinearGAM', 'LogisticGAM', 'GammaGAM', 'PoissonGAM',
           'InvGaussGAM', 'ExpectileGAM', 'l', 's', 'f', 'te', 'intercept']

__version__ = '0.8.0'
