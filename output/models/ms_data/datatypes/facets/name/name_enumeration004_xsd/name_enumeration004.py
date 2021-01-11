from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooTypeFoo(Enum):
    FOO = "foo"
    FOO123 = "foo123"
    FU1 = "fu1"


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[FooTypeFoo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
