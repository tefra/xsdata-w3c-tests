from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        nillable = True

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
