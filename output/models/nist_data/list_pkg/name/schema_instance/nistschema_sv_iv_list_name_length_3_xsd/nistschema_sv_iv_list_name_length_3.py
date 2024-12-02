from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-length-3-NS"


@dataclass
class NistschemaSvIvListNameLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-length-3"
        namespace = "NISTSchema-SV-IV-list-Name-length-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
