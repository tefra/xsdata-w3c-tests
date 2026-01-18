from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"

    e1: None | object = field(
        default=None,
        metadata={
            "wrapper": "child",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    e1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Doc(Bar):
    class Meta:
        name = "doc"
