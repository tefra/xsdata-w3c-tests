from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar any_element:
    """
    class Meta:
        name = "doc"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
