from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-minLength-2-NS"


@dataclass
class NistschemaSvIvListDateTimeMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-minLength-2"
        namespace = "NISTSchema-SV-IV-list-dateTime-minLength-2-NS"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        },
    )
