from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "tck_test"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "tck_test"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )