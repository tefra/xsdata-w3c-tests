from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Tabletype:
    class Meta:
        name = "tabletype"

    r: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class T(Tabletype):
    class Meta:
        name = "t"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
