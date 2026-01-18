from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-1-NS"


class NistschemaSvIvAtomicStringEnumeration1Type(Enum):
    EC = "EC"
    OBVIOUS = "obvious"
    TO = "to"
    DESIGN = "design"
    ENTERPRISES = "enterprises"
    ASSOCIATED = "associated"
    AND_OR = "and/or"
    STANDARDS = "standards"
    DEVELOPMENT = "development"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicStringEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-1-NS"

    value: NistschemaSvIvAtomicStringEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
