from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

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


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguageEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-language-enumeration-1-NS"

    value: NistschemaSvIvAtomicLanguageEnumeration1Type = field()
