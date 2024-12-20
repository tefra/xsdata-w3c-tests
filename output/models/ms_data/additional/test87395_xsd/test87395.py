from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "foo"


class St(Enum):
    A = "a"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "foo"

    value: Optional[St] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "foo"

    a: Optional[A] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
