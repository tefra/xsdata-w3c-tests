from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "Schema/annotations"


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "Schema/annotations"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
