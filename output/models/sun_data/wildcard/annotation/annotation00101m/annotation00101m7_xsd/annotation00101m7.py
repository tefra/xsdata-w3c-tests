from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "Wildcard/annotation"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "Wildcard/annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TheType:
    class Meta:
        name = "theType"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
