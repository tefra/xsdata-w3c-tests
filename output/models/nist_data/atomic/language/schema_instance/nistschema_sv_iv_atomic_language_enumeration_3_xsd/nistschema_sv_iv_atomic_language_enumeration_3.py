from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-3-NS"


class NistschemaSvIvAtomicLanguageEnumeration3Type(Enum):
    AY = "AY"
    AZ = "AZ"
    BA = "BA"
    BE = "BE"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BN = "BN"
    BO = "BO"


@dataclass
class NistschemaSvIvAtomicLanguageEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicLanguageEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
