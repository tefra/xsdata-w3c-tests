from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class A1:
    class Meta:
        name = "A"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class A2:
    class Meta:
        name = "a"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
    a_or_a: Optional[Union[A1, A2]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "A",
                    "type": A1,
                },
                {
                    "name": "a",
                    "type": A2,
                },
            ),
        },
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
