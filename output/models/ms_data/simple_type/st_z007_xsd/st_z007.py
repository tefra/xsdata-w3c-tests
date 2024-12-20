from dataclasses import dataclass, field
from typing import Optional


@dataclass
class T1:
    class Meta:
        name = "t1"

    value: Optional[object] = field(default=None)


@dataclass
class T2(T1):
    class Meta:
        name = "t2"


@dataclass
class Root:
    class Meta:
        name = "root"

    e1: list[T1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    e2: list[T2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
