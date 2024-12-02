from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-length-3-NS"


@dataclass
class NistschemaSvIvListTimeLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-length-3"
        namespace = "NISTSchema-SV-IV-list-time-length-3-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
