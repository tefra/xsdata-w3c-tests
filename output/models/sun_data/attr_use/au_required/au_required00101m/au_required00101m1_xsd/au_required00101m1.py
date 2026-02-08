from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrUse/required"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrUse/required"

    number: int = field(
        metadata={
            "type": "Attribute",
            "namespace": "AttrUse/required",
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrUse/required"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
