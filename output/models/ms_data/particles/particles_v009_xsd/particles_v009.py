from dataclasses import dataclass, field
from typing import Any, List, Optional, Type, Union

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
                    "type": Type["B.E1"],
                    "namespace": "",
                },
                {
                    "name": "e2",
                    "type": Type["B.E2"],
                    "namespace": "",
                },
                {
                    "name": "e3",
                    "type": Type["B.E3"],
                    "namespace": "",
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
    e2_or_e3: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
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
