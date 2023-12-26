from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-whiteSpace-3-NS"


@dataclass
class NistschemaSvIvAtomicStringWhiteSpace3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-whiteSpace-3"
        namespace = "NISTSchema-SV-IV-atomic-string-whiteSpace-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "replace",
        },
    )
