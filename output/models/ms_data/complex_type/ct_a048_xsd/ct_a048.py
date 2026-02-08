from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Type1:
    class Meta:
        name = "_1"

    value: str = field(default="")
    attr_test: None | object = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(Type1):
    class Meta:
        name = "root"
