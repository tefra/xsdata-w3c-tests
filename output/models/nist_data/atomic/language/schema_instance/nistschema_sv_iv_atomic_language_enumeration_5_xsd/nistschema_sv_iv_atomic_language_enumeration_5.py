from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-5-NS"


class NistschemaSvIvAtomicLanguageEnumeration5Type(Enum):
    """
    :cvar BH:
    :cvar BI:
    :cvar BN:
    :cvar BO:
    :cvar BR:
    :cvar CA:
    :cvar CO:
    :cvar CS:
    :cvar CY:
    """
    BH = "BH"
    BI = "BI"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    CA = "CA"
    CO = "CO"
    CS = "CS"
    CY = "CY"


@dataclass
class NistschemaSvIvAtomicLanguageEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicLanguageEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
