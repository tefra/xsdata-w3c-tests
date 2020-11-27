from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ids:
    class Meta:
        name = "ids"

    id1: str = field(
        default="zxc",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    a: Optional[Ids] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
