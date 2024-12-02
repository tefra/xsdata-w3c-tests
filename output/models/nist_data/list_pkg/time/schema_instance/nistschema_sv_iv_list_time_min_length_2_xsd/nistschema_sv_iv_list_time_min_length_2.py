from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-minLength-2-NS"


@dataclass
class NistschemaSvIvListTimeMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-minLength-2"
        namespace = "NISTSchema-SV-IV-list-time-minLength-2-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        },
    )
