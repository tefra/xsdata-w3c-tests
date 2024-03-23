from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    e1_or_e2: List[Union["B.E1", "B.E2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": Type["B.E1"],
                    "namespace": "",
                    "max_occurs": 9,
                },
                {
                    "name": "e2",
                    "type": Type["B.E2"],
                    "namespace": "",
                    "max_occurs": 9,
                },
            ),
            "min_occurs": 3,
            "max_occurs": 9,
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
class R(B):
    pass


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
