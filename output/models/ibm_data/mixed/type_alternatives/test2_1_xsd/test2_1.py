from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Example:
    x: list[Example.KindQuantity | Example.KindPrice | Example.KindMesg] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
    )

    @dataclass(kw_only=True)
    class KindQuantity:
        value: int = field(
            metadata={
                "required": True,
            }
        )
        kind: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KindPrice:
        value: float = field(
            metadata={
                "required": True,
            }
        )
        kind: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KindMesg:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        kind: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
