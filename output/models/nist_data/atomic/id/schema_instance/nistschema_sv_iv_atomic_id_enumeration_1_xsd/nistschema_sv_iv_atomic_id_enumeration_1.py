from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-1-NS"


class NistschemaSvIvAtomicIdEnumeration1Type(Enum):
    """
    :cvar ITEMPLATES_RESOURCE:
    :cvar HORGANIZ:
    :cvar WORK_OF_IS_DOCUMENTS_RELATIONSHIPS_OF_AT_OBJECT:
    :cvar MACCOMPLISH_VERSIONS_CARE_DEFINE_AND_PR:
    :cvar DALLOW_SUCCESS_OF_DEVICES_ENOUGH_THE_RETRIEVE:
    :cvar MANUFACTURERS_INFORMATION_WORLD_TH:
    :cvar HDOCUMENTS_IMPACT:
    """
    ITEMPLATES_RESOURCE = "itemplates.resource_"
    HORGANIZ = "horganiz"
    WORK_OF_IS_DOCUMENTS_RELATIONSHIPS_OF_AT_OBJECT = "_work-of-is-documents_relationships-of_at.object"
    MACCOMPLISH_VERSIONS_CARE_DEFINE_AND_PR = "maccomplish.versions.care.define-and.pr"
    DALLOW_SUCCESS_OF_DEVICES_ENOUGH_THE_RETRIEVE = "dallow-success-of_devices_enough_the.retrieve"
    MANUFACTURERS_INFORMATION_WORLD_TH = "_manufacturers_information.world_th"
    HDOCUMENTS_IMPACT = "hdocuments-impact"


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicIdEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicIdEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
