from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    foo1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    foo2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ext_foo: None | int = field(
        default=None,
        metadata={
            "name": "extFoo",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc(Test):
    class Meta:
        name = "doc"
