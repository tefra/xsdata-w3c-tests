from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-pattern-4-NS"


@dataclass
class NistschemaSvIvListStringPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-string-pattern-4"
        namespace = "NISTSchema-SV-IV-list-string-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15352 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18423-1985 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15520-1083 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18786-1596 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_12834-1343",
            "tokens": True,
        },
    )
