from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooTypeFoo(Enum):
    ADF789 = b"\xad\xf7\x89"


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
            "format": "base16",
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
