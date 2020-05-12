from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-3-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration3Type(Enum):
    """
    :cvar GOPHER_SUCHKNOWNEN_UREORGANIZ_TIONSSUCCE_STHE_EDU:
    :cvar MAILTO_D_TOTOOLSASOFANDTOOLSFORLAWWHICHANDREGISTRY_GOV:
    :cvar VALUE_2_0588983_E18:
    :cvar VALUE_3_4028235_E38:
    :cvar VALUE_1_4_E_45:
    :cvar NEWS_AR_ORG:
    :cvar FTP_FTP_INTHERIGORO_SSYSTEMDEV_LOPMENTTH_NET:
    :cvar VALUE_3_3041671_E_5:
    :cvar NEWS_FULLOVERWIR_LESSAPPLIC_TIONSPROVI_ETOABILI_ORG:
    """
    GOPHER_SUCHKNOWNEN_UREORGANIZ_TIONSSUCCE_STHE_EDU = "gopher://suchknownen.ureorganiz.tionssucce.sthe.edu"
    MAILTO_D_TOTOOLSASOFANDTOOLSFORLAWWHICHANDREGISTRY_GOV = "mailto:d@totoolsasofandtoolsforlawwhichandregistry.gov"
    VALUE_2_0588983_E18 = "2.0588983E18"
    VALUE_3_4028235_E38 = "3.4028235E38"
    VALUE_1_4_E_45 = "1.4E-45"
    NEWS_AR_ORG = "news://ar.org"
    FTP_FTP_INTHERIGORO_SSYSTEMDEV_LOPMENTTH_NET = "ftp://ftp.intherigoro.ssystemdev.lopmentth.net"
    VALUE_3_3041671_E_5 = "3.3041671E-5"
    NEWS_FULLOVERWIR_LESSAPPLIC_TIONSPROVI_ETOABILI_ORG = "news://fulloverwir.lessapplic.tionsprovi.etoabili.org"


@dataclass
class NistschemaSvIvUnionAnyUriFloatEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-3"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-3-NS"

    value: Optional[NistschemaSvIvUnionAnyUriFloatEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
