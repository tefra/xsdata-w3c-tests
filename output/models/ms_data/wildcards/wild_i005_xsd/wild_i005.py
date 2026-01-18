from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    foo_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo",
        },
    )
    a_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "a",
        },
    )
    b_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "b",
        },
    )
    target_namespace_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
