from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    class Meta:
        name = "ttype"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        }
    )


@dataclass
class Utype:
    class Meta:
        name = "utype"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        }
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

    t_or_u: List[Union[U, T]] = field(
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
        }
    )
