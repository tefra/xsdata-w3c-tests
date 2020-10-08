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
            pattern=r"[A-E]{1,2}"
        )
    )


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fooTest",
            type="Element",
            required=True,
            pattern=r"[A-E]{1,2}"
        )
    )
