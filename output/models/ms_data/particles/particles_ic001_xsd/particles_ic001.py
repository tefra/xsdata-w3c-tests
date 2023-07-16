from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    e2: Optional[object] = field(
        default=None,
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
