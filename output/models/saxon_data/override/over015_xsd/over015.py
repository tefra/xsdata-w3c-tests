from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from output.models.saxon_data.override.over015_xsd.over015a import StructuredDate


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
