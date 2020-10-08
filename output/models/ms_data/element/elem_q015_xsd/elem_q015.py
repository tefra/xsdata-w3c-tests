from dataclasses import dataclass, field
from typing import List, Optional


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
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="fooTest",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
