from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-4-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration4Type(Enum):
    VALUE_3_0698753_E_18 = 3.0698753e-18
    TELNET_TOINVOLVE_GOV = "telnet://toinvolve.gov"
    GOPHER_SUCHKNOWNEN_UREORGANIZ_TIONSSUCCE_STHE_EDU = (
        "gopher://suchknownen.ureorganiz.tionssucce.sthe.edu"
    )
    VALUE_3_4028235_E38 = 3.4028235e38
    FTP_FTP_TECH_GOV = "ftp://ftp.tech.gov"
    NEWS_AR_ORG = "news://ar.org"
    MAILTO_MANUA_WIDELY_A_ORG = "mailto:manua@widelyA.org"
    FTP_FTP_G_ORG = "ftp://ftp.g.org"


@dataclass(kw_only=True)
class NistschemaSvIvUnionAnyUriFloatEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-4"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-4-NS"

    value: NistschemaSvIvUnionAnyUriFloatEnumeration4Type = field()
