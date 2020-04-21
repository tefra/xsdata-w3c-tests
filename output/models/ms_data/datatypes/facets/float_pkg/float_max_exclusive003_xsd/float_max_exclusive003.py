from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[float] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            max_exclusive=7.7
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
