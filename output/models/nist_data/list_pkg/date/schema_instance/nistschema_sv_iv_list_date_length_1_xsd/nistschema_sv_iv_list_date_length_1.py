from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-length-1-NS"


@dataclass
class NistschemaSvIvListDateLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-length-1"
        namespace = "NISTSchema-SV-IV-list-date-length-1-NS"

    value: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
