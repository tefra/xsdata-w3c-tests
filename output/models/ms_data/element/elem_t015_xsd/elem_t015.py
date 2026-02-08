from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


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
