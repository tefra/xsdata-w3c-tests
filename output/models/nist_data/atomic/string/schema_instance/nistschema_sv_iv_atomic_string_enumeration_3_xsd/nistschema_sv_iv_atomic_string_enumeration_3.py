from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-3-NS"


class NistschemaSvIvAtomicStringEnumeration3Type(Enum):
    SYNTAX = "syntax"
    THROUGH = "through"
    ONLY = "only"
    ANY = "any"
    OUR = "our"
    THAT = "that"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicStringEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-3-NS"

    value: NistschemaSvIvAtomicStringEnumeration3Type = field()
