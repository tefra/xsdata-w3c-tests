from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    idrefs_attr: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "length": 2,
            "tokens": True,
        },
    )
    id1_attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[Foo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id2_attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
