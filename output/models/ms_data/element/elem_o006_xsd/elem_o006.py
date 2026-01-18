from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"
        nillable = True

    value: None | str = field(
        default="",
        metadata={
            "min_length": 3,
            "nillable": True,
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_test: None | FooTest = field(
        metadata={
            "name": "fooTest",
            "type": "Element",
            "nillable": True,
        }
    )
