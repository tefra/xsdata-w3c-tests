from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MyBase:
    class Meta:
        name = "myBase"

    value: str = field(default="")
    a: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class A(MyBase):
    pass
