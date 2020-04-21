from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Item0to1:
    """
    :ivar x:
    """
    class Meta:
        name = "item0to1"
        namespace = "foo"

    x: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )


@dataclass
class Item0to2:
    """
    :ivar x:
    """
    class Meta:
        name = "item0to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class Item0toX:
    """
    :ivar x:
    """
    class Meta:
        name = "item0toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Item1to2:
    """
    :ivar x:
    """
    class Meta:
        name = "item1to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class Item1toX:
    """
    :ivar x:
    """
    class Meta:
        name = "item1toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Item2to2:
    """
    :ivar x:
    """
    class Meta:
        name = "item2to2"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )


@dataclass
class Item2toX:
    """
    :ivar x:
    """
    class Meta:
        name = "item2toX"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Item3to7:
    """
    :ivar x:
    """
    class Meta:
        name = "item3to7"
        namespace = "foo"

    x: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=3,
            max_occurs=7
        )
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

    item0to1: List[Item0to1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item0to2: List[Item0to2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item0to_x: List[Item0toX] = field(
        default_factory=list,
        metadata=dict(
            name="item0toX",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item1to2: List[Item1to2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item1to_x: List[Item1toX] = field(
        default_factory=list,
        metadata=dict(
            name="item1toX",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item2to2: List[Item2to2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item2to_x: List[Item2toX] = field(
        default_factory=list,
        metadata=dict(
            name="item2toX",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    item3to7: List[Item3to7] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
