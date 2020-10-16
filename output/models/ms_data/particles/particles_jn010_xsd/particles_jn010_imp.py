from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://importedXSD"


@dataclass
class B:
    """
    :ivar any_element:
    :ivar e2:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )


@dataclass
class ExtRefType:
    """
    :ivar imp_e1:
    :ivar imp_e2:
    :ivar imp_a1:
    """
    class Meta:
        name = "extRefType"

    imp_e1: Optional[object] = field(
        default=None,
        metadata={
            "name": "impE1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    imp_e2: Optional[object] = field(
        default=None,
        metadata={
            "name": "impE2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    imp_a1: Optional[str] = field(
        default=None,
        metadata={
            "name": "impA1",
            "type": "Attribute",
        }
    )


@dataclass
class ImpElem1:
    """
    :ivar any_element:
    """
    class Meta:
        name = "impElem1"
        namespace = "http://importedXSD"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class ImpElem2(ExtRefType):
    class Meta:
        name = "impElem2"
        namespace = "http://importedXSD"
