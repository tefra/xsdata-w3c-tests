from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    local_foo_bar_target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local foo bar ##targetNamespace",
            "max_occurs": 2,
        },
    )


@dataclass
class R(B):
    local_foo_bar_target_namespace_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    local_bar_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local bar",
            "max_occurs": 2,
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
