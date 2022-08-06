from output.models.ibm_data.valid.d4_3_15.d4_3_15v14_xsd.d4_3_15v14 import ElementType1
from output.models.ibm_data.valid.d4_3_15.d4_3_15v14_xsd.d4_3_15v14 import ElementType2
from output.models.ibm_data.valid.d4_3_15.d4_3_15v14_xsd.d4_3_15v14 import Root
from output.models.ibm_data.valid.d4_3_15.d4_3_15v14_xsd.d4_3_15v14 import RootType


obj = Root(
    ele1=[
        ElementType1(
            sub_element1=[
                RootType(
                    ele1=[],
                    ele2=[
                        ElementType2(
                            sub_element2=[
                                RootType(
                                    ele1=[
                                        ElementType1(
                                            sub_element1=[]
                                        ),
                                    ],
                                    ele2=[]
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
    ele2=[]
)
