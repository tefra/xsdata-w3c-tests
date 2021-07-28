from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class ACt:
    class Meta:
        name = "A-ct"

    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att5: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att6: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att7: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att9: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att11: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "total_digits": 1,
        }
    )
    att12: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        }
    )
    att13: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        }
    )
    att14: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        }
    )
    att15: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        }
    )
    att16: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class E2:
    class Meta:
        name = "e2"
        namespace = "ns-a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 2,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
