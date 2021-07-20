from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-1-NS"


class NistschemaSvIvAtomicLanguageEnumeration1Type(Enum):
    AF = "AF"
    AM = "AM"
    AR = "AR"
    AS = "AS"
    AY = "AY"
    AZ = "AZ"
    BA = "BA"
    BE = "BE"


@dataclass
class NistschemaSvIvAtomicLanguageEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicLanguageEnumeration1Type] = field(
        default=None
    )
