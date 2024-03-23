from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    r1_or_r2: List[Union["ComplexType.R1", "ComplexType.R2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "r1",
                    "type": Type["ComplexType.R1"],
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "r2",
                    "type": Type["ComplexType.R2"],
                    "namespace": "",
                    "max_occurs": 100,
                },
            ),
            "max_occurs": 100,
        },
    )

    @dataclass
    class R1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class R2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Elem(ComplexType):
    class Meta:
        name = "elem"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
