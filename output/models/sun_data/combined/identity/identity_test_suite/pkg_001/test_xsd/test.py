from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    key_or_ref: list[Union["Root.Key", "Root.Ref"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": ForwardRef("Root.Key"),
                },
                {
                    "name": "ref",
                    "type": ForwardRef("Root.Ref"),
                },
            ),
        },
    )

    @dataclass
    class Key:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Ref:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
