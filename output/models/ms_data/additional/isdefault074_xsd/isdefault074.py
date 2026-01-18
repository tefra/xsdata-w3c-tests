from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    a: Ct.A = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class A:
        att1: object = field(
            default="default",
            metadata={
                "type": "Attribute",
            },
        )
        att2: str = field(
            init=False,
            default="fixed",
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Root(Ct):
    class Meta:
        name = "root"
