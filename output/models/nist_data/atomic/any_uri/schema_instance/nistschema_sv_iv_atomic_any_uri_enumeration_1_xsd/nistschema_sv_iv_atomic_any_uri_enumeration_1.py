from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-1-NS"


class NistschemaSvIvAtomicAnyUriEnumeration1Type(Enum):
    """
    :cvar FTP_FTP_ATHECONSTIT_ENT_OASISRE_RIE_NET:
    :cvar FTP_H_COM:
    :cvar GOPHER_CONFORMANCE_UP_COM:
    :cvar HTTP_THEISTE_COM:
    :cvar HTTP_WWW_ASSERIES_GOV:
    :cvar HTTP_WWW_SYSTEMSWEBI_TEROPERABI_ITYBEANDOF_HIC_EDU:
    :cvar MAILTO_PROV_ORG:
    :cvar MAILTO_DEVIC_MANIPULATIONANDABILITYSPECIFICA_GOV:
    :cvar TELNET_F_ORG:
    :cvar TELNET_WIT_EDU:
    """
    FTP_FTP_ATHECONSTIT_ENT_OASISRE_RIE_NET = "ftp://ftp.atheconstit.entOASISre.rie.net"
    FTP_H_COM = "ftp://h.com"
    GOPHER_CONFORMANCE_UP_COM = "gopher://Conformance.up.com"
    HTTP_THEISTE_COM = "http://Theiste.com"
    HTTP_WWW_ASSERIES_GOV = "http://www.asseries.gov"
    HTTP_WWW_SYSTEMSWEBI_TEROPERABI_ITYBEANDOF_HIC_EDU = "http://www.systemswebi.teroperabi.itybeandof.hic.edu"
    MAILTO_PROV_ORG = "mailto:@prov.org"
    MAILTO_DEVIC_MANIPULATIONANDABILITYSPECIFICA_GOV = "mailto:devic@manipulationandabilityspecifica.gov"
    TELNET_F_ORG = "telnet://f.org"
    TELNET_WIT_EDU = "telnet://wit.edu"


@dataclass
class NistschemaSvIvAtomicAnyUriEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicAnyUriEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
