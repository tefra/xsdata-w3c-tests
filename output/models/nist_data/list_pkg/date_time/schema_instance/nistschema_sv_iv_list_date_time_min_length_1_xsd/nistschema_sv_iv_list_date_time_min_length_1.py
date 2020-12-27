from dataclasses import dataclass, field
from datetime import datetime
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-minLength-1-NS"


@dataclass
class NistschemaSvIvListDateTimeMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-minLength-1"
        namespace = "NISTSchema-SV-IV-list-dateTime-minLength-1-NS"

    value: List[datetime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 5,
            "tokens": True,
        }
    )
