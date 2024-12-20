from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-3-NS"


class NistschemaSvIvAtomicAnyUriEnumeration3Type(Enum):
    HTTP_WWW_APISIN_COMPU_INGTE_COM = "http://www.APIsinCompu.ingte.com"
    TELNET_ACADEMI_ORG = "telnet://academi.org"
    GOPHER_THATOVER_JAV_THROUGHT_COM = "gopher://thatoverJav.throught.com"
    HTTP_WWW_ENSUREADDRE_SASSPECIFI_ATIONSIMAG_SANDST_ORG = (
        "http://www.ensureaddre.sasspecifi.ationsimag.sandst.org"
    )
    FTP_FTP_PROT_EDU = "ftp://ftp.prot.edu"
    FTP_FTP_COMPUTING_HT_LHETEROGEN_OUSRETRIEV_VENDORSBE_EDU = (
        "ftp://ftp.computingHT.Lheterogen.ousretriev.vendorsbe.edu"
    )
    FTP_NEWDEVELOPM_NTCOMPLEXA_ONGADVANCE_CONSEQUENT_YALLOW_ORG = (
        "ftp://newdevelopm.ntcomplexa.ongadvance.Consequent.yallow.org"
    )


@dataclass
class NistschemaSvIvAtomicAnyUriEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicAnyUriEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
