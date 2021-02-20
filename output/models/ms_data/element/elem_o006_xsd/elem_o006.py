from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"
        nillable = True

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 3,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "min_length": 3,
            "nillable": True,
        }
    )
