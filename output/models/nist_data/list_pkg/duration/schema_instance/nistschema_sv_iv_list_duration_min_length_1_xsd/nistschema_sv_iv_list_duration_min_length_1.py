from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-minLength-1-NS"


@dataclass
class NistschemaSvIvListDurationMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-minLength-1"
        namespace = "NISTSchema-SV-IV-list-duration-minLength-1-NS"

    value: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
