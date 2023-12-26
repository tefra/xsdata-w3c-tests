from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooTypeFoo(Enum):
    MS0Y_LTM = b"1-2-3"


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
            "format": "base64",
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
