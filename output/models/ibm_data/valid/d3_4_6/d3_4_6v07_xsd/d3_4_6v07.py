from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    ele: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_ele",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )
    value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_-",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )
    value_1: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_.",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )
    value_9: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_9",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )
    value_2: List[str] = field(
        default_factory=list,
        metadata={
            "name": "___",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )
    a_a: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )
    a_a_a: List[str] = field(
        default_factory=list,
        metadata={
            "name": "a.a",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )
    a_ele: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ele",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        }
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
