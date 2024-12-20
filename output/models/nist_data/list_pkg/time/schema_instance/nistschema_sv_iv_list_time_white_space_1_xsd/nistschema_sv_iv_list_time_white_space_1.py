from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListTimeWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-time-whiteSpace-1-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
