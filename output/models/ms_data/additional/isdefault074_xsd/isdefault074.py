from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ct:
    class Meta:
        name = "ct"

    a: Optional["Ct.A"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class A:
        att1: str = field(
            default="default",
            metadata={
                "type": "Attribute",
            }
        )
        att2: str = field(
            init=False,
            default="fixed",
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class Root(Ct):
    class Meta:
        name = "root"
