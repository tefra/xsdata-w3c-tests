from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
