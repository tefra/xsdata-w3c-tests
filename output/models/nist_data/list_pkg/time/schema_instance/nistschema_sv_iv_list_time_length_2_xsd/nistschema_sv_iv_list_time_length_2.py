from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-length-2-NS"


@dataclass
class NistschemaSvIvListTimeLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-length-2"
        namespace = "NISTSchema-SV-IV-list-time-length-2-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
