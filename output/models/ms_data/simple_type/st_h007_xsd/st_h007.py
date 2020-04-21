from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: Optional["FooTest.Value"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )

    class Value(Enum):
        """
        :cvar CA:
        """
        CA = "CA"


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
