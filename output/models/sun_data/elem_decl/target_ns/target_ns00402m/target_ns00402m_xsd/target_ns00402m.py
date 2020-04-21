from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GlobalType:
    """
    :ivar any_element:
    """
    class Meta:
        name = "Global"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
