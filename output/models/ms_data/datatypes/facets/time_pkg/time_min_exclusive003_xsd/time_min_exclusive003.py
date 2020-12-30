from dataclasses import dataclass, field
from datetime import time, timedelta, timezone
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[time] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_exclusive": time(10, 21, tzinfo=timezone(timedelta(days=-1, seconds=68400))),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
