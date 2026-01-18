from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-5-NS"


class NistschemaSvIvAtomicLanguageEnumeration5Type(Enum):
    BH = "BH"
    BI = "BI"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    CA = "CA"
    CO = "CO"
    CS = "CS"
    CY = "CY"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguageEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-5-NS"

    value: NistschemaSvIvAtomicLanguageEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
