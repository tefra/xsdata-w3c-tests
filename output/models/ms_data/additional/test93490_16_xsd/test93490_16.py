from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://schemas.microsoft.com/office/excel/2003/xml"


@dataclass
class SchemaType:
    """
    :ivar any_element:
    :ivar id:
    :ivar namespace:
    :ivar schema_ref:
    """
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute",
            namespace="http://schemas.microsoft.com/office/excel/2003/xml",
            required=True
        )
    )
    namespace: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Namespace",
            type="Attribute",
            namespace="http://schemas.microsoft.com/office/excel/2003/xml",
            required=True
        )
    )
    schema_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SchemaRef",
            type="Attribute",
            namespace="http://schemas.microsoft.com/office/excel/2003/xml"
        )
    )


class TruefalseType(Enum):
    """
    :cvar FALSE_VALUE:
    :cvar TRUE_VALUE:
    """
    FALSE_VALUE = "false"
    TRUE_VALUE = "true"


@dataclass
class MapInfoType:
    """
    :ivar schema:
    :ivar hide_inactive_list_border:
    :ivar selection_namespaces:
    :ivar hide_single_mapped_cell_border:
    """
    schema: List[SchemaType] = field(
        default_factory=list,
        metadata=dict(
            name="Schema",
            type="Element",
            namespace="http://schemas.microsoft.com/office/excel/2003/xml",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    hide_inactive_list_border: "MapInfoType.HideInactiveListBorder" = field(
        default="false",
        metadata=dict(
            name="HideInactiveListBorder",
            type="Attribute",
            namespace="http://schemas.microsoft.com/office/excel/2003/xml"
        )
    )
    selection_namespaces: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SelectionNamespaces",
            type="Attribute",
            namespace="http://schemas.microsoft.com/office/excel/2003/xml"
        )
    )
    hide_single_mapped_cell_border: TruefalseType = field(
        default="true",
        metadata=dict(
            name="HideSingleMappedCellBorder",
            type="Attribute",
            namespace="http://schemas.microsoft.com/office/excel/2003/xml"
        )
    )

    class HideInactiveListBorder(Enum):
        """
        :cvar FALSE_VALUE:
        :cvar TRUE_VALUE:
        """
        FALSE_VALUE = "false"
        TRUE_VALUE = "true"


@dataclass
class MapInfo(MapInfoType):
    class Meta:
        namespace = "http://schemas.microsoft.com/office/excel/2003/xml"
