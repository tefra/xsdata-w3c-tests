from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-length-2-NS"


@dataclass
class NistschemaSvIvListDurationLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-length-2"
        namespace = "NISTSchema-SV-IV-list-duration-length-2-NS"

    value: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
