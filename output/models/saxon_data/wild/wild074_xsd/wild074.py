from dataclasses import dataclass, field
from typing import Optional


@dataclass
class A1:
    class Meta:
        name = "A"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class A2:
    class Meta:
        name = "a"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
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
        }
    )
    a_or_a: Optional[object] = field(
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
                    "type": str,
                },
            ),
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
