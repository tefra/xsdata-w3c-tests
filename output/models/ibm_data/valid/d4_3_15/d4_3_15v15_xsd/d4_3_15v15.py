from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ElementType1:
    """
    :ivar sub_element1:
    :ivar attr1:
    """
    class Meta:
        name = "elementType1"

    sub_element1: List["RootType"] = field(
        default_factory=list,
        metadata={
            "name": "subElement1",
            "type": "Element",
            "namespace": "",
        }
    )
    attr1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ElementType2:
    """
    :ivar sub_element2:
    :ivar attr2:
    """
    class Meta:
        name = "elementType2"

    sub_element2: List["RootType"] = field(
        default_factory=list,
        metadata={
            "name": "subElement2",
            "type": "Element",
            "namespace": "",
        }
    )
    attr2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    ele2: List[ElementType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
