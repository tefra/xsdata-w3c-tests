from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union


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
            required=True,
            tokens=True
        )
    )

    class Value(Enum):
        """
        :cvar WA:
        :cvar OR_VALUE:
        """
        WA = "WA"
        OR_VALUE = "OR"


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: List[Union[int, "Root.Value"]] = field(
        default_factory=list,
        metadata=dict(
            name="fooTest",
            type="Element",
            required=True,
            tokens=True
        )
    )

    class Value(Enum):
        """
        :cvar WA:
        :cvar OR_VALUE:
        """
        WA = "WA"
        OR_VALUE = "OR"
