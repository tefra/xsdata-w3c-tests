from dataclasses import dataclass, field
from typing import List


@dataclass
class ElementType1:
    """
    :ivar sub_element1:
    """
    class Meta:
        name = "elementType1"

    sub_element1: List["RootType"] = field(
        default_factory=list,
        metadata=dict(
            name="subElement1",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ElementType2:
    """
    :ivar sub_element2:
    """
    class Meta:
        name = "elementType2"

    sub_element2: List["RootType"] = field(
        default_factory=list,
        metadata=dict(
            name="subElement2",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class RootType:
    """
    :ivar ele1:
    :ivar ele2:
    """
    class Meta:
        name = "rootType"

    ele1: List[ElementType1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ele2: List[ElementType2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
