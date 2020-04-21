from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-4-NS"


class NistschemaSvIvAtomicStringEnumeration4Type(Enum):
    """
    :cvar IJ_IW_MDAI:
    :cvar IL_RO_ZSI:
    :cvar IM_VI_WE1_MIG:
    :cvar IM1HBNKI:
    :cvar IN_RO_ZSI:
    """
    IJ_IW_MDAI = "2000"
    IL_RO_ZSI = "The"
    IM_VI_WE1_MIG = "ebXML"
    IM1HBNKI = "many"
    IN_RO_ZSI = "the"


@dataclass
class NistschemaSvIvAtomicStringEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
