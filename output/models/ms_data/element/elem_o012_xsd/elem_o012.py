from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=3
        )
    )


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata=dict(
            name="fooTest",
            type="Element",
            required=True
        )
    )
