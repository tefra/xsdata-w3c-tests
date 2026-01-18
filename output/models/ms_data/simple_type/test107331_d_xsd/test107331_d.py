from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"

    value: None | object = field(default=None)


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"

    value: float = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class D:
    class Meta:
        name = "d"

    value: list[float | int | bool] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Item:
    class Meta:
        name = "item"

    value: None | object = field(default=None)


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    choice: list[D | C | B | A | Item] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d",
                    "type": D,
                },
                {
                    "name": "c",
                    "type": C,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "a",
                    "type": A,
                },
                {
                    "name": "item",
                    "type": Item,
                },
            ),
        },
    )
