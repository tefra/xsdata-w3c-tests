from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AD_annotation"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AD_annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
