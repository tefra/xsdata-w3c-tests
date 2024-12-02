from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-minLength-5-NS"


@dataclass
class NistschemaSvIvListNameMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-minLength-5"
        namespace = "NISTSchema-SV-IV-list-Name-minLength-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
