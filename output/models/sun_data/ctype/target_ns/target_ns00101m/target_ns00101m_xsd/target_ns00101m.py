from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "targetNS"


@dataclass
class Test:
    abc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
