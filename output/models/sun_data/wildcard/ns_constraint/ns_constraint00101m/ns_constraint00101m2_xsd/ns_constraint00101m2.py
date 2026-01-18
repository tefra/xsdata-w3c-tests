from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "nsConstraint"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
