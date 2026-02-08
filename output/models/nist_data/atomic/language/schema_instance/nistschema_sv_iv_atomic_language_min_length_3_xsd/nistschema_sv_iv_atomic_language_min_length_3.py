from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-minLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguageMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-language-minLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "min_length": 9,
        },
    )
