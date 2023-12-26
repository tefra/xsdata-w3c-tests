from dataclasses import dataclass, field
from typing import Optional


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
        idref1: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        idref2: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
