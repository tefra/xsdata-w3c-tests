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
            pattern=r"[a-z]{3}"
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"