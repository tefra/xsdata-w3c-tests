from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ComplexType:
    class Meta:
        name = "complexType"

    x: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Elem(ComplexType):
    class Meta:
        name = "elem"

    group_elem: None | object = field(
        default=None,
        metadata={
            "name": "groupElem",
            "type": "Element",
            "namespace": "",
        },
    )
    att2: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att3: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: Elem = field(
        metadata={
            "type": "Element",
        }
    )
