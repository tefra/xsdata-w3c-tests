from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    elem: Root.Elem = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass(kw_only=True)
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
