from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Zz:
    class Meta:
        name = "zz"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )


@dataclass
class A(Zz):
    class Meta:
        name = "a"


@dataclass
class ZzDouble(Zz):
    class Meta:
        name = "zz-double"


@dataclass
class ZzInteger(Zz):
    class Meta:
        name = "zz-integer"


@dataclass
class Zing:
    class Meta:
        name = "zing"

    a: Optional[Union[Zz, ZzInteger, ZzDouble]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
