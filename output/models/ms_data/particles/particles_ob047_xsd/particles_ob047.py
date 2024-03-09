from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    foo_bar_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "foo bar",
        },
    )


@dataclass
class R(B):
    foo_bar_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    foo_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "foo",
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
