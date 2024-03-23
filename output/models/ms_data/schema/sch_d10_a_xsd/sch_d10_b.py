from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    class Meta:
        name = "b-ct"

    c21_or_c22: List[Union["BCt.C21", "BCt.C22"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c21",
                    "type": Type["BCt.C21"],
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "c22",
                    "type": Type["BCt.C22"],
                    "namespace": "",
                    "max_occurs": 3,
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass
    class C21:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class C22:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
