from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "base"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )


@dataclass
class Testing:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "testing"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
