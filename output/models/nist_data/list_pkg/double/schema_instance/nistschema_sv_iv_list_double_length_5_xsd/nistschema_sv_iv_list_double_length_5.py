from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-length-5-NS"


@dataclass
class NistschemaSvIvListDoubleLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-length-5"
        namespace = "NISTSchema-SV-IV-list-double-length-5-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
