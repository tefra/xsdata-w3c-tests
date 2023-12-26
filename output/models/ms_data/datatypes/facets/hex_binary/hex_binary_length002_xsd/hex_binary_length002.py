from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "length": 5,
            "format": "base16",
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
