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
            "max_length": 4,
            "format": "base16",
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
