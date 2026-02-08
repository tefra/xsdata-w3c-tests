from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-4-NS"


class NistschemaSvIvAtomicLanguageEnumeration4Type(Enum):
    BR = "BR"
    CA = "CA"
    CO = "CO"
    CS = "CS"
    CY = "CY"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguageEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-4-NS"

    value: NistschemaSvIvAtomicLanguageEnumeration4Type = field()
