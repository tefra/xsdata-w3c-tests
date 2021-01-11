from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-length-3-NS"


@dataclass
class NistschemaSvIvListDateTimeLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-length-3"
        namespace = "NISTSchema-SV-IV-list-dateTime-length-3-NS"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 7,
            "tokens": True,
        }
    )
