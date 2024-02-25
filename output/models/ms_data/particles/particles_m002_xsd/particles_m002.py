from dataclasses import dataclass, field
from typing import List, Optional, Type, Union, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    choice: List[Union["B.C1", "B.C2", "B.D1", "B.D2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": Type["B.C1"],
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": Type["B.C2"],
                    "namespace": "",
                },
                {
                    "name": "d1",
                    "type": Type["B.D1"],
                    "namespace": "",
                },
                {
                    "name": "d2",
                    "type": Type["B.D2"],
                    "namespace": "",
                },
            ),
            "max_occurs": 9,
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
    c2_or_d1_or_d2: Any = field(
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
