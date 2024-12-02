from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-pattern-5-NS"


@dataclass
class NistschemaSvIvListStringPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-string-pattern-5"
        namespace = "NISTSchema-SV-IV-list-string-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_17435-1843 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_16376 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_11348 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14973 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16518-1410 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10254-1649 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_17642 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18742 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17310-1594",
            "tokens": True,
        },
    )
