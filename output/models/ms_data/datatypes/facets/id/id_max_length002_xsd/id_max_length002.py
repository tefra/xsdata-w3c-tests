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
        }
    )

    @dataclass
    class Foo:
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
        )
        attr_test: Optional[str] = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "max_length": 5,
            }
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
