from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-2-NS"


class NistschemaSvIvAtomicLanguageEnumeration2Type(Enum):
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SQ = "SQ"
    SR = "SR"
    SS = "SS"


@dataclass
class NistschemaSvIvAtomicLanguageEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicLanguageEnumeration2Type] = field(
        default=None
    )
