from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    """
    :ivar a_element:
    """
    class Meta:
        name = "t"

    a_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "a",
            "required": True,
        }
    )


@dataclass
class X:
    """
    :ivar value:
    """
    class Meta:
        name = "x"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
