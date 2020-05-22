from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    """
    :ivar any_element:
    """
    class Meta:
        name = "fooTest"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


class MyUnion(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_7:
    :cvar VALUE_8:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_7 = "7"
    VALUE_8 = "8"


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
