from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    """
    :ivar content:
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "b"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    c: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Ext(B):
    """
    :ivar content:
    :ivar d:
    :ivar e:
    """
    class Meta:
        name = "ext"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    e: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        }
    )


@dataclass
class Doc(Ext):
    class Meta:
        name = "doc"
