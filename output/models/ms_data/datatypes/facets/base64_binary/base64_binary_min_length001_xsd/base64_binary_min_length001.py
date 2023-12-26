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
            "min_length": 4,
            "format": "base64",
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
