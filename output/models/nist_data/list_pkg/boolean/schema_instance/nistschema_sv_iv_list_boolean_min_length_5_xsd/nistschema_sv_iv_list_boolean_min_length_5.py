from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-minLength-5-NS"


@dataclass
class NistschemaSvIvListBooleanMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-minLength-5"
        namespace = "NISTSchema-SV-IV-list-boolean-minLength-5-NS"

    value: list[bool] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
