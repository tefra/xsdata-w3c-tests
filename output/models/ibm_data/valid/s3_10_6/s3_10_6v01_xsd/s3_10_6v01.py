from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    class Meta:
        name = "t"

    e1: Optional["T.E1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    e2: Optional["T.E2"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )

    @dataclass
    class E1:
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass
    class E2:
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
