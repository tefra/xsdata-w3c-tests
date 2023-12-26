from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooAttrTest(Enum):
    FOO = "foo"
    FOO123 = "foo123"
    FU1 = "fu1"


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
        attr_test: Optional[FooAttrTest] = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
            },
        )
        id_attr: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
