from dataclasses import dataclass, field
from typing import Optional, Union

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
    att: Optional[Union[bool, int, str]] = field(
        default=None,
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
