from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Stylesheet:
    class Meta:
        name = "stylesheet"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
