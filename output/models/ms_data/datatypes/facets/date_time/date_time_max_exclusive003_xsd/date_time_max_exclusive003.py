from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_exclusive": "1999-05-12T10:31:00",
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
