from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Idrefs:
    class Meta:
        name = "idrefs"

    idref_subelement: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    idref1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    idref2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Ids:
    class Meta:
        name = "ids"

    idref_element: list[Idrefs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    id1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root(Ids):
    class Meta:
        name = "root"
