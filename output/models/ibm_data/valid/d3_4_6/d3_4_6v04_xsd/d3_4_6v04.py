from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Nametest:
    ele: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
            "pattern": r"\i\c",
        },
    )


@dataclass(kw_only=True)
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
