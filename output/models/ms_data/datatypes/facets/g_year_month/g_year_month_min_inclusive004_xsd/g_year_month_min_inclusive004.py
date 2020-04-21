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
            min_inclusive="2000-12",
            max_inclusive="2001-12"
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
