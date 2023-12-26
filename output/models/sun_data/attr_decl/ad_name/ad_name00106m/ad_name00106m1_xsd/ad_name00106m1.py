from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    number00: Optional[int] = field(
        default=None,
        metadata={
            "name": "number00_",
            "type": "Attribute",
        },
    )
    number01: Optional[int] = field(
        default=None,
        metadata={
            "name": "number01.",
            "type": "Attribute",
        },
    )
    number02: Optional[int] = field(
        default=None,
        metadata={
            "name": "number02-",
            "type": "Attribute",
        },
    )
