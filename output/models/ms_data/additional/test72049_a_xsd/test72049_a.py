from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar a:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
