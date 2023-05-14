from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class R:
    class Meta:
        name = "r"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class R2:
    class Meta:
        name = "r2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Rtype:
    class Meta:
        name = "rtype"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class T:
    class Meta:
        name = "t"

    r2_or_r: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "r2",
                    "type": str,
                },
                {
                    "name": "r",
                    "type": str,
                },
            ),
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
