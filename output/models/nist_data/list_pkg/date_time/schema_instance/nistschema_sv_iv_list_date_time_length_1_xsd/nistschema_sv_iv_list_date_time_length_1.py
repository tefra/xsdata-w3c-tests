from dataclasses import dataclass, field
from datetime import datetime
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-length-1-NS"


@dataclass
class NistschemaSvIvListDateTimeLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-length-1"
        namespace = "NISTSchema-SV-IV-list-dateTime-length-1-NS"

    value: List[datetime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 5,
            "tokens": True,
        }
    )
