from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-4-NS"


class NistschemaSvIvAtomicIdEnumeration4Type(Enum):
    """
    :cvar FOR_NEWCOMERS_FOR_RESOURCES_FORUM_AND_THAN_MAINTAINED_SERIES:
    :cvar IIMPACT_THE_DEVICES_TEMPLATES_SY:
    :cvar NSOFTWARE_THE_FROM_COMMERCE_USING:
    :cvar HI:
    :cvar LPROVIDES_DISCOVER_OVER_CLEAN_REL:
    :cvar QBAN:
    :cvar WREGISTRIES_RESULT_MADE_KEY_THE_OF_WITHOUT_THE_CAN_ORGANIZATIO:
    :cvar STESTING_ADDRESSING_TH:
    """
    FOR_NEWCOMERS_FOR_RESOURCES_FORUM_AND_THAN_MAINTAINED_SERIES = "_for.newcomers_for-resources.forum_and-than.maintained-series-"
    IIMPACT_THE_DEVICES_TEMPLATES_SY = "iimpact-the.devices_templates_sy"
    NSOFTWARE_THE_FROM_COMMERCE_USING = "nsoftware.the.from_commerce_using-"
    HI = "hi"
    LPROVIDES_DISCOVER_OVER_CLEAN_REL = "lprovides.discover.over.clean.rel"
    QBAN = "qban"
    WREGISTRIES_RESULT_MADE_KEY_THE_OF_WITHOUT_THE_CAN_ORGANIZATIO = "wregistries_result_made_key.the.of_without_the.can.organizatio"
    STESTING_ADDRESSING_TH = "stesting-addressing_th"


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class NistschemaSvIvAtomicIdEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicIdEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
