from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"


class NistschemaSvIvAtomicQnameEnumeration5Type(Enum):
    """
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_AMONG_TO_MUST_AND_INDUSTRY_FROM_THAT:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_FOR_FILES_SUPPLY_FOR_TO_MUST_MEASUR:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_I:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_HMANIPULATE_US:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_PS_PERVASIVE_IN_HOUSE_ON_PERFORMANCE_ALS:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_UTHE_BASE_THE_ABILITY_INTO_TARGET_THE_TESTABILITY_DISCOVE:
    """
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_AMONG_TO_MUST_AND_INDUSTRY_FROM_THAT = QName("http://www.nist.gov/xsdNS", "_among.to.must_and.industry-from-that_")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_FOR_FILES_SUPPLY_FOR_TO_MUST_MEASUR = QName("NISTSchema-SV-IV-atomic-QName-enumeration-5-NS", "_for-files.supply.for.to-must_measur")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_I = QName("http://www.nist.gov/xsdNS", "i")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_HMANIPULATE_US = QName("NISTSchema-SV-IV-atomic-QName-enumeration-5-NS", "hmanipulate-us")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_PS_PERVASIVE_IN_HOUSE_ON_PERFORMANCE_ALS = QName("NISTSchema-SV-IV-atomic-QName-enumeration-5-NS", "ps.pervasive.in-house_on.performance-als")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_5_NS_UTHE_BASE_THE_ABILITY_INTO_TARGET_THE_TESTABILITY_DISCOVE = QName("NISTSchema-SV-IV-atomic-QName-enumeration-5-NS", "uthe.base_the_ability-into-target_the_testability-discove")


@dataclass
class TypeForFilesSupplyForToMustMeasur:
    """
    :ivar value:
    """
    class Meta:
        name = "_for-files.supply.for.to-must_measur"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class HmanipulateUs:
    """
    :ivar value:
    """
    class Meta:
        name = "hmanipulate-us"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class PsPervasiveInHouseOnPerformanceAls:
    """
    :ivar value:
    """
    class Meta:
        name = "ps.pervasive.in-house_on.performance-als"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

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
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
