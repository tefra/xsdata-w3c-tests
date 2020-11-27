from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
