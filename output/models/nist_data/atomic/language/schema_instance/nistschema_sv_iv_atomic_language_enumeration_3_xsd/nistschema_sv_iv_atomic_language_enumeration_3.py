from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

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


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguageEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-3-NS"

    value: NistschemaSvIvAtomicLanguageEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
