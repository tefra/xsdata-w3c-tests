from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"

    e1: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    e1_element: str = field(
        metadata={
            "name": "e1",
            "type": "Element",
            "namespace": "",
        }
    )
    e1: str = field(
        metadata={
            "wrapper": "e2",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
