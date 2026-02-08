from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    content: list[object] = field(
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
