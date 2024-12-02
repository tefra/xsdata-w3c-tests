from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-length-2-NS"


@dataclass
class NistschemaSvIvListFloatLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-length-2"
        namespace = "NISTSchema-SV-IV-list-float-length-2-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
