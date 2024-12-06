from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-maxLength-2-NS"


@dataclass
class NistschemaSvIvListFloatMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-float-maxLength-2-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        },
    )
