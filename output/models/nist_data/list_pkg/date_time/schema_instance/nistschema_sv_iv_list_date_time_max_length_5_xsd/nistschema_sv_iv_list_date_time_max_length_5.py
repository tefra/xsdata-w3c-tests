from dataclasses import dataclass, field
from datetime import datetime
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-5-NS"


@dataclass
class NistschemaSvIvListDateTimeMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-5-NS"

    value: List[datetime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 10,
            "tokens": True,
        }
    )
