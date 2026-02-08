from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguageMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-language-maxLength-1-NS"

    value: str = field(
        default="",
        metadata={
            "max_length": 2,
        },
    )
