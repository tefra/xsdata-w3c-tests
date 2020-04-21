from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-2-NS"


class NistschemaSvIvAtomicIdEnumeration2Type(Enum):
    """
    :cvar VALUE_OF_OF_A_CONFERENCES_PROMINENT_ORGANIZATIONS_AS_RECENT_TE:
    :cvar JMETHODS_WIDE_UTILIZE_KNOWN_DATA_ORGANIZATIO:
    :cvar JREQUESTING_METHODS_IN:
    :cvar LRIGOROUS_BE_PR:
    :cvar MINDUSTRY_DESIGNED_MATCH_AND_INFLUENCE_TO_THOSE_WILL:
    :cvar PDATA_TECHNOLOGIES_WILL_THAT_THEIR_AT_ME:
    :cvar SVISIBLY_REGISTRY_IS_SUPPORT_FOR_WILL_INDUSTRY_IN_PROVIDE_AND:
    :cvar TRESULT_A_OF_METHODS_AS_OF_NETWORKS_AND_SPECIFICA:
    """
    VALUE_OF_OF_A_CONFERENCES_PROMINENT_ORGANIZATIONS_AS_RECENT_TE = "_of_of_a-conferences_prominent-organizations-as_recent_te"
    JMETHODS_WIDE_UTILIZE_KNOWN_DATA_ORGANIZATIO = "jmethods-wide.utilize-known-data-organizatio"
    JREQUESTING_METHODS_IN = "jrequesting-methods-in"
    LRIGOROUS_BE_PR = "lrigorous-be-pr"
    MINDUSTRY_DESIGNED_MATCH_AND_INFLUENCE_TO_THOSE_WILL = "mindustry.designed_match.and.influence_to_those.will"
    PDATA_TECHNOLOGIES_WILL_THAT_THEIR_AT_ME = "pdata_technologies-will-that_their-at_me"
    SVISIBLY_REGISTRY_IS_SUPPORT_FOR_WILL_INDUSTRY_IN_PROVIDE_AND = "svisibly.registry_is_support_for-will.industry-in_provide.and"
    TRESULT_A_OF_METHODS_AS_OF_NETWORKS_AND_SPECIFICA = "tresult-a-of-methods-as.of-networks_and.specifica"


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicIdEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicIdEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
