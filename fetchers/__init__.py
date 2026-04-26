"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .adidas import AdidasFetcher
from .eclat import EclatFetcher
from .far_eastern import FarEasternFetcher
from .fast_retailing import FastRetailingFetcher
from .formosa_taffeta import FormosaTaffetaFetcher
from .hm import HmFetcher
from .inditex import InditexFetcher
from .lealea import LealeaFetcher
from .lenzing import LenzingFetcher
from .lululemon import LululemonFetcher
from .makalot import MakalotFetcher
from .nike import NikeFetcher
from .pvh import PvhFetcher
from .shenzhou import ShenzhouFetcher
from .tapestry import TapestryFetcher
from .toray import TorayFetcher
from .vf_corp import VfCorpFetcher

FETCHERS = {
    "adidas": AdidasFetcher,
    "eclat": EclatFetcher,
    "far_eastern": FarEasternFetcher,
    "fast_retailing": FastRetailingFetcher,
    "formosa_taffeta": FormosaTaffetaFetcher,
    "hm": HmFetcher,
    "inditex": InditexFetcher,
    "lealea": LealeaFetcher,
    "lenzing": LenzingFetcher,
    "lululemon": LululemonFetcher,
    "makalot": MakalotFetcher,
    "nike": NikeFetcher,
    "pvh": PvhFetcher,
    "shenzhou": ShenzhouFetcher,
    "tapestry": TapestryFetcher,
    "toray": TorayFetcher,
    "vf_corp": VfCorpFetcher,
}
