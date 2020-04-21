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
            max_inclusive="P2Y3MT2H"
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
