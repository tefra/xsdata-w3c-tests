from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class NotaFooBar(Enum):
    """
    :cvar FOO:
    :cvar BAR:
    :cvar BEZ:
    """
    FOO = "foo"
    BAR = "bar"
    BEZ = "bez"


@dataclass
class StructuredDate:
    """
    :ivar year:
    :ivar month:
    :ivar day:
    :ivar nota:
    """
    class Meta:
        name = "structuredDate"

    year: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    month: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    day: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    nota: Optional[NotaFooBar] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar para:
    :ivar bezzle:
    """
    class Meta:
        name = "doc"

    para: List[StructuredDate] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    bezzle: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
