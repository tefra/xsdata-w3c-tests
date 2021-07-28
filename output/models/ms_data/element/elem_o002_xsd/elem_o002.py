from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[A-E]{1,2}",
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
            "required": True,
            "pattern": r"[A-E]{1,2}",
        }
    )
