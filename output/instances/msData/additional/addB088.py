from output.models.ms_data.additional.add_b088_xsd.add_b088 import AnyType
from output.models.ms_data.additional.add_b088_xsd.add_b088 import Doc
from output.models.ms_data.additional.add_b088_xsd.add_b088_imp import Any1
from output.models.ms_data.additional.add_b088_xsd.add_b088_imp import Doc1


obj = Doc(
    elem=[
        AnyType(
            target_namespace_imported_xsd_element=Doc1(
                elem1=[
                    Any1(
                        local_element_or_bbb_or_ccc=Any1.Bbb(

                        )
                    ),
                ],
                elem2=[
                    Any1(
                        local_element_or_bbb_or_ccc=Any1.Bbb(

                        )
                    ),
                ]
            )
        ),
    ]
)
