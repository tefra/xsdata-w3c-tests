from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ids:
    class Meta:
        name = "ids"

    id1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    multiple_ids: Optional["Root.MultipleIds"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class MultipleIds(Ids):
        idref_element: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
