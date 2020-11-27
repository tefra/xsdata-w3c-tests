from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


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
        attr_test: List["FooType.Foo.AttrTest"] = field(
            default_factory=list,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "tokens": True,
            }
        )

        class AttrTest(Enum):
            FOO = "foo"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
