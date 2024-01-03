from dataclasses import dataclass, field
from typing import Optional, Any

__NAMESPACE__ = "a"


@dataclass
class C:
    class Meta:
        name = "c"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class D(C):
    class Meta:
        name = "d"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    p: Optional[D] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
