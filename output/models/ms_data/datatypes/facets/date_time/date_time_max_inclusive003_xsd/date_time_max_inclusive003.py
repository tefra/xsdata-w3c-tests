from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[datetime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": datetime(1999, 5, 12, 10, 31),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
