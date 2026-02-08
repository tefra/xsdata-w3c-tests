from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    a: object = field(
        default="default",
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    b: str = field(
        init=False,
        default="fixed",
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Root(Ct):
    class Meta:
        name = "root"
