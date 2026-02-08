from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-1-NS"


class NistschemaSvIvAtomicAnyUriEnumeration1Type(Enum):
    HTTP_THEISTE_COM = "http://Theiste.com"
    MAILTO_PROV_ORG = "mailto:@prov.org"
    FTP_H_COM = "ftp://h.com"
    MAILTO_DEVIC_MANIPULATIONANDABILITYSPECIFICA_GOV = (
        "mailto:devic@manipulationandabilityspecifica.gov"
    )
    HTTP_WWW_SYSTEMSWEBI_TEROPERABI_ITYBEANDOF_HIC_EDU = (
        "http://www.systemswebi.teroperabi.itybeandof.hic.edu"
    )
    GOPHER_CONFORMANCE_UP_COM = "gopher://Conformance.up.com"
    TELNET_F_ORG = "telnet://f.org"
    HTTP_WWW_ASSERIES_GOV = "http://www.asseries.gov"
    TELNET_WIT_EDU = "telnet://wit.edu"
    FTP_FTP_ATHECONSTIT_ENT_OASISRE_RIE_NET = (
        "ftp://ftp.atheconstit.entOASISre.rie.net"
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-1-NS"

    value: NistschemaSvIvAtomicAnyUriEnumeration1Type = field()
