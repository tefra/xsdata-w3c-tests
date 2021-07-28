from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "bar"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "bar"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "bar"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "bar"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
