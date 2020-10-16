from dataclasses import dataclass, field
from typing import List
from output.models.saxon_data.override.over012_xsd.over012 import StructuredDate


@dataclass
class Doc:
    """
    :ivar para:
    """
    class Meta:
        name = "doc"

    para: List[StructuredDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
