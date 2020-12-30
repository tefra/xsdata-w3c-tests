from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[Duration] = field(
        default=None,
        metadata={
            "min_inclusive": Duration("-P3Y"),
            "max_inclusive": Duration("P3Y"),
        }
    )
