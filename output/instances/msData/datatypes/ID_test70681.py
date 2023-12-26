from output.models.ms_data.datatypes.datatypes_xsd.datatypes import Data
from output.models.ms_data.datatypes.datatypes_xsd.datatypes import Item


obj = Data(
    any_element=Item(
        any_attributes={
            'SOMITEM_DATATYPE_ID': ' id ',
        }
    )
)
