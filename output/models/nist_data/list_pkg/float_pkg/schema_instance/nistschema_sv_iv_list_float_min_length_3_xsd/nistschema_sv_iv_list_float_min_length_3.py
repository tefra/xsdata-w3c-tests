from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-minLength-3-NS"


@dataclass
class NistschemaSvIvListFloatMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-minLength-3"
        namespace = "NISTSchema-SV-IV-list-float-minLength-3-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
