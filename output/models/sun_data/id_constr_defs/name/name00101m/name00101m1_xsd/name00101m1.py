from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "IdConstrDefs/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/name"

    person: List["Root.Person"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Person:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        parent: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
