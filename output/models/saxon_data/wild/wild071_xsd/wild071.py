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
            "required": True,
        },
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
