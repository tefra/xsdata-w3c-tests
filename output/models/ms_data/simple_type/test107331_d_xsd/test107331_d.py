from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[object] = field(default=None)


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class C:
    class Meta:
        name = "c"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class D:
    class Meta:
        name = "d"

    value: List[Union[float, int, bool]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class Item:
    class Meta:
        name = "item"

    value: Optional[object] = field(default=None)


@dataclass
class Root:
    class Meta:
        name = "root"

    choice: List[Union[D, C, B, A, Item]] = field(
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
