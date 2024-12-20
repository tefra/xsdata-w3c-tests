from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://importedXSD"


@dataclass
class B:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    e2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://importedXSD",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )


@dataclass
class ExtRefType:
    class Meta:
        name = "extRefType"

    imp_e1: Optional[object] = field(
        default=None,
        metadata={
            "name": "impE1",
            "type": "Element",
            "namespace": "http://importedXSD",
        },
    )
    imp_e2: Optional[object] = field(
        default=None,
        metadata={
            "name": "impE2",
            "type": "Element",
            "namespace": "http://importedXSD",
        },
    )
    imp_a1: Optional[object] = field(
        default=None,
        metadata={
            "name": "impA1",
            "type": "Attribute",
        },
    )


@dataclass
class ImpElem1:
    class Meta:
        name = "impElem1"
        namespace = "http://importedXSD"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ImpElem2(ExtRefType):
    class Meta:
        name = "impElem2"
        namespace = "http://importedXSD"
