from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-1-NS"


class NistschemaSvIvAtomicStringEnumeration1Type(Enum):
    """
    :cvar AND_OR:
    :cvar ASSOCIATED:
    :cvar DESIGN:
    :cvar DEVELOPMENT:
    :cvar EC:
    :cvar ENTERPRISES:
    :cvar OBVIOUS:
    :cvar STANDARDS:
    :cvar TO:
    """
    AND_OR = "and/or"
    ASSOCIATED = "associated"
    DESIGN = "design"
    DEVELOPMENT = "development"
    EC = "EC"
    ENTERPRISES = "enterprises"
    OBVIOUS = "obvious"
    STANDARDS = "standards"
    TO = "to"


@dataclass
class NistschemaSvIvAtomicStringEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
