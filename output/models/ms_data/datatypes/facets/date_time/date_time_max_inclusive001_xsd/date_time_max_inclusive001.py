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
            max_inclusive="1981-03-12T10:30:00"
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
