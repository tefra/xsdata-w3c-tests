from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"


class NistschemaSvIvAtomicQnameEnumeration4Type(Enum):
    Q_TTHE_WITH = QName("{http://www.nist.gov/xsdNS}tthe.with-")
    ETRANSFORMING_SPECIFIC_EMERGING_IS_DEVELOPED_ACT_RELA = QName(
        "{NISTSchema-SV-IV-atomic-QName-enumeration-4-NS}etransforming-specific.emerging_is-developed.act_rela"
    )
    YOF_AUTOMATIC_PARTNERSHIPS_AND_SET_SERIES_IS_KEY_E = QName(
        "{NISTSchema-SV-IV-atomic-QName-enumeration-4-NS}yof_automatic-partnerships.and.set-series_is.key.e"
    )
    FAND_IS_INCLUDE_VOCA_JWORK_TOOLS_AND_WIDELY_ELECTRONIC_MANIPUL = QName(
        "{http://www.nist.gov/xsdNS}jwork.tools-and.widely.electronic_manipul"
    )
    TMANY_RETRIEVAL_WITH_LANGUAGE_BOTH_BE_RESULTS_IS_OF_B = QName(
        "{NISTSchema-SV-IV-atomic-QName-enumeration-4-NS}tmany-retrieval-with_language.both-be.results-is-of-b"
    )
    ITO_D_LCOMPUTING_OBJECT_FOR_A_MUST_BE_FROM_DESIGN_RO = QName(
        "{http://www.nist.gov/xsdNS}lcomputing-object_for_a_must-be-from-design-ro"
    )
    INTEROPERABILITY_S_LED_ALSO_SPECIFICATIONS_PROVIDE_WITH_IS_THU = QName(
        "{NISTSchema-SV-IV-atomic-QName-enumeration-4-NS}_interoperability.s.led_also-specifications_provide_with.is.thu"
    )
    THE_LWHICH = QName("{http://www.nist.gov/xsdNS}lwhich_")
    UTHE_BASE_THE_ABILITY_INTO_TARGET_THE_TESTABILITY_DISCOVE = QName(
        "{NISTSchema-SV-IV-atomic-QName-enumeration-4-NS}uthe.base_the_ability-into-target_the_testability-discove"
    )


@dataclass
class InteroperabilitySLedAlsoSpecificationsProvideWithIsThu:
    class Meta:
        name = (
            "_interoperability.s.led_also-specifications_provide_with.is.thu"
        )
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class EtransformingSpecificEmergingIsDevelopedActRela:
    class Meta:
        name = "etransforming-specific.emerging_is-developed.act_rela"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class TmanyRetrievalWithLanguageBothBeResultsIsOfB:
    class Meta:
        name = "tmany-retrieval-with_language.both-be.results-is-of-b"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class UtheBaseTheAbilityIntoTargetTheTestabilityDiscove:
    class Meta:
        name = "uthe.base_the_ability-into-target_the_testability-discove"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class YofAutomaticPartnershipsAndSetSeriesIsKeyE:
    class Meta:
        name = "yof_automatic-partnerships.and.set-series_is.key.e"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
