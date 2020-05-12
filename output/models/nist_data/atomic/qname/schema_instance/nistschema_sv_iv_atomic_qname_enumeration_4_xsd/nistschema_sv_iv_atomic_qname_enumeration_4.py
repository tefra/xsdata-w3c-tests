from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"


class NistschemaSvIvAtomicQnameEnumeration4Type(Enum):
    """
    :cvar Q_TTHE_WITH:
    :cvar ETRANSFORMING_SPECIFIC_EMERGING_IS_DEVELOPED_ACT_RELA:
    :cvar YOF_AUTOMATIC_PARTNERSHIPS_AND_SET_SERIES_IS_KEY_E:
    :cvar FAND_IS_INCLUDE_VOCA_JWORK_TOOLS_AND_WIDELY_ELECTRONIC_MANIPUL:
    :cvar TMANY_RETRIEVAL_WITH_LANGUAGE_BOTH_BE_RESULTS_IS_OF_B:
    :cvar ITO_D_LCOMPUTING_OBJECT_FOR_A_MUST_BE_FROM_DESIGN_RO:
    :cvar INTEROPERABILITY_S_LED_ALSO_SPECIFICATIONS_PROVIDE_WITH_IS_THU:
    :cvar THE_LWHICH:
    :cvar UTHE_BASE_THE_ABILITY_INTO_TARGET_THE_TESTABILITY_DISCOVE:
    """
    Q_TTHE_WITH = QName("http://www.nist.gov/xsdNS", "tthe.with-")
    ETRANSFORMING_SPECIFIC_EMERGING_IS_DEVELOPED_ACT_RELA = QName("NISTSchema-SV-IV-atomic-QName-enumeration-4-NS", "etransforming-specific.emerging_is-developed.act_rela")
    YOF_AUTOMATIC_PARTNERSHIPS_AND_SET_SERIES_IS_KEY_E = QName("NISTSchema-SV-IV-atomic-QName-enumeration-4-NS", "yof_automatic-partnerships.and.set-series_is.key.e")
    FAND_IS_INCLUDE_VOCA_JWORK_TOOLS_AND_WIDELY_ELECTRONIC_MANIPUL = QName("http://www.nist.gov/xsdNS", "jwork.tools-and.widely.electronic_manipul")
    TMANY_RETRIEVAL_WITH_LANGUAGE_BOTH_BE_RESULTS_IS_OF_B = QName("NISTSchema-SV-IV-atomic-QName-enumeration-4-NS", "tmany-retrieval-with_language.both-be.results-is-of-b")
    ITO_D_LCOMPUTING_OBJECT_FOR_A_MUST_BE_FROM_DESIGN_RO = QName("http://www.nist.gov/xsdNS", "lcomputing-object_for_a_must-be-from-design-ro")
    INTEROPERABILITY_S_LED_ALSO_SPECIFICATIONS_PROVIDE_WITH_IS_THU = QName("NISTSchema-SV-IV-atomic-QName-enumeration-4-NS", "_interoperability.s.led_also-specifications_provide_with.is.thu")
    THE_LWHICH = QName("http://www.nist.gov/xsdNS", "lwhich_")
    UTHE_BASE_THE_ABILITY_INTO_TARGET_THE_TESTABILITY_DISCOVE = QName("NISTSchema-SV-IV-atomic-QName-enumeration-4-NS", "uthe.base_the_ability-into-target_the_testability-discove")


@dataclass
class TypeInteroperabilitySLedAlsoSpecificationsProvideWithIsThu:
    """
    :ivar value:
    """
    class Meta:
        name = "_interoperability.s.led_also-specifications_provide_with.is.thu"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class EtransformingSpecificEmergingIsDevelopedActRela:
    """
    :ivar value:
    """
    class Meta:
        name = "etransforming-specific.emerging_is-developed.act_rela"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TmanyRetrievalWithLanguageBothBeResultsIsOfB:
    """
    :ivar value:
    """
    class Meta:
        name = "tmany-retrieval-with_language.both-be.results-is-of-b"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class UtheBaseTheAbilityIntoTargetTheTestabilityDiscove:
    """
    :ivar value:
    """
    class Meta:
        name = "uthe.base_the_ability-into-target_the_testability-discove"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class YofAutomaticPartnershipsAndSetSeriesIsKeyE:
    """
    :ivar value:
    """
    class Meta:
        name = "yof_automatic-partnerships.and.set-series_is.key.e"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
