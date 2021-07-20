from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooAttrTest(Enum):
    FOO = "foo"


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
        value: Optional[str] = field(
            default=None
        )
        attr_test: Optional[FooAttrTest] = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
            }
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
