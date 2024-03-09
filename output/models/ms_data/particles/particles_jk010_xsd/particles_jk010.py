from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class R(B):
    other_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
