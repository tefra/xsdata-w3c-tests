from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-3-NS"


@dataclass
class NistschemaSvIvListDoubleMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-3-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
