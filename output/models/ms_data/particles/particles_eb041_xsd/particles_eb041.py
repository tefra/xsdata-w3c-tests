from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    bar: None | Foo.Bar = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
    class Bar:
        foo: None | object = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "foo"
