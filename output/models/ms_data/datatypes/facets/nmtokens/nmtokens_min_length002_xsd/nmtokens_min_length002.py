from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Foo:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        attr_test: list[str] = field(
            default_factory=list,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "min_length": 2,
                "tokens": True,
            },
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
