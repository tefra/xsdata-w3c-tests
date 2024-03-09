from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    a0: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class R(B):
    a0: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    a2: Any = field(
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
