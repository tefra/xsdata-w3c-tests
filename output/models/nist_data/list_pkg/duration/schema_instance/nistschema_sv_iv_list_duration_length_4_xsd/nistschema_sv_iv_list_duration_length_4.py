from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-length-4-NS"


@dataclass
class NistschemaSvIvListDurationLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-length-4"
        namespace = "NISTSchema-SV-IV-list-duration-length-4-NS"

    value: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
