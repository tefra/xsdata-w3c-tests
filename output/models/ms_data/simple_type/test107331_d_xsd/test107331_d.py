from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[object] = field(
        default=None
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class C:
    class Meta:
        name = "c"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class D:
    class Meta:
        name = "d"

    value: List[Union[float, int, bool]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class Item:
    class Meta:
        name = "item"

    value: Optional[object] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    choice: List[Union[object, bool, int, float]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d",
                    "type": List[Union[float, int, bool]],
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "c",
                    "type": List[float],
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "b",
                    "type": float,
                },
                {
                    "name": "a",
                    "type": object,
                },
                {
                    "name": "item",
                    "type": object,
                },
            ),
        }
    )
