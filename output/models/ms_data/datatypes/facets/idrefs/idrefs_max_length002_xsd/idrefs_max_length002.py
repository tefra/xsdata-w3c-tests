from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    idrefs_attr: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "max_length": 1,
            "tokens": True,
        },
    )
    id1_attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: Foo = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id2_attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
