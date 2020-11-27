from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-4-NS"


@dataclass
class NistschemaSvIvListDateTimeMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 8,
            "tokens": True,
        }
    )
