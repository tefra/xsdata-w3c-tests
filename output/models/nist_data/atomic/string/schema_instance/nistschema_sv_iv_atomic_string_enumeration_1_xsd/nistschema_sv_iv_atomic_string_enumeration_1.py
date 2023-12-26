from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

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


@dataclass
class NistschemaSvIvAtomicStringEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
