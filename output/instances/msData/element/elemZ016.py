from output.models.ms_data.element.elem_z016_xsd.elem_z016 import DataTypes
from output.models.ms_data.element.elem_z016_xsd.elem_z016 import Id
from output.models.ms_data.element.elem_z016_xsd.elem_z016 import Idref
from output.models.ms_data.element.elem_z016_xsd.elem_z016 import Idrefs
from output.models.ms_data.element.elem_z016_xsd.elem_z016 import Root


obj = Root(
    data_types=[
        DataTypes(
            id=[
                Id(
                    value='Address'
                ),
                Id(
                    value='Address'
                ),
            ],
            idref=[
                Idref(
                    value='Address'
                ),
                Idref(
                    value='Address'
                ),
            ],
            idrefs=[
                Idrefs(
                    value=[
                        'Address',
                    ]
                ),
                Idrefs(
                    value=[
                        'Address',
                    ]
                ),
            ]
        ),
    ]
)
