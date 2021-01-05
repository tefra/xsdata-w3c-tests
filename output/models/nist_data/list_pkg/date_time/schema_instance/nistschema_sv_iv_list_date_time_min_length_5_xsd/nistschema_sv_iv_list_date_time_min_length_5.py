from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-minLength-5-NS"


@dataclass
class NistschemaSvIvListDateTimeMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-minLength-5"
        namespace = "NISTSchema-SV-IV-list-dateTime-minLength-5-NS"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 10,
            "tokens": True,
        }
    )
