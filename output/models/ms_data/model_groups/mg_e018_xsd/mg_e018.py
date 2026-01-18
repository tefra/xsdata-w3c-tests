from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    a: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    b: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
