from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "a"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
