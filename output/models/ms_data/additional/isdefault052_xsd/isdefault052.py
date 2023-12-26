from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    elem: Optional["Root.Elem"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Elem:
        attr1: int = field(
            init=False,
            default=123,
            metadata={
                "type": "Attribute",
            },
        )
        attr2: str = field(
            init=False,
            default="abc",
            metadata={
                "type": "Attribute",
            },
        )
        attr3: bool = field(
            init=False,
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
