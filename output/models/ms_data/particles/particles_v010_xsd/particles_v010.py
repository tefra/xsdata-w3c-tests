from dataclasses import dataclass, field
from typing import Any, ForwardRef, List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    e1_or_e2_or_e3: List[Union["B.E1", "B.E2", "B.E3"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("B.E1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("B.E2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e3",
                    "type": ForwardRef("B.E3"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass
    class E1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E3:
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
    e1_or_e3: Any = field(
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
