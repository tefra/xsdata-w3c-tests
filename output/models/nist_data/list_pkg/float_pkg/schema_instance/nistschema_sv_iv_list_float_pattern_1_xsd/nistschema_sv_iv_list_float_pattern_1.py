from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-pattern-1-NS"


@dataclass
class NistschemaSvIvListFloatPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-pattern-1"
        namespace = "NISTSchema-SV-IV-list-float-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1}E\-\d{2} \.\d{2}E\-\d{1} \d{1}\.\d{2}E\d{1} \d{1}\.\d{3}E\d{2} \d{1}\.\d{7}E\-\d{2}",
            "tokens": True,
        },
    )
