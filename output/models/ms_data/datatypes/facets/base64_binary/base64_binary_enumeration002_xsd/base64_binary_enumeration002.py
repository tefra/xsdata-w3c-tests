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
            "format": "base64",
        }
    )

    class Foo(Enum):
        MS0Y_LTM = b"1-2-3"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
