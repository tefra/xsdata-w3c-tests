from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    ele1: list["ElementType1"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ele2: list["ElementType2"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ElementType1:
    class Meta:
        name = "elementType1"

    sub_element1: list[RootType] = field(
        default_factory=list,
        metadata={
            "name": "subElement1",
            "type": "Element",
            "namespace": "",
        },
    )
    attr1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ElementType2:
    class Meta:
        name = "elementType2"

    sub_element2: list[RootType] = field(
        default_factory=list,
        metadata={
            "name": "subElement2",
            "type": "Element",
            "namespace": "",
        },
    )
    attr2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
