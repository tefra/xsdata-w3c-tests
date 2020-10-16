from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-4-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration4Type(Enum):
    """
    :cvar VALUE_3_0698753_E_18:
    :cvar TELNET_TOINVOLVE_GOV:
    :cvar GOPHER_SUCHKNOWNEN_UREORGANIZ_TIONSSUCCE_STHE_EDU:
    :cvar VALUE_3_4028235_E38:
    :cvar FTP_FTP_TECH_GOV:
    :cvar NEWS_AR_ORG:
    :cvar MAILTO_MANUA_WIDELY_A_ORG:
    :cvar FTP_FTP_G_ORG:
    """
    VALUE_3_0698753_E_18 = "3.0698753E-18"
    TELNET_TOINVOLVE_GOV = "telnet://toinvolve.gov"
    GOPHER_SUCHKNOWNEN_UREORGANIZ_TIONSSUCCE_STHE_EDU = "gopher://suchknownen.ureorganiz.tionssucce.sthe.edu"
    VALUE_3_4028235_E38 = "3.4028235E38"
    FTP_FTP_TECH_GOV = "ftp://ftp.tech.gov"
    NEWS_AR_ORG = "news://ar.org"
    MAILTO_MANUA_WIDELY_A_ORG = "mailto:manua@widelyA.org"
    FTP_FTP_G_ORG = "ftp://ftp.g.org"


@dataclass
class NistschemaSvIvUnionAnyUriFloatEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-4"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-4-NS"

    value: Optional[NistschemaSvIvUnionAnyUriFloatEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
