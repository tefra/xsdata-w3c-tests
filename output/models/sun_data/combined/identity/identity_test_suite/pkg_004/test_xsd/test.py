from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Scope:
    class Meta:
        name = "scope"
        namespace = "foo"

    key_or_ref: list[Scope.Key | Scope.Ref] = field(
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

    @dataclass(kw_only=True)
    class Key:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Ref:
        value: str = field(
            metadata={
                "required": True,
            }
        )


@dataclass(kw_only=True)
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
