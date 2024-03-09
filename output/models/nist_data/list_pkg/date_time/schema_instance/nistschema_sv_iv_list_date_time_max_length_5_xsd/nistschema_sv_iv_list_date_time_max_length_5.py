from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-5-NS"


@dataclass
class NistschemaSvIvListDateTimeMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-5-NS"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
