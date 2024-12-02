from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-minLength-1-NS"


@dataclass
class NistschemaSvIvListFloatMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-minLength-1"
        namespace = "NISTSchema-SV-IV-list-float-minLength-1-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
