from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-4-NS"


class NistschemaSvIvAtomicStringEnumeration4Type(Enum):
    THE = "the"
    EB_XML = "ebXML"
    THE_1 = "The"
    MANY = "many"
    VALUE_2000 = "2000"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicStringEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-4-NS"

    value: NistschemaSvIvAtomicStringEnumeration4Type = field()
