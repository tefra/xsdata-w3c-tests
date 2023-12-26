from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-2-NS"


class NistschemaSvIvAtomicTokenEnumeration2Type(Enum):
    MAINTAINED = "maintained"
    DEVELOP = "Develop"
    NETWORKS = "networks"
    FILE = "file"
    THE = "the"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
