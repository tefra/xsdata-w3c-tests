from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Xmlns:
    class Meta:
        name = "xmlns"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    attr_test: None | str = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(Xmlns):
    class Meta:
        name = "root"
