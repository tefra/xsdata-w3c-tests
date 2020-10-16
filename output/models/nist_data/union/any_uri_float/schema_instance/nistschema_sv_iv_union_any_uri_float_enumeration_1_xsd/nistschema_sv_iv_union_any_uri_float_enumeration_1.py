from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-1-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration1Type(Enum):
    """
    :cvar TELNET_TOINVOLVE_GOV:
    :cvar VALUE_3_3221344_E9:
    :cvar FTP_WILL_PERVASI_EPARTNERSH_PS_ORGANIZA_NET:
    :cvar FTP_THATGUIDEL_ORG:
    :cvar HTTP_TH_ORG:
    :cvar HTTP_DIVISIONSPA_T_EDU:
    """
    TELNET_TOINVOLVE_GOV = "telnet://toinvolve.gov"
    VALUE_3_3221344_E9 = "3.3221344E9"
    FTP_WILL_PERVASI_EPARTNERSH_PS_ORGANIZA_NET = "ftp://willPervasi.epartnersh.psOrganiza.net"
    FTP_THATGUIDEL_ORG = "ftp://thatguidel.org"
    HTTP_TH_ORG = "http://th.org"
    HTTP_DIVISIONSPA_T_EDU = "http://divisionspa.t.edu"


@dataclass
class NistschemaSvIvUnionAnyUriFloatEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-1-NS"

    value: Optional[NistschemaSvIvUnionAnyUriFloatEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
