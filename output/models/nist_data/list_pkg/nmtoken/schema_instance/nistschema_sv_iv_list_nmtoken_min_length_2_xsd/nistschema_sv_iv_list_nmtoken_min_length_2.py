from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-minLength-2-NS"


@dataclass
class NistschemaSvIvListNmtokenMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-minLength-2"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-minLength-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        },
    )
