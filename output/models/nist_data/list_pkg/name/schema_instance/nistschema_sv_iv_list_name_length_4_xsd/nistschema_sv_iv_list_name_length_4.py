from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-length-4-NS"


@dataclass
class NistschemaSvIvListNameLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-length-4"
        namespace = "NISTSchema-SV-IV-list-Name-length-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
