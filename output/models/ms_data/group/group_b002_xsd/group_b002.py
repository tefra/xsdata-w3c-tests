from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Elem(ComplexType):
    class Meta:
        name = "elem"

    group_elem: Optional[object] = field(
        default=None,
        metadata={
            "name": "groupElem",
            "type": "Element",
            "namespace": "",
        },
    )
    att2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
