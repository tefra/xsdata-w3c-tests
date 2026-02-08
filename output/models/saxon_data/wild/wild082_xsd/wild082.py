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
class A(Zz):
    class Meta:
        name = "a"


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

    a: Zz | ZzInteger | ZzDouble = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Root(Zing):
    class Meta:
        name = "root"
