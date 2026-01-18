from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-3-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration3Type(Enum):
    GOPHER_SUCHKNOWNEN_UREORGANIZ_TIONSSUCCE_STHE_EDU = (
        "gopher://suchknownen.ureorganiz.tionssucce.sthe.edu"
    )
    MAILTO_D_TOTOOLSASOFANDTOOLSFORLAWWHICHANDREGISTRY_GOV = (
        "mailto:d@totoolsasofandtoolsforlawwhichandregistry.gov"
    )
    VALUE_2_0588983_E18 = 2.0588983e18
    VALUE_3_4028235_E38 = 3.4028235e38
    VALUE_1_4_E_45 = 1.4e-45
    NEWS_AR_ORG = "news://ar.org"
    FTP_FTP_INTHERIGORO_SSYSTEMDEV_LOPMENTTH_NET = (
        "ftp://ftp.intherigoro.ssystemdev.lopmentth.net"
    )
    VALUE_3_3041671_E_5 = "3.3041671E-5"
    NEWS_FULLOVERWIR_LESSAPPLIC_TIONSPROVI_ETOABILI_ORG = (
        "news://fulloverwir.lessapplic.tionsprovi.etoabili.org"
    )


@dataclass(kw_only=True)
class NistschemaSvIvUnionAnyUriFloatEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-3"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-3-NS"

    value: NistschemaSvIvUnionAnyUriFloatEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
