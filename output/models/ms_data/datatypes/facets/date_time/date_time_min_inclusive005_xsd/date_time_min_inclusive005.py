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
            min_inclusive="1981-03-12T10:30:00",
            max_exclusive="1999-05-12T10:31:00"
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"