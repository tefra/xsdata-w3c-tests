from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
