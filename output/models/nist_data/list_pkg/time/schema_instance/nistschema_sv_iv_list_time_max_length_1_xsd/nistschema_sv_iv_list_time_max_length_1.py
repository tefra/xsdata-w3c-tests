from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-maxLength-1-NS"


@dataclass
class NistschemaSvIvListTimeMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-time-maxLength-1-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
