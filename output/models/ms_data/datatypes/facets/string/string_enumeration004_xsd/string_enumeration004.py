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

    class Foo(Enum):
        FOO = "foo"
        VALUE_123 = "123"
        FOO123 = "foo123"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
