from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-5-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration5Type(Enum):
    VALUE_1_5172229_E21 = 1.5172229e21
    VALUE_3_0376633_E15 = "3.0376633E15"
    VALUE_3_0698753_E_18 = 3.0698753e-18
    FTP_INDUSTRYAND_EWELLTOINTO_ORG = "ftp://industryand.ewelltointo.org"
    VALUE_1_9458620_E10 = "1.9458620E10"
    FTP_FTP_INTHERIGORO_SSYSTEMDEV_LOPMENTTH_NET = (
        "ftp://ftp.intherigoro.ssystemdev.lopmentth.net"
    )
    TELNET_ANDSUCHROBU_TINDICATIO_ANDTHEINFO_MATIONANDOF_NET = (
        "telnet://andsuchrobu.tindicatio.andtheinfo.mationandof.net"
    )
    VALUE_1_7427166_E27 = 1.7427166e27
    FTP_WILL_PERVASI_EPARTNERSH_PS_ORGANIZA_NET = (
        "ftp://willPervasi.epartnersh.psOrganiza.net"
    )


@dataclass(kw_only=True)
class NistschemaSvIvUnionAnyUriFloatEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-5"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-5-NS"

    value: NistschemaSvIvUnionAnyUriFloatEnumeration5Type = field()
