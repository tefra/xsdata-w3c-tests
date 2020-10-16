from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-length-4-NS"


@dataclass
class NistschemaSvIvListDateTimeLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-length-4"
        namespace = "NISTSchema-SV-IV-list-dateTime-length-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
