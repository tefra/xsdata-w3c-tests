from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://schemas.microsoft.com/office/excel/2003/xml"


class MapInfoTypeHideInactiveListBorder(Enum):
    TRUE_VALUE = "true"
    FALSE_VALUE = "false"


@dataclass
class SchemaType:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
            "required": True,
        }
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "Namespace",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
            "required": True,
        }
    )
    schema_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchemaRef",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        }
    )


class TruefalseType(Enum):
    TRUE_VALUE = "true"
    FALSE_VALUE = "false"


@dataclass
class MapInfoType:
    schema: List[SchemaType] = field(
        default_factory=list,
        metadata={
            "name": "Schema",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
            "min_occurs": 1,
        }
    )
    hide_inactive_list_border: MapInfoTypeHideInactiveListBorder = field(
        default=MapInfoTypeHideInactiveListBorder.FALSE_VALUE,
        metadata={
            "name": "HideInactiveListBorder",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        }
    )
    selection_namespaces: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectionNamespaces",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        }
    )
    hide_single_mapped_cell_border: TruefalseType = field(
        default=TruefalseType.TRUE_VALUE,
        metadata={
            "name": "HideSingleMappedCellBorder",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        }
    )


@dataclass
class MapInfo(MapInfoType):
    class Meta:
        namespace = "http://schemas.microsoft.com/office/excel/2003/xml"
