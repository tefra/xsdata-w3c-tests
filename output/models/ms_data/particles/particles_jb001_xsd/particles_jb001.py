from dataclasses import dataclass, field
from typing import Any, List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class R(B):
    any_element: Any = field(
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
            "required": True,
        },
    )
