from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    value: str = field(
        default="",
        metadata={
            "white_space": "collapse",
        },
    )
    my_attr: None | str = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
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
