from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-enumeration-2-NS"


class NistschemaSvIvAtomicLanguageEnumeration2Type(Enum):
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SQ = "SQ"
    SR = "SR"
    SS = "SS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguageEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-2-NS"

    value: NistschemaSvIvAtomicLanguageEnumeration2Type = field()
