from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


class MyListValue(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


class MyUnion(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_7 = "7"
    VALUE_8 = "8"


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
