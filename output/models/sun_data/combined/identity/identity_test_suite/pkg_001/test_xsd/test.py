from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    key_or_ref: list[Root.Key | Root.Ref] = field(
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

    @dataclass(kw_only=True)
    class Key:
        value: Decimal = field()

    @dataclass(kw_only=True)
    class Ref:
        value: Decimal = field()
