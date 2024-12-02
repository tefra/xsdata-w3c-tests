from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Rtype:
    class Meta:
        name = "rtype"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class R(Rtype):
    class Meta:
        name = "r"


@dataclass
class R2(Rtype):
    class Meta:
        name = "r2"


@dataclass
class T:
    class Meta:
        name = "t"

    r2_or_r: Optional[Union[R2, R]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "r2",
                    "type": R2,
                },
                {
                    "name": "r",
                    "type": R,
                },
            ),
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
