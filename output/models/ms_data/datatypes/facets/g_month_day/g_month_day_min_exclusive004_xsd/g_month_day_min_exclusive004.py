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
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            min_exclusive="--01-01",
            max_inclusive="--10-01"
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
