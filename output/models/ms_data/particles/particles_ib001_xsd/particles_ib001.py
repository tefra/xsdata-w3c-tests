from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    foo_or_foo1: list[Base.Foo | Base.Foo1] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": ForwardRef("Base.Foo"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 6,
                },
                {
                    "name": "foo1",
                    "type": ForwardRef("Base.Foo1"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 6,
                },
            ),
            "max_occurs": 6,
        },
    )

    @dataclass(kw_only=True)
    class Foo:
        value: bool = field()

    @dataclass(kw_only=True)
    class Foo1:
        value: bool = field()


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
