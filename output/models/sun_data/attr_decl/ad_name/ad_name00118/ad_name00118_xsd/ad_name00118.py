from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "Aƻa",
            "type": "Attribute",
        }
    )
    b_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "bƻB",
            "type": "Attribute",
        }
    )
