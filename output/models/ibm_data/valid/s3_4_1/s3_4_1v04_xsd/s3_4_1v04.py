from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"

    x: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    y: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    p: C = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
