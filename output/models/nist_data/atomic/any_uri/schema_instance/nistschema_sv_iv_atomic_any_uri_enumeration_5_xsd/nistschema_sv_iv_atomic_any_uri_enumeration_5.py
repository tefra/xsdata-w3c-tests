from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-5-NS"


class NistschemaSvIvAtomicAnyUriEnumeration5Type(Enum):
    MAILTO_OFDISCOVERYST_GROUPS_ATOOFOFWHICHISCREA_GOV = (
        "mailto:ofdiscoveryst@GroupsAtoofofwhichiscrea.gov"
    )
    GOPHER_PROGRAMACCE_SBYNEWTHE_I_TERNETINFO_MATIONINTE_ORG = (
        "gopher://programacce.sbynewtheI.ternetinfo.mationinte.org"
    )
    MAILTO_COMPUTINGEXECUTIONTOAC_INDUSTRYPROVIDESANDINAND_PER_GOV = (
        "mailto:computingexecutiontoac@industryprovidesandinandPer.gov"
    )
    MAILTO_MATCHCREAT_ELECTRONICBEENYEARSDOCUMENTS_INVE_GOV = (
        "mailto:matchcreat@electronicbeenyearsdocumentsInve.gov"
    )
    FTP_FTP_AREANDA_COMM_TTEETRANSA_TTHEMBUSIN_SSISFILT_EDU = (
        "ftp://ftp.areandaComm.tteetransa.tthembusin.ssisfilt.edu"
    )
    HTTP_WORLDONENAB_INGTHROUGH_UTCANPRINT_EFI_NET = (
        "http://worldonenab.ingthrough.utcanprint.efi.net"
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-5-NS"

    value: NistschemaSvIvAtomicAnyUriEnumeration5Type = field()
