from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-2-NS"


class NistschemaSvIvAtomicIdEnumeration2Type(Enum):
    JREQUESTING_METHODS_IN = "jrequesting-methods-in"
    PDATA_TECHNOLOGIES_WILL_THAT_THEIR_AT_ME = (
        "pdata_technologies-will-that_their-at_me"
    )
    TRESULT_A_OF_METHODS_AS_OF_NETWORKS_AND_SPECIFICA = (
        "tresult-a-of-methods-as.of-networks_and.specifica"
    )
    MINDUSTRY_DESIGNED_MATCH_AND_INFLUENCE_TO_THOSE_WILL = (
        "mindustry.designed_match.and.influence_to_those.will"
    )
    JMETHODS_WIDE_UTILIZE_KNOWN_DATA_ORGANIZATIO = (
        "jmethods-wide.utilize-known-data-organizatio"
    )
    OF_OF_A_CONFERENCES_PROMINENT_ORGANIZATIONS_AS_RECENT_TE = (
        "_of_of_a-conferences_prominent-organizations-as_recent_te"
    )
    SVISIBLY_REGISTRY_IS_SUPPORT_FOR_WILL_INDUSTRY_IN_PROVIDE_AND = (
        "svisibly.registry_is_support_for-will.industry-in_provide.and"
    )
    LRIGOROUS_BE_PR = "lrigorous-be-pr"


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-2-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-2-NS"

    value: NistschemaSvIvAtomicIdEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
