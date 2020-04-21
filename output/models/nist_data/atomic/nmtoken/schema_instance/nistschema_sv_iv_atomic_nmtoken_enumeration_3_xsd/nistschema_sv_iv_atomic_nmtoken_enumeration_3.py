from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-3-NS"


class NistschemaSvIvAtomicNmtokenEnumeration3Type(Enum):
    """
    :cvar GROUPS_IN:
    :cvar BROWSERS_DOM_BOTH_CHAIN_THE_RECOMMENDING_C:
    :cvar CRITERIA_MUST_TAR:
    :cvar DISCOVER_OASIS_VERSIONS_HAS_COMPATIBILITY_EMBEDDED:
    :cvar INDUSTRY_ADVANCEMENT_PERMITTING_CONFORMANCE_AND_WILL_PARTICI:
    :cvar MANUAL_THAT_TOOLS_STANDARD:
    :cvar METHODS_PROFILES_ENSURE_MANIPULATE_B:
    :cvar NEEDED_AS_IS_FURTHERMORE_RETRIEVE_TO_MEANS_FIND:
    :cvar THAN_BUSINESS_EB_XML_OF_FOR_OF_ELECTRONIC_DIAGNOSTI:
    :cvar THE_UNITED_DEVELOPMENT_AND_EACH_DISCO:
    """
    GROUPS_IN = "Groups_in_"
    BROWSERS_DOM_BOTH_CHAIN_THE_RECOMMENDING_C = "browsers:DOM:both.chain:the:recommending.C"
    CRITERIA_MUST_TAR = "criteria:-must-tar"
    DISCOVER_OASIS_VERSIONS_HAS_COMPATIBILITY_EMBEDDED = "discover.OASIS-versions.has.compatibility-embedded"
    INDUSTRY_ADVANCEMENT_PERMITTING_CONFORMANCE_AND_WILL_PARTICI = "industry:Advancement.permitting_conformance.and_will-partici"
    MANUAL_THAT_TOOLS_STANDARD = "manual.that.tools.standard"
    METHODS_PROFILES_ENSURE_MANIPULATE_B = "methods.profiles.ensure_manipulate.b"
    NEEDED_AS_IS_FURTHERMORE_RETRIEVE_TO_MEANS_FIND = "needed:as-is.Furthermore_retrieve-to.means.find"
    THAN_BUSINESS_EB_XML_OF_FOR_OF_ELECTRONIC_DIAGNOSTI = "than:business:ebXML-of:for.of_electronic.diagnosti"
    THE_UNITED_DEVELOPMENT_AND_EACH_DISCO = "the_United-development-and-each-disco"


@dataclass
class NistschemaSvIvAtomicNmtokenEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicNmtokenEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
