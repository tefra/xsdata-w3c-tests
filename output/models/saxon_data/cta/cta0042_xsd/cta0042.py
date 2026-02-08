from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Zz:
    class Meta:
        name = "zz"

    value: str = field(default="")
    type_value: None | int = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ZzDouble(Zz):
    class Meta:
        name = "zz-double"


@dataclass(kw_only=True)
class ZzInteger(Zz):
    class Meta:
        name = "zz-integer"


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    a: list[Zz | ZzInteger | ZzDouble] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Root(Zing):
    class Meta:
        name = "root"
