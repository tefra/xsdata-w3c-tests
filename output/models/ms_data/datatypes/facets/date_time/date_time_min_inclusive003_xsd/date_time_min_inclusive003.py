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
            "min_inclusive": datetime(1981, 3, 12, 10, 30),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
