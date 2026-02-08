from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-4-NS"


class NistschemaSvIvAtomicTokenEnumeration4Type(Enum):
    PICO_CELLULAR = "pico-cellular"
    TO = "to"
    TECHNIQUES = "techniques"
    IS = "is"
    VISIBLY = "visibly"
    AS = "as"
    SYNTAX = "syntax"
    WAS = "was"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTokenEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-4-NS"

    value: NistschemaSvIvAtomicTokenEnumeration4Type = field()
