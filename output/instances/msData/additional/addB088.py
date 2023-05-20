from output.models.ms_data.additional.add_b088_xsd.add_b088 import AnyType
from output.models.ms_data.additional.add_b088_xsd.add_b088 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            target_namespace_imported_xsd_element=AnyElement(
                qname="{http://importedXSD}doc1",
                text="",
                children=[
                    AnyElement(
                        qname="{http://importedXSD}elem1",
                        text="",
                        children=[
                            AnyElement(
                                qname="{http://importedXSD}bbb",
                                text=""
                            ),
                        ]
                    ),
                    AnyElement(
                        qname="{http://importedXSD}elem2",
                        text="",
                        children=[
                            AnyElement(
                                qname="{http://importedXSD}bbb",
                                text=""
                            ),
                        ]
                    ),
                ]
            )
        ),
    ]
)
