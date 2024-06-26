from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class ExtRefType:
    class Meta:
        name = "extRefType"

    imp_e1: Optional[object] = field(
        default=None,
        metadata={
            "name": "impE1",
            "type": "Element",
            "namespace": "",
        },
    )
    imp_e2: Optional[object] = field(
        default=None,
        metadata={
            "name": "impE2",
            "type": "Element",
            "namespace": "",
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
        namespace = "http://xsdtesting"

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
        namespace = "http://xsdtesting"
