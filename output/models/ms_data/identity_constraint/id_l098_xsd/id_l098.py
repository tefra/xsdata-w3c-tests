from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class Ttype:
    class Meta:
        name = "ttype"

    value: bool = field(
        metadata={
            "required": True,
        }
    )
    row: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )


@dataclass(kw_only=True)
class Utype:
    class Meta:
        name = "utype"

    value: int = field(
        metadata={
            "required": True,
        }
    )
    row: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )


@dataclass(kw_only=True)
class T(Ttype):
    class Meta:
        name = "t"
        nillable = True
        namespace = "myNS.tempuri.org"


@dataclass(kw_only=True)
class U(Utype):
    class Meta:
        name = "u"
        nillable = True
        namespace = "myNS.tempuri.org"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t_or_u: list[T | U] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "t",
                    "type": T,
                    "nillable": True,
                },
                {
                    "name": "u",
                    "type": U,
                    "nillable": True,
                },
            ),
        },
    )
