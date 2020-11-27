from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "importNS"


@dataclass
class Iid:
    class Meta:
        name = "iid"
        namespace = "importNS"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
