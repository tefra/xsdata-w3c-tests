from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Item0To1:
    """
    :ivar x:
    """
    class Meta:
        name = "item0to1"
        namespace = "foo"

    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Item0To2:
    """
    :ivar x:
    """
    class Meta:
        name = "item0to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        }
    )


@dataclass
class Item0ToX:
    """
    :ivar x:
    """
    class Meta:
        name = "item0toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Item1To2:
    """
    :ivar x:
    """
    class Meta:
        name = "item1to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class Item1ToX:
    """
    :ivar x:
    """
    class Meta:
        name = "item1toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Item2To2:
    """
    :ivar x:
    """
    class Meta:
        name = "item2to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )


@dataclass
class Item2ToX:
    """
    :ivar x:
    """
    class Meta:
        name = "item2toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        }
    )


@dataclass
class Item3To7:
    """
    :ivar x:
    """
    class Meta:
        name = "item3to7"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 3,
            "max_occurs": 7,
        }
    )


@dataclass
class Root:
    """
    :ivar item0to1:
    :ivar item0to2:
    :ivar item0to_x:
    :ivar item1to2:
    :ivar item1to_x:
    :ivar item2to2:
    :ivar item2to_x:
    :ivar item3to7:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    item0to1: List[Item0To1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item0to2: List[Item0To2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item0to_x: List[Item0ToX] = field(
        default_factory=list,
        metadata={
            "name": "item0toX",
            "type": "Element",
        }
    )
    item1to2: List[Item1To2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item1to_x: List[Item1ToX] = field(
        default_factory=list,
        metadata={
            "name": "item1toX",
            "type": "Element",
        }
    )
    item2to2: List[Item2To2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item2to_x: List[Item2ToX] = field(
        default_factory=list,
        metadata={
            "name": "item2toX",
            "type": "Element",
        }
    )
    item3to7: List[Item3To7] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
