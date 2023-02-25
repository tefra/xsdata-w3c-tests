from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "IdConstrDefs/name"


@dataclass
class Name:
    class Meta:
        name = "name"
        namespace = "IdConstrDefs/name"

    name: List["Name.NameInner"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class NameInner:
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
        )
        name: Optional[object] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
