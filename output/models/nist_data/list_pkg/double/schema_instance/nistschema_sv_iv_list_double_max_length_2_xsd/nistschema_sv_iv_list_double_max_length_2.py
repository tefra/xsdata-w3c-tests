from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-2-NS"


@dataclass
class NistschemaSvIvListDoubleMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-2-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        },
    )
