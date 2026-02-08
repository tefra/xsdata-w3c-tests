from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-2-NS"


class NistschemaSvIvAtomicAnyUriEnumeration2Type(Enum):
    FTP_FTP_RELATEDTOOL_AANDOFINVE_TICALOFEFF_RTHAVE_EC_EDU = (
        "ftp://ftp.relatedtool.aandofinve.ticalofeff.rthaveEC.edu"
    )
    NEWS_TH_GOV = "news://th.gov"
    HTTP_WWW_WITHOUTTHE_R_COMMENDATI_NSMEASUREME_GOV = (
        "http://www.withouttheR.commendati.nsmeasureme.gov"
    )
    MAILTO_METHODS_ITTECH_LIBRARIESWITHBET_NET = (
        "mailto:methodsIttech@librarieswithbet.net"
    )
    FTP_FOR_INVESTIG_ORG = "ftp://forInvestig.org"
    HTTP_WWW_SIGNATURESR_ACHT_ORG = "http://www.signaturesr.acht.org"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-2-NS"

    value: NistschemaSvIvAtomicAnyUriEnumeration2Type = field()
