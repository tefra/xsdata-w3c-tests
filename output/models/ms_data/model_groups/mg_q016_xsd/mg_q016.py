from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"

    e1: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    e1: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    e2: Bar = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
