from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-4-NS"


class NistschemaSvIvAtomicAnyUriEnumeration4Type(Enum):
    GOPHER_THESEDEFINE_ESCRIBESOF_HOSEINDUSTR_EDU = (
        "gopher://thesedefine.escribesof.hoseindustr.edu"
    )
    NEWS_ABLERESULTP_OVIDEDFO_ORG = "news://ableresultp.ovidedfo.org"
    TELNET_CORRECTIONO_FORINFORMA_IONBUILDCA_ABILITIES_COM = (
        "telnet://correctiono.forinforma.ionbuildca.abilities.com"
    )
    FTP_BYSYNTAXINF_RMATIONRET_IEVA_ORG = (
        "ftp://bysyntaxinf.rmationret.ieva.org"
    )
    GOPHER_GROUPSRELA_GOV = "gopher://Groupsrela.gov"
    FTP_FTP_ISSUESQUALI_YENSUREAND_HISTESTSCR_ATIONFORC_COM = (
        "ftp://ftp.issuesquali.yensureand.histestscr.ationforc.com"
    )
    NEWS_XMLAOF_MARKU_ONINOFSTAN_ARDSLACKRE_RIEVE_DE_GOV = (
        "news://XMLAofMarku.oninofstan.ardslackre.rieveDe.gov"
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-4-NS"

    value: NistschemaSvIvAtomicAnyUriEnumeration4Type = field()
