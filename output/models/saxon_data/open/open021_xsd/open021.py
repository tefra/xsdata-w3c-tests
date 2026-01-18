from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class R(B):
    pass


@dataclass(kw_only=True)
class Doc(R):
    class Meta:
        name = "doc"
