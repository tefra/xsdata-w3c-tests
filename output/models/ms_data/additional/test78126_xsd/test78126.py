from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    """
    :ivar value:
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "a"

    value: Optional[str] = field(
        default=None,
    )
    att1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Any:
    """
    :ivar any_element:
    """
    class Meta:
        name = "any"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Root:
    """
    :ivar any:
    :ivar a:
    """
    class Meta:
        name = "root"

    any: List[Any] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    a: List[A] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
