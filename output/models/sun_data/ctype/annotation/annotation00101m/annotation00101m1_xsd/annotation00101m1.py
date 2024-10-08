from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "annotation"


@dataclass
class Test:
    """
    This is a complex type definition.
    """


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
