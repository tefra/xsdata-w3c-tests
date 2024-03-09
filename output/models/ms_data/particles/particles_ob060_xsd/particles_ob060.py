from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    local_foo_bar_target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local foo bar ##targetNamespace",
        },
    )


@dataclass
class R(B):
    local_foo_bar_target_namespace_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    bar_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "bar",
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
