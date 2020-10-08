from dataclasses import dataclass, field
from typing import List


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            required=True,
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

    foo_test: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="fooTest",
            type="Element",
            required=True,
            tokens=True
        )
    )
