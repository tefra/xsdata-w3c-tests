from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-4-NS"


class NistschemaSvIvAtomicAnyUriEnumeration4Type(Enum):
    """
    :cvar FTP_BYSYNTAXINF_RMATIONRET_IEVA_ORG:
    :cvar FTP_FTP_ISSUESQUALI_YENSUREAND_HISTESTSCR_ATIONFORC_COM:
    :cvar GOPHER_GROUPSRELA_GOV:
    :cvar GOPHER_THESEDEFINE_ESCRIBESOF_HOSEINDUSTR_EDU:
    :cvar NEWS_XMLAOF_MARKU_ONINOFSTAN_ARDSLACKRE_RIEVE_DE_GOV:
    :cvar NEWS_ABLERESULTP_OVIDEDFO_ORG:
    :cvar TELNET_CORRECTIONO_FORINFORMA_IONBUILDCA_ABILITIES_COM:
    """
    FTP_BYSYNTAXINF_RMATIONRET_IEVA_ORG = "ftp://bysyntaxinf.rmationret.ieva.org"
    FTP_FTP_ISSUESQUALI_YENSUREAND_HISTESTSCR_ATIONFORC_COM = "ftp://ftp.issuesquali.yensureand.histestscr.ationforc.com"
    GOPHER_GROUPSRELA_GOV = "gopher://Groupsrela.gov"
    GOPHER_THESEDEFINE_ESCRIBESOF_HOSEINDUSTR_EDU = "gopher://thesedefine.escribesof.hoseindustr.edu"
    NEWS_XMLAOF_MARKU_ONINOFSTAN_ARDSLACKRE_RIEVE_DE_GOV = "news://XMLAofMarku.oninofstan.ardslackre.rieveDe.gov"
    NEWS_ABLERESULTP_OVIDEDFO_ORG = "news://ableresultp.ovidedfo.org"
    TELNET_CORRECTIONO_FORINFORMA_IONBUILDCA_ABILITIES_COM = "telnet://correctiono.forinforma.ionbuildca.abilities.com"


@dataclass
class NistschemaSvIvAtomicAnyUriEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicAnyUriEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
