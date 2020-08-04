from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"[0-8]{5}",
            tokens=True
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
