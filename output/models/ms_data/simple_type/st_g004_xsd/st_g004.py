from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: List[Union[int, "FooTest.Value"]] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    class Value(Enum):
        """
        :cvar OR_VALUE:
        :cvar WA:
        """
        OR_VALUE = "OR"
        WA = "WA"


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
