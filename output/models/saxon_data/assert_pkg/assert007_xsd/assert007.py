from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://chess/ns/"


@dataclass
class T1:
    class Meta:
        name = "t1"

    white: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://chess/ns/",
            "min_occurs": 1,
            "sequence": 1,
        }
    )
    black: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://chess/ns/",
            "sequence": 1,
        }
    )


@dataclass
class T2(T1):
    class Meta:
        name = "t2"


@dataclass
class T3(T2):
    class Meta:
        name = "t3"

    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://chess/ns/",
            "required": True,
        }
    )


@dataclass
class Game(T3):
    class Meta:
        name = "game"
        namespace = "http://chess/ns/"
