from output.models.ms_data.identity_constraint.id_z006_xsd.id_z006 import AType
from output.models.ms_data.identity_constraint.id_z006_xsd.id_z006 import BType
from output.models.ms_data.identity_constraint.id_z006_xsd.id_z006 import BsType
from output.models.ms_data.identity_constraint.id_z006_xsd.id_z006 import CType
from output.models.ms_data.identity_constraint.id_z006_xsd.id_z006 import CsType
from output.models.ms_data.identity_constraint.id_z006_xsd.id_z006 import Root


obj = Root(
    a=[
        AType(
            bs=[
                BsType(
                    b=[
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="c"
                                    )
                                ),
                            ],
                            att_b="a"
                        ),
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="cc"
                                    )
                                ),
                            ],
                            att_b="aa"
                        ),
                    ]
                ),
                BsType(
                    b=[
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="c"
                                    )
                                ),
                            ],
                            att_b="a"
                        ),
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="cc"
                                    )
                                ),
                            ],
                            att_b="aa"
                        ),
                    ]
                ),
            ],
            cs=CsType(
                c=CType(
                    att_c="c"
                )
            ),
            att_a="a"
        ),
        AType(
            bs=[
                BsType(
                    b=[
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="c"
                                    )
                                ),
                            ],
                            att_b="a"
                        ),
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="cc"
                                    )
                                ),
                            ],
                            att_b="aa"
                        ),
                    ]
                ),
                BsType(
                    b=[
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="c"
                                    )
                                ),
                            ],
                            att_b="a"
                        ),
                        BType(
                            cs=[
                                CsType(
                                    c=CType(
                                        att_c="cc"
                                    )
                                ),
                            ],
                            att_b="aa"
                        ),
                    ]
                ),
            ],
            cs=CsType(
                c=CType(
                    att_c="c"
                )
            ),
            att_a="a"
        ),
    ]
)