from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-length-3-NS"


@dataclass
class NistschemaSvIvListDoubleLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-length-3"
        namespace = "NISTSchema-SV-IV-list-double-length-3-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
