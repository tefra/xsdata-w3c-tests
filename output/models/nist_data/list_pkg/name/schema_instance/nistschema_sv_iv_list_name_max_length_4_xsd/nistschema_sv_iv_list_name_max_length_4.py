from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-maxLength-4-NS"


@dataclass
class NistschemaSvIvListNameMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-Name-maxLength-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
