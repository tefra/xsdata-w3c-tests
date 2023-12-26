from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    sub: List["Root.Sub"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Sub:
        idelt: Optional["Root.Sub.Idelt"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

        @dataclass
        class Idelt:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )
            attr: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )
