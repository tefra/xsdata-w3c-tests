from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-length-5-NS"


@dataclass
class NistschemaSvIvListTimeLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-length-5"
        namespace = "NISTSchema-SV-IV-list-time-length-5-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
