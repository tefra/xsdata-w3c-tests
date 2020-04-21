from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Anyuri:
    """
    :ivar value:
    """
    class Meta:
        name = "anyuri"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class BoolType:
    """
    :ivar value:
    """
    class Meta:
        name = "bool"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Date:
    """
    :ivar value:
    """
    class Meta:
        name = "date"

    value: Optional["str"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Datetime:
    """
    :ivar value:
    """
    class Meta:
        name = "datetime"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Day:
    """
    :ivar value:
    """
    class Meta:
        name = "day"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Decimal:
    """
    :ivar value:
    """
    class Meta:
        name = "decimal"

    value: Optional["Decimal"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Double:
    """
    :ivar value:
    """
    class Meta:
        name = "double"

    value: Optional["Decimal"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Duration:
    """
    :ivar value:
    """
    class Meta:
        name = "duration"

    value: Optional["str"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Entity:
    """
    :ivar value:
    """
    class Meta:
        name = "entity"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FloatType:
    """
    :ivar value:
    """
    class Meta:
        name = "float"

    value: Optional["float"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Hexbinary:
    """
    :ivar value:
    """
    class Meta:
        name = "hexbinary"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IntType:
    """
    :ivar value:
    """
    class Meta:
        name = "int"

    value: Optional["int"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Item:
    """
    :ivar any_element:
    """
    class Meta:
        name = "item"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Month:
    """
    :ivar value:
    """
    class Meta:
        name = "month"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Monthday:
    """
    :ivar value:
    """
    class Meta:
        name = "monthday"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class String:
    """
    :ivar value:
    """
    class Meta:
        name = "string"

    value: Optional["str"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Time:
    """
    :ivar value:
    """
    class Meta:
        name = "time"

    value: Optional["str"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Year:
    """
    :ivar value:
    """
    class Meta:
        name = "year"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar entity:
    :ivar anyuri:
    :ivar hexbinary:
    :ivar month:
    :ivar day:
    :ivar monthday:
    :ivar year:
    :ivar date:
    :ivar time:
    :ivar datetime:
    :ivar duration:
    :ivar decimal:
    :ivar double:
    :ivar float_value:
    :ivar bool_value:
    :ivar int_value:
    :ivar string:
    :ivar item:
    """
    class Meta:
        name = "root"

    entity: List[Entity] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    anyuri: List[Anyuri] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    hexbinary: List[Hexbinary] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    month: List[Month] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    day: List[Day] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    monthday: List[Monthday] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    year: List[Year] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    date: List[Date] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    time: List[Time] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    datetime: List[Datetime] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    duration: List[Duration] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    decimal: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    double: List[Double] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    float_value: List[FloatType] = field(
        default_factory=list,
        metadata=dict(
            name="float",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    bool_value: List[BoolType] = field(
        default_factory=list,
        metadata=dict(
            name="bool",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    int_value: List[IntType] = field(
        default_factory=list,
        metadata=dict(
            name="int",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    string: List[String] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    item: List[Item] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
