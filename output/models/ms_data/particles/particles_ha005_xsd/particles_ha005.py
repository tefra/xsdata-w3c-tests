from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e3:
    """
    class Meta:
        name = "base"

    e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class Doc:
    """
    :ivar e3:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
