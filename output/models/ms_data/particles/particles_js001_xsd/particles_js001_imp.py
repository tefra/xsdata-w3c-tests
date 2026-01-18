from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class ExtRefType:
    class Meta:
        name = "extRefType"

    imp_e1: None | object = field(
        default=None,
        metadata={
            "name": "impE1",
            "type": "Element",
            "namespace": "",
        },
    )
    imp_e2: None | object = field(
        default=None,
        metadata={
            "name": "impE2",
            "type": "Element",
            "namespace": "",
        },
    )
    imp_a1: None | object = field(
        default=None,
        metadata={
            "name": "impA1",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ImpElem1:
    class Meta:
        name = "impElem1"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ImpElem2(ExtRefType):
    class Meta:
        name = "impElem2"
        namespace = "http://xsdtesting"
