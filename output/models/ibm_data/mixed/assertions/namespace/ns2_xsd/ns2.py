from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.example.org"


@dataclass(kw_only=True)
class Mod2Sequence:
    class Meta:
        name = "MOD2_SEQUENCE"

    y: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class X(Mod2Sequence):
    class Meta:
        name = "x"
        namespace = "http://www.example.org"
