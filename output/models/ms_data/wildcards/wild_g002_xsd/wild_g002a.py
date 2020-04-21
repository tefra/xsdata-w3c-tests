from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foo"


@dataclass
class Bar:
    """
    :ivar value:
    """
    class Meta:
        name = "bar"
        namespace = "http://foo"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
