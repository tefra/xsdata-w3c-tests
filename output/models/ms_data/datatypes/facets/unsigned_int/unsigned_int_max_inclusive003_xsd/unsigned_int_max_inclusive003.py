from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            max_inclusive=7.0
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
