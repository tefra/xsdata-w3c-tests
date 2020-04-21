from dataclasses import dataclass, field
from typing import List
from output.models.saxon_data.override.over002_xsd.over002 import (
    Para,
)


@dataclass
class Doc:
    """
    :ivar para:
    """
    class Meta:
        name = "doc"

    para: List[Para] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
