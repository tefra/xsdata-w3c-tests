from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Ext(B):
    class Meta:
        name = "ext"


@dataclass(kw_only=True)
class Doc(Ext):
    class Meta:
        name = "doc"
