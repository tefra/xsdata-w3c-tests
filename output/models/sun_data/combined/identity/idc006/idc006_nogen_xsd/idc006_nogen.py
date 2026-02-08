from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.publishing.org"


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        namespace = "http://www.publishing.org"

    b: None | B = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.publishing.org"

    keys: Root.Keys = field(
        metadata={
            "type": "Element",
        }
    )
    keyref: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class Keys:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )
