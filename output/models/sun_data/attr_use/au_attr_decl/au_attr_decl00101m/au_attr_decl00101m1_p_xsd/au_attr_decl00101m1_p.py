from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrUse/attrDecl"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrUse/attrDecl"

    number: int = field(
        metadata={
            "type": "Attribute",
            "namespace": "AttrUse/attrDecl",
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrUse/attrDecl"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
