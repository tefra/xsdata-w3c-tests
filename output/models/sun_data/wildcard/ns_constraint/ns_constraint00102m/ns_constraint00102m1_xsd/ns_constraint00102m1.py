from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "nsConstraint"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
