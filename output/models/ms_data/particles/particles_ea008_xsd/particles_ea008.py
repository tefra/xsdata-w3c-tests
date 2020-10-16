from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
