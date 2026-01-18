from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-3-NS"


class NistschemaSvIvAtomicNmtokenEnumeration3Type(Enum):
    NEEDED_AS_IS_FURTHERMORE_RETRIEVE_TO_MEANS_FIND = (
        "needed:as-is.Furthermore_retrieve-to.means.find"
    )
    THE_UNITED_DEVELOPMENT_AND_EACH_DISCO = (
        "the_United-development-and-each-disco"
    )
    GROUPS_IN = "Groups_in_"
    INDUSTRY_ADVANCEMENT_PERMITTING_CONFORMANCE_AND_WILL_PARTICI = (
        "industry:Advancement.permitting_conformance.and_will-partici"
    )
    THAN_BUSINESS_EB_XML_OF_FOR_OF_ELECTRONIC_DIAGNOSTI = (
        "than:business:ebXML-of:for.of_electronic.diagnosti"
    )
    MANUAL_THAT_TOOLS_STANDARD = "manual.that.tools.standard"
    DISCOVER_OASIS_VERSIONS_HAS_COMPATIBILITY_EMBEDDED = (
        "discover.OASIS-versions.has.compatibility-embedded"
    )
    BROWSERS_DOM_BOTH_CHAIN_THE_RECOMMENDING_C = (
        "browsers:DOM:both.chain:the:recommending.C"
    )
    METHODS_PROFILES_ENSURE_MANIPULATE_B = (
        "methods.profiles.ensure_manipulate.b"
    )
    CRITERIA_MUST_TAR = "criteria:-must-tar"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNmtokenEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-enumeration-3-NS"

    value: NistschemaSvIvAtomicNmtokenEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
