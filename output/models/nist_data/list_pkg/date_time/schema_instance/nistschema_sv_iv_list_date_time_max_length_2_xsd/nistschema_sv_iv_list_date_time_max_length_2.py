from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-2-NS"


@dataclass
class NistschemaSvIvListDateTimeMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-2-NS"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        }
    )
