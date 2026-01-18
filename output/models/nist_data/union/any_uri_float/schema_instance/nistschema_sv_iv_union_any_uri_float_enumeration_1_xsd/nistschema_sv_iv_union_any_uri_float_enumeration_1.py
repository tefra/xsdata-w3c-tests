from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-1-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration1Type(Enum):
    TELNET_TOINVOLVE_GOV = "telnet://toinvolve.gov"
    VALUE_3_3221344_E9 = "3.3221344E9"
    FTP_WILL_PERVASI_EPARTNERSH_PS_ORGANIZA_NET = (
        "ftp://willPervasi.epartnersh.psOrganiza.net"
    )
    FTP_THATGUIDEL_ORG = "ftp://thatguidel.org"
    HTTP_TH_ORG = "http://th.org"
    HTTP_DIVISIONSPA_T_EDU = "http://divisionspa.t.edu"


@dataclass(kw_only=True)
class NistschemaSvIvUnionAnyUriFloatEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-1-NS"

    value: NistschemaSvIvUnionAnyUriFloatEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
