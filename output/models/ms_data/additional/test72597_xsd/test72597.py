from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class A:
    part: list[A.Part] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Part:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        number: None | int = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        number2: None | int = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    a: A = field(
        metadata={
            "name": "A",
            "type": "Element",
            "required": True,
        }
    )
