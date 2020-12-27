from dataclasses import dataclass, field
from datetime import datetime
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDateTimeMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-1-NS"

    value: List[datetime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 5,
            "tokens": True,
        }
    )
