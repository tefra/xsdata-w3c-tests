from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"--[0-9]{2}-[0-9]{2}",
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
