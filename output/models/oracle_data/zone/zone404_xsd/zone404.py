from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "explicit_timezone": "prohibited",
        },
    )
