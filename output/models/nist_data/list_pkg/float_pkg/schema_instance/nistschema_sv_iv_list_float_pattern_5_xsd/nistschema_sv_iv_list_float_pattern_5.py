from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-pattern-5-NS"


@dataclass
class NistschemaSvIvListFloatPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-pattern-5"
        namespace = "NISTSchema-SV-IV-list-float-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1}E\-\d{2} \.\d{2}E\-\d{1} \d{3}E\d{1} \d{1}\.\d{3}E\d{2} \d{1}\.\d{4}E\-\d{2} \d{1}\.\d{5}E\-\d{1} \d{1}\.\d{6}E\d{1} \d{1}\.\d{7}E\d{2}",
            "tokens": True,
        },
    )
