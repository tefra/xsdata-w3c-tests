from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Eden:
    """
    :ivar any_element:
    """
    class Meta:
        name = "eden"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
