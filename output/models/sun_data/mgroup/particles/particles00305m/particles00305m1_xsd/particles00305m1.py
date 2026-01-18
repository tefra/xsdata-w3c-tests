from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "particles"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
