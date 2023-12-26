from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "foo"


@dataclass
class Item0To1:
    class Meta:
        name = "item0to1"
        namespace = "foo"

    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Item0To2:
    class Meta:
        name = "item0to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )


@dataclass
class Item0ToX:
    class Meta:
        name = "item0toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Item1To2:
    class Meta:
        name = "item1to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class Item1ToX:
    class Meta:
        name = "item1toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Item2To2:
    class Meta:
        name = "item2to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )


@dataclass
class Item2ToX:
    class Meta:
        name = "item2toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        },
    )


@dataclass
class Item3To7:
    class Meta:
        name = "item3to7"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 3,
            "max_occurs": 7,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    choice: List[
        Union[
            Item0To1,
            Item0To2,
            Item0ToX,
            Item1To2,
            Item1ToX,
            Item2To2,
            Item2ToX,
            Item3To7,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "item0to1",
                    "type": Item0To1,
                },
                {
                    "name": "item0to2",
                    "type": Item0To2,
                },
                {
                    "name": "item0toX",
                    "type": Item0ToX,
                },
                {
                    "name": "item1to2",
                    "type": Item1To2,
                },
                {
                    "name": "item1toX",
                    "type": Item1ToX,
                },
                {
                    "name": "item2to2",
                    "type": Item2To2,
                },
                {
                    "name": "item2toX",
                    "type": Item2ToX,
                },
                {
                    "name": "item3to7",
                    "type": Item3To7,
                },
            ),
        },
    )
