from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    e1_or_e2: list[Base.E1 | Base.E2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Base.E1"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 2,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Base.E2"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass(kw_only=True)
    class E1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )

    @dataclass(kw_only=True)
    class E2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )


@dataclass(kw_only=True)
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass(kw_only=True)
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
