from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-length-4-NS"


@dataclass
class NistschemaSvIvListPositiveIntegerLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-length-4"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-length-4-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
