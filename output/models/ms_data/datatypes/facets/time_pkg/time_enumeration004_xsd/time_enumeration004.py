from dataclasses import dataclass, field
from datetime import time, timedelta, timezone
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
        }
    )

    class Foo(Enum):
        VALUE_13_20_00_05_00 = time(13, 20, tzinfo=timezone(timedelta(days=-1, seconds=68400)))
        VALUE_13_20_00 = time(13, 20)
        VALUE_01_50_40 = time(1, 50, 40)


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
