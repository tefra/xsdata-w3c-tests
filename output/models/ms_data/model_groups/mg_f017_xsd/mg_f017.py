from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    c1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c3: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c4: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    s1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    s2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    s3: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    s4: None | object = field(
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
