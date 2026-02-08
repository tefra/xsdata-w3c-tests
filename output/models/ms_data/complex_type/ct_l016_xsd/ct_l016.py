from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    child_1: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    child_2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class FooTest(FooType):
    class Meta:
        name = "fooTest"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_test: FooTest = field(
        metadata={
            "name": "fooTest",
            "type": "Element",
        }
    )
