from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-enumeration-5-NS"


class NistschemaSvIvAtomicAnyUriEnumeration5Type(Enum):
    """
    :cvar FTP_FTP_AREANDA_COMM_TTEETRANSA_TTHEMBUSIN_SSISFILT_EDU:
    :cvar GOPHER_PROGRAMACCE_SBYNEWTHE_I_TERNETINFO_MATIONINTE_ORG:
    :cvar HTTP_WORLDONENAB_INGTHROUGH_UTCANPRINT_EFI_NET:
    :cvar MAILTO_COMPUTINGEXECUTIONTOAC_INDUSTRYPROVIDESANDINAND_PER_GOV:
    :cvar MAILTO_MATCHCREAT_ELECTRONICBEENYEARSDOCUMENTS_INVE_GOV:
    :cvar MAILTO_OFDISCOVERYST_GROUPS_ATOOFOFWHICHISCREA_GOV:
    """
    FTP_FTP_AREANDA_COMM_TTEETRANSA_TTHEMBUSIN_SSISFILT_EDU = "ftp://ftp.areandaComm.tteetransa.tthembusin.ssisfilt.edu"
    GOPHER_PROGRAMACCE_SBYNEWTHE_I_TERNETINFO_MATIONINTE_ORG = "gopher://programacce.sbynewtheI.ternetinfo.mationinte.org"
    HTTP_WORLDONENAB_INGTHROUGH_UTCANPRINT_EFI_NET = "http://worldonenab.ingthrough.utcanprint.efi.net"
    MAILTO_COMPUTINGEXECUTIONTOAC_INDUSTRYPROVIDESANDINAND_PER_GOV = "mailto:computingexecutiontoac@industryprovidesandinandPer.gov"
    MAILTO_MATCHCREAT_ELECTRONICBEENYEARSDOCUMENTS_INVE_GOV = "mailto:matchcreat@electronicbeenyearsdocumentsInve.gov"
    MAILTO_OFDISCOVERYST_GROUPS_ATOOFOFWHICHISCREA_GOV = "mailto:ofdiscoveryst@GroupsAtoofofwhichiscrea.gov"


@dataclass
class NistschemaSvIvAtomicAnyUriEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicAnyUriEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
