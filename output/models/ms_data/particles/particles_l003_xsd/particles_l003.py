from dataclasses import dataclass, field
from typing import List, Optional, Type, Union, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    c1_or_c2: List[Union["B.C1", "B.C2"]] = field(
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
            ),
            "max_occurs": 2,
        },
    )
    d1_or_d2: List[Union["B.D1", "B.D2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
        metadata={
            "type": "Ignore",
        },
    )
    d2: Any = field(
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
