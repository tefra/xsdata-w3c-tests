from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/1999/xhtml"


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/1999/xhtml"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )