from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://wild053.org/"


@dataclass(kw_only=True)
class Zang:
    class Meta:
        name = "zang"
        namespace = "http://wild053.org/"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Zeng:
    class Meta:
        name = "zeng"
        namespace = "http://wild053.org/"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    local_target_namespace_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local ##targetNamespace",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class Zong:
    class Meta:
        name = "zong"
        namespace = "http://wild053.org/"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
