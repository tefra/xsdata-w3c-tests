from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e1:
    :ivar e2:
    :ivar e3:
    """
    class Meta:
        name = "base"

    e1: Optional[object] = field(
        default=None,
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
            "max_occurs": 2,
        }
    )
    e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 2,
        }
    )


@dataclass
class Doc:
    """
    :ivar e1:
    :ivar e2:
    :ivar e3:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        }
    )
    e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        }
    )
