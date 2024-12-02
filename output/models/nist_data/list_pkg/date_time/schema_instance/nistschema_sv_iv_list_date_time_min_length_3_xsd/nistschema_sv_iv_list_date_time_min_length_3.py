from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-minLength-3-NS"


@dataclass
class NistschemaSvIvListDateTimeMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-minLength-3"
        namespace = "NISTSchema-SV-IV-list-dateTime-minLength-3-NS"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
