from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn-klondike-test"


@dataclass(kw_only=True)
class CtypeFoo:
    class Meta:
        name = "ctype_foo"

    a: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RootElem:
    class Meta:
        name = "root_elem"
        namespace = "urn-klondike-test"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
