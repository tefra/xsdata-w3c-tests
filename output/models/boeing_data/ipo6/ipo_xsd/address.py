from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.example.com/add"


@dataclass
class Salutation:
    """
    :ivar value:
    """
    class Meta:
        name = "salutation"
        namespace = "http://www.example.com/add"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
