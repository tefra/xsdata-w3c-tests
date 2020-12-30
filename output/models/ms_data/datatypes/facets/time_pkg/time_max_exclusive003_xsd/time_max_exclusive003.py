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
            "max_exclusive": time(13, 20, tzinfo=timezone(timedelta(days=-1, seconds=72000))),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
