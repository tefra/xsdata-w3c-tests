from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class ExternFirstElement:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
