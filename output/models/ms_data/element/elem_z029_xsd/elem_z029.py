from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"
        nillable = True

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            nillable=True
        )
    )