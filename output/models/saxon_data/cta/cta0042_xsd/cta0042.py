from dataclasses import dataclass, field
from typing import List, Optional, Union


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
    type: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


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

    a: List[Union[Zz, ZzInteger, ZzDouble]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
