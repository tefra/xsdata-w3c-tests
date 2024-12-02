from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-minLength-4-NS"


@dataclass
class NistschemaSvIvListDateTimeMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-minLength-4"
        namespace = "NISTSchema-SV-IV-list-dateTime-minLength-4-NS"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
