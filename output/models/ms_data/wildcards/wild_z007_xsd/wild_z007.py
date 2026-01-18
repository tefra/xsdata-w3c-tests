from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass(kw_only=True)
class Stylesheet:
    class Meta:
        name = "stylesheet"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
