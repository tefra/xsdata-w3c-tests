from dataclasses import dataclass, field
from enum import Enum
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
        value: Optional[str] = field(
            default=None,
        )
        attr_test: Optional["FooType.Foo.AttrTest"] = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
            }
        )

        class AttrTest(Enum):
            FOO = "foo"
            FOO123 = "foo123"
            FU1 = "fu1"
            FOO_FU1 = "foo fu1"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
