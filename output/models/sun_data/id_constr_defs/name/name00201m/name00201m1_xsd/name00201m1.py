from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "IdConstrDefs/name"


@dataclass
class Name:
    class Meta:
        name = "name"
        namespace = "IdConstrDefs/name"

    name: List["Name.Name"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Name:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
