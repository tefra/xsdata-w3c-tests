from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-2-NS"


class NistschemaSvIvAtomicTokenEnumeration2Type(Enum):
    """
    :cvar MAINTAINED:
    :cvar DEVELOP:
    :cvar NETWORKS:
    :cvar FILE:
    :cvar THE:
    """
    MAINTAINED = "maintained"
    DEVELOP = "Develop"
    NETWORKS = "networks"
    FILE = "file"
    THE = "the"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
