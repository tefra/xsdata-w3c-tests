from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class E1(B):
    class Meta:
        name = "E"


@dataclass(kw_only=True)
class E(E1):
    class Meta:
        name = "e"
