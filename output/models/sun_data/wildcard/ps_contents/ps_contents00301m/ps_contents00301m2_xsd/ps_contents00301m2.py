from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "psContents"


@dataclass
class A:
    """
    :ivar any_element:
    """
    class Meta:
        name = "a"
        namespace = "psContents"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
