from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    elem: Root.Elem = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Elem:
        attr1: int = field(
            init=False,
            default=123,
            metadata={
                "type": "Attribute",
                "namespace": "foo",
            },
        )
        attr2: str = field(
            init=False,
            default="abc",
            metadata={
                "type": "Attribute",
                "namespace": "foo",
            },
        )
        attr3: bool = field(
            init=False,
            default=True,
            metadata={
                "type": "Attribute",
                "namespace": "foo",
            },
        )
