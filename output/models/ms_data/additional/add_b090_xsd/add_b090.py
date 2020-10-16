from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Base:
    """
    :ivar foo_element:
    """
    class Meta:
        name = "base"

    foo_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo",
            "max_occurs": 3,
        }
    )


@dataclass
class Foo:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Doc(Base):
    """
    :ivar c1:
    :ivar c2:
    """
    class Meta:
        name = "doc"

    c1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    c2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
