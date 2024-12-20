from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    class Meta:
        name = "ttype"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )


@dataclass
class Utype:
    class Meta:
        name = "utype"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )


@dataclass
class T(Ttype):
    class Meta:
        name = "t"
        nillable = True
        namespace = "myNS.tempuri.org"


@dataclass
class U(Utype):
    class Meta:
        name = "u"
        nillable = True
        namespace = "myNS.tempuri.org"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t_or_u: list[Union[T, U]] = field(
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
