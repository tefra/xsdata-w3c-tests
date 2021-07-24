from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "child_1",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "child_2",
                    "type": int,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class FooTest(FooType):
    class Meta:
        name = "fooTest"


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
