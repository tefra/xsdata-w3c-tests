from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    """
    :ivar ele:
    :ivar value:
    :ivar value_1:
    :ivar value_9:
    :ivar value_2:
    :ivar a_a:
    :ivar a_a_a:
    :ivar a_ele:
    """
    ele: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_ele",
            "type": "Element",
            "namespace": "a",
        }
    )
    value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_-",
            "type": "Element",
            "namespace": "a",
        }
    )
    value_1: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_.",
            "type": "Element",
            "namespace": "a",
        }
    )
    value_9: List[str] = field(
        default_factory=list,
        metadata={
            "name": "_9",
            "type": "Element",
            "namespace": "a",
        }
    )
    value_2: List[str] = field(
        default_factory=list,
        metadata={
            "name": "___",
            "type": "Element",
            "namespace": "a",
        }
    )
    a_a: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    a_a_a: List[str] = field(
        default_factory=list,
        metadata={
            "name": "a.a",
            "type": "Element",
            "namespace": "a",
        }
    )
    a_ele: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ele",
            "type": "Element",
            "namespace": "a",
        }
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
