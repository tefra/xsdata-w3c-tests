from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar a:
    :ivar other_element:
    :ivar b:
    """
    class Meta:
        name = "doc"

    a: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    b: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
            "sequential": True,
        }
    )


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        name = "e"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
