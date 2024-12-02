from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-minLength-1-NS"


@dataclass
class NistschemaSvIvListIntMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-minLength-1"
        namespace = "NISTSchema-SV-IV-list-int-minLength-1-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
