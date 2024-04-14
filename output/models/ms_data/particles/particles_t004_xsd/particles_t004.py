from dataclasses import dataclass, field
from typing import Any, ForwardRef, List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    c1_or_c2_or_c3: List[Union["B.C1", "B.C2", "B.C3"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("B.C1"),
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": ForwardRef("B.C2"),
                    "namespace": "",
                    "max_occurs": 5,
                },
                {
                    "name": "c3",
                    "type": ForwardRef("B.C3"),
                    "namespace": "",
                },
            ),
            "max_occurs": 5,
        },
    )
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
    class C3:
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
    c3: Any = field(
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
