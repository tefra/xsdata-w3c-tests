from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.com/over019"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://example.com/over019"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
