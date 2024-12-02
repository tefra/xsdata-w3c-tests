from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-minLength-5-NS"


@dataclass
class NistschemaSvIvListDurationMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-minLength-5"
        namespace = "NISTSchema-SV-IV-list-duration-minLength-5-NS"

    value: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
