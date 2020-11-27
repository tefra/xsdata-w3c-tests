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
            "min_exclusive": "1999-01-31",
            "max_exclusive": "2000-05-31",
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
