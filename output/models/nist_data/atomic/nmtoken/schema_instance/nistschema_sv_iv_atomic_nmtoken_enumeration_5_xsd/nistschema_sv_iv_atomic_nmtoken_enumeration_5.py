from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-5-NS"


class NistschemaSvIvAtomicNmtokenEnumeration5Type(Enum):
    CROSS_OVER_RELATED_AMBIGUITIES_THE_EX = (
        "cross-over.related.ambiguities-The.Ex"
    )
    VIA_DISCUSSIONS = "via.discussions"
    HAVE_AUTOMATIC = "have_automatic"
    PROMINENT_RETRIEVE_RIGOROUS_A_OF_FOR_DEFINE_AND_PARTICIPANTS_JA = (
        "prominent_retrieve_rigorous.a:of-for.define-and:participants:Ja"
    )
    ONLY_D = "only:d"
    OBJECT_RAPID_OF_PARTNERS_INCLUDING_DOCUME = (
        "object_rapid.of:partners:including.docume"
    )
    DEFINE_A_SCHEMAS_OASIS_WORKING_CONFERENCE_PROFI = (
        "define.a:Schemas-OASIS:working.Conference_profi"
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNmtokenEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-5-NS"

    value: NistschemaSvIvAtomicNmtokenEnumeration5Type = field()
