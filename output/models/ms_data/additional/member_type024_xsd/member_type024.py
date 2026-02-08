from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    value: str = field(default="")
    att1: bool | int | str = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    att2: bool | int | str = field(
        default=5,
        metadata={
            "type": "Attribute",
        },
    )
    att3: bool | int | str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    e: list[Ct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
