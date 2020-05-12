from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-1-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration1Type(Enum):
    """
    :cvar FTP_THATGUIDEL_ORG:
    :cvar FTP_WILL_PERVASI_EPARTNERSH_PS_ORGANIZA_NET:
    :cvar HTTP_DIVISIONSPA_T_EDU:
    :cvar HTTP_TH_ORG:
    :cvar TELNET_TOINVOLVE_GOV:
    :cvar VALUE_3_3221344_E9:
    """
    FTP_THATGUIDEL_ORG = "ftp://thatguidel.org"
    FTP_WILL_PERVASI_EPARTNERSH_PS_ORGANIZA_NET = "ftp://willPervasi.epartnersh.psOrganiza.net"
    HTTP_DIVISIONSPA_T_EDU = "http://divisionspa.t.edu"
    HTTP_TH_ORG = "http://th.org"
    TELNET_TOINVOLVE_GOV = "telnet://toinvolve.gov"
    VALUE_3_3221344_E9 = "3.3221344E9"


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
        metadata=dict(
            required=True
        )
    )
