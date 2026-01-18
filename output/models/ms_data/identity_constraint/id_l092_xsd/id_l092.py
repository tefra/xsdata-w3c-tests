from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class Ttype:
    class Meta:
        name = "ttype"

    row: str = field(
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "required": True,
        }
    )
    col: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Utype:
    class Meta:
        name = "utype"

    row: str = field(
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "required": True,
        }
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class T(Ttype):
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"


@dataclass(kw_only=True)
class U(Utype):
    class Meta:
        name = "u"
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
                },
                {
                    "name": "u",
                    "type": U,
                },
            ),
        },
    )
