from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-2-NS"


class NistschemaSvIvAtomicAnyUriEnumeration2Type(Enum):
    """
    :cvar FTP_FOR_INVESTIG_ORG:
    :cvar FTP_FTP_RELATEDTOOL_AANDOFINVE_TICALOFEFF_RTHAVE_EC_EDU:
    :cvar HTTP_WWW_SIGNATURESR_ACHT_ORG:
    :cvar HTTP_WWW_WITHOUTTHE_R_COMMENDATI_NSMEASUREME_GOV:
    :cvar MAILTO_METHODS_ITTECH_LIBRARIESWITHBET_NET:
    :cvar NEWS_TH_GOV:
    """
    FTP_FOR_INVESTIG_ORG = "ftp://forInvestig.org"
    FTP_FTP_RELATEDTOOL_AANDOFINVE_TICALOFEFF_RTHAVE_EC_EDU = "ftp://ftp.relatedtool.aandofinve.ticalofeff.rthaveEC.edu"
    HTTP_WWW_SIGNATURESR_ACHT_ORG = "http://www.signaturesr.acht.org"
    HTTP_WWW_WITHOUTTHE_R_COMMENDATI_NSMEASUREME_GOV = "http://www.withouttheR.commendati.nsmeasureme.gov"
    MAILTO_METHODS_ITTECH_LIBRARIESWITHBET_NET = "mailto:methodsIttech@librarieswithbet.net"
    NEWS_TH_GOV = "news://th.gov"


@dataclass
class NistschemaSvIvAtomicAnyUriEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicAnyUriEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )