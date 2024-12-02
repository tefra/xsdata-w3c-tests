from dataclasses import dataclass, field
from typing import Any, ForwardRef, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    c1_or_c2: list[Union["B.C1", "B.C2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("B.C1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "c2",
                    "type": ForwardRef("B.C2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    d1_or_d2: list[Union["B.D1", "B.D2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d1",
                    "type": ForwardRef("B.D1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "d2",
                    "type": ForwardRef("B.D2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass
    class C1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class C2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class D1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class D2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class R(B):
    c2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    d2: Any = field(
        init=False,
        default=None,
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
