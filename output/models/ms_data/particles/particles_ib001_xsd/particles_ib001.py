from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar foo:
    :ivar foo1:
    """
    class Meta:
        name = "base"

    foo: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 6,
        }
    )
    foo1: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 6,
        }
    )


@dataclass
class Doc:
    """
    :ivar foo:
    :ivar foo1:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        }
    )
    foo1: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )
