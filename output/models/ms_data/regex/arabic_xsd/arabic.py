from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"\p{IsArabic}+"
        )
    )
