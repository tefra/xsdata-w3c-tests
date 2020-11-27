from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateTimeMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "2030-12-31T23:59:59",
        }
    )
