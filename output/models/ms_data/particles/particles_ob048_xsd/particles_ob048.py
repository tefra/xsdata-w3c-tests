from dataclasses import dataclass, field
from typing import Optional

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
