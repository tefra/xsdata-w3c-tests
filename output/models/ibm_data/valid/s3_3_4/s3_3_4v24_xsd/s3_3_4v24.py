from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Idrefs:
    """
    :ivar idref_subelement:
    :ivar idref1:
    :ivar idref2:
    """
    class Meta:
        name = "idrefs"

    idref_subelement: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    idref1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    idref2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Ids:
    """
    :ivar idref_element:
    :ivar id1:
    :ivar id2:
    """
    class Meta:
        name = "ids"

    idref_element: List[Idrefs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    id1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root(Ids):
    class Meta:
        name = "root"
