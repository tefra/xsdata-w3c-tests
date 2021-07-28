from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "Wildcard/annotation"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "Wildcard/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class TheType:
    class Meta:
        name = "theType"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
