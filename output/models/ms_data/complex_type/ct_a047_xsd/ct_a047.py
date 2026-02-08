from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "_foo"

    value: str = field(default="")
    attr_test: None | object = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(Foo):
    class Meta:
        name = "root"
