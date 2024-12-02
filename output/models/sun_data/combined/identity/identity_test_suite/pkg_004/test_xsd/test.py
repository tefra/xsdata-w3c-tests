from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "foo"


@dataclass
class Scope:
    class Meta:
        name = "scope"
        namespace = "foo"

    key_or_ref: list[Union["Scope.Key", "Scope.Ref"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": ForwardRef("Scope.Key"),
                },
                {
                    "name": "ref",
                    "type": ForwardRef("Scope.Ref"),
                },
            ),
        },
    )

    @dataclass
    class Key:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Ref:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    scope: list[Scope] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
