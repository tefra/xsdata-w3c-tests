from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-length-4-NS"


@dataclass
class NistschemaSvIvListDateTimeLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-length-4"
        namespace = "NISTSchema-SV-IV-list-dateTime-length-4-NS"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
