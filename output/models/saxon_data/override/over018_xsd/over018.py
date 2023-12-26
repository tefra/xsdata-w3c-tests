from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://example.com/over018"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://example.com/over018"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
