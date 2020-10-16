from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FooType:
    """
    :ivar content:
    :ivar child_1:
    :ivar child_2:
    """
    class Meta:
        name = "fooType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    child_1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    child_2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class FooTest(FooType):
    class Meta:
        name = "fooTest"


@dataclass
class Root:
    """
    :ivar foo_test:
    """
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
