from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "Notation/annotation"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "Notation/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
