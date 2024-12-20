from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Example:
    even_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "even-number",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
