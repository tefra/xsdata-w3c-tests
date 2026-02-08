from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://chess/ns/"


@dataclass(kw_only=True)
class T1:
    class Meta:
        name = "t1"

    white: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://chess/ns/",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    black: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://chess/ns/",
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class T2(T1):
    class Meta:
        name = "t2"


@dataclass(kw_only=True)
class T3(T2):
    class Meta:
        name = "t3"

    result: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://chess/ns/",
        }
    )


@dataclass(kw_only=True)
class Game(T3):
    class Meta:
        name = "game"
        namespace = "http://chess/ns/"
