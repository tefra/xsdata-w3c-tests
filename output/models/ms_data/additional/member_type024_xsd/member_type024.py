from dataclasses import dataclass, field
from typing import Union

__NAMESPACE__ = "foo"


@dataclass
class Ct:
    class Meta:
        name = "ct"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    att1: Union[bool, int, str] = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    att2: Union[bool, int, str] = field(
        default=5,
        metadata={
            "type": "Attribute",
        },
    )
    att3: Union[bool, int, str] = field(
        default="abc",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
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
