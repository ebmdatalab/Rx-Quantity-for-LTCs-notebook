# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   widgets:
#     application/vnd.jupyter.widget-state+json:
#       state:
#         006c5887e5944579a1a43bd78a3ca194:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Time to collect (min):'
#             layout: IPY_MODEL_96c0f51cf4824b4aa5e6da6543eec87a
#             max: 30
#             style: IPY_MODEL_d0f4aab4810f40d285812f93f2eedd3a
#             value: 10
#         01b9ee8797e842e8b325a8b97e49d0c9:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         06443af9e14e45229c9e69ed069c1a29:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: HBoxModel
#           state:
#             children:
#             - IPY_MODEL_d459732f2bf74a28b0f5e97e35664b42
#             layout: IPY_MODEL_858b01d62fbe4192b24e01f212c56a3f
#         0683704fc53243a7ab5286d366de55f9:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         069a3eb8f4a541beb8cb77c1d2d669c7:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         0803253b9b8e42d6a9b6a9adfc00fef1:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Time per presc (min):'
#             layout: IPY_MODEL_ed3037a3440f4dc2aa5c8058ea537a4d
#             max: 2
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_171ec9359cce47568c6802f52c4f760f
#             value: 0.5
#         089ea883e97043bebae1760673972732:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DropdownModel
#           state:
#             _options_labels:
#             - 00C
#             - 00D
#             - 00J
#             - 00K
#             - 00L
#             - 00M
#             - 00N
#             - 00P
#             - 00Q
#             - 00R
#             - 00T
#             - 00V
#             - 00X
#             - 00Y
#             - 01A
#             - 01C
#             - 01D
#             - 01E
#             - 01F
#             - 01G
#             - 01H
#             - 01J
#             - 01K
#             - 01R
#             - 01T
#             - 01V
#             - 01W
#             - 01X
#             - 01Y
#             - 02A
#             - 02D
#             - 02E
#             - 02F
#             - 02G
#             - 02H
#             - 02M
#             - 02N
#             - 02P
#             - 02Q
#             - 02R
#             - 02T
#             - 02W
#             - 02X
#             - 02Y
#             - 03A
#             - 03D
#             - 03E
#             - 03F
#             - 03H
#             - 03J
#             - 03K
#             - 03L
#             - 03M
#             - 03N
#             - 03Q
#             - 03R
#             - 03T
#             - 03V
#             - 03W
#             - 04C
#             - 04D
#             - 04E
#             - 04F
#             - 04G
#             - 04H
#             - 04K
#             - 04L
#             - 04M
#             - 04N
#             - 04Q
#             - 04V
#             - 04Y
#             - 05A
#             - 05C
#             - 05D
#             - 05F
#             - 05G
#             - 05H
#             - 05J
#             - 05L
#             - 05N
#             - 05Q
#             - 05R
#             - 05T
#             - 05V
#             - 05W
#             - 05X
#             - 05Y
#             - 06A
#             - 06D
#             - 06F
#             - 06H
#             - 06K
#             - 06L
#             - 06M
#             - 06N
#             - 06P
#             - 06Q
#             - 06T
#             - 06V
#             - 06W
#             - 06Y
#             - 07G
#             - 07H
#             - 07J
#             - 07K
#             - 07L
#             - 07M
#             - 07N
#             - 07P
#             - 07Q
#             - 07R
#             - 07T
#             - 07V
#             - 07W
#             - 07X
#             - 07Y
#             - 08A
#             - 08C
#             - 08D
#             - 08E
#             - 08F
#             - 08G
#             - 08H
#             - 08J
#             - 08K
#             - 08L
#             - 08M
#             - 08N
#             - 08P
#             - 08Q
#             - 08R
#             - 08T
#             - 08V
#             - 08W
#             - 08X
#             - 08Y
#             - 09A
#             - 09C
#             - 09D
#             - 09E
#             - 09F
#             - 09G
#             - 09H
#             - 09J
#             - 09L
#             - 09N
#             - 09P
#             - 09W
#             - 09X
#             - 09Y
#             - 10A
#             - 10C
#             - 10D
#             - 10E
#             - 10J
#             - 10K
#             - 10L
#             - 10Q
#             - 10R
#             - 10V
#             - 10X
#             - 11A
#             - 11E
#             - 11J
#             - 11M
#             - 11N
#             - 11X
#             - 12D
#             - 12F
#             - 13T
#             - 14L
#             - 14Y
#             - 15A
#             - 15C
#             - 15D
#             - 15E
#             - 15F
#             - 15M
#             - 15N
#             - 99A
#             - 99C
#             - 99D
#             - 99E
#             - 99F
#             - 99G
#             - 99H
#             - 99J
#             - 99K
#             - 99M
#             - 99N
#             - All
#             description: 'CCG:'
#             index: 123
#             layout: IPY_MODEL_9b60817ee94e4e6f83eb335d663ed87c
#             style: IPY_MODEL_559b4f0f02394607a0dbc68d88697146
#         092e3843ddc04859943ebc8f967aa3ac:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         0a2e020bb83e4c30b6af479d67ae5141:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         0a821b13e7be45aeb2d88c715e589ab2:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion amenable:'
#             layout: IPY_MODEL_73033f6129d74f9bb542d1822f9231bf
#             max: 0.95
#             min: 0.2
#             step: 0.05
#             style: IPY_MODEL_c778db39893a4ffb9b355ca7102b92ab
#             value: 0.9
#         0b30a29446d149bf94e23ace70f600ff:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         0b3a5c3463804bcfa786534b5bd0ba6f:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         0befbab010424a899e7e15a6c8fd0fbf:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         10d8a202f5a245ae9ebe5e0fe6fcddb3:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         11f3af56fffd4aee971f9fc5fb91d976:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion GP:'
#             layout: IPY_MODEL_c5cb833375d74915a76c2391b80b1431
#             max: 0.9
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_4ab2d7da9e89493d84b0df0a36bb8a06
#             value: 0.5
#         1396965b792248b1aa7ecbde34c354bb:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         139eb8ae1ae7441f9535f9fd5a3a2e67:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         14165161302d425c8870b6db055ab571:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         1429337cafa048dd9265f10747086de7:
#           model_module: '@jupyter-widgets/output'
#           model_module_version: 1.0.0
#           model_name: OutputModel
#           state:
#             layout: IPY_MODEL_579a57de9f5649b2b61bf2a75a1fc0a1
#             outputs:
#             - name: stdout
#               output_type: stream
#               text: "Total prescriptions = 16,212,361 \n\nDispensing fees =  \xA3\
#                 6,128,272 \nStaff cost =  \xA32,285,943 \nWasted meds =  \xA31,325,860\
#                 \ \nPatient cost =  \xA311,889,065 \n \nOverall impact: =  \xA315,500,867\n"
#         14b1771f419b4baf8ccae80d68b6d582:
#           model_module: '@jupyter-widgets/output'
#           model_module_version: 1.0.0
#           model_name: OutputModel
#           state:
#             layout: IPY_MODEL_9d814774e3964cf8bac2c62f0106f4a8
#             outputs:
#             - name: stdout
#               output_type: stream
#               text: "Total 28-day prescriptions = 87,207,906 \nPercent 1 month (of\
#                 \ all 1+2+3 month prescriptions) = 66% \nMean price per item = \xA3\
#                 1.04 \n\nDispensing fees =  \xA333M \nStaff cost =  \xA312,296,315\
#                 \ \nWasted meds =  \xA39,284,602 \nPatient cost =  \xA363,952,464\
#                 \ \n \nOverall impact: =  \xA385,533,381\n"
#         16114efd37bc467bac2afbb722fe8e7c:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         16b72d3d83ae4d31842686cf0f48ed91:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         16d596ece4e042ecbbe935b7b5fae13d:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         171ec9359cce47568c6802f52c4f760f:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         1c6abc57904e4a0ba39ce0df435588fa:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: VBoxModel
#           state:
#             children:
#             - IPY_MODEL_28452012b8c248838595f0a49d6a7251
#             - IPY_MODEL_0a821b13e7be45aeb2d88c715e589ab2
#             - IPY_MODEL_d976abf58d8545c5b00a401967581db7
#             - IPY_MODEL_640c71878dec48d599fb65d72aabb5ba
#             - IPY_MODEL_c4c3aa87e3a84629ad13fb279ba8b497
#             - IPY_MODEL_5a560fc034fc44f1bb965862fb7e44dd
#             - IPY_MODEL_9497a65536e8451c99e16967f295ea2a
#             - IPY_MODEL_bebabeeef0a243df90e2dbef670dad45
#             - IPY_MODEL_45d72c50c8474e2fabc4f562f6532e07
#             layout: IPY_MODEL_746c7efbe0eb432b9f5363bd5a9eff55
#         20d4e666cbb94873be18303cb272f769:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         224114ee017e45a69b4f893d1fdeed42:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         23fa1073ffda422ca5a9f9b7780f46d8:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         2683f8ea1d9f49149a7cba9dae2f56f6:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Time per presc (min):'
#             layout: IPY_MODEL_74974dffb09b4b2a938548293895879f
#             max: 2
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_4c405b5eeede48a5aabea1815f7bde12
#             value: 0.5
#         28452012b8c248838595f0a49d6a7251:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Months supply:'
#             layout: IPY_MODEL_224114ee017e45a69b4f893d1fdeed42
#             max: 4
#             min: 1
#             style: IPY_MODEL_d2e642b8e2284e1f8235697b7b9b0773
#             value: 3
#         28c1d445be7344869d093c56ac29dab4:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         28fc4881230541dd82fd29f08146470e:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'e-RD proportion:'
#             layout: IPY_MODEL_23fa1073ffda422ca5a9f9b7780f46d8
#             max: 1
#             step: 0.1
#             style: IPY_MODEL_e7249d10b563404aaca5c3660da1f008
#             value: 0.5
#         297b2c51ee8b442387eebcc79e8f04c6:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: "Cost of public time (\xA3):"
#             layout: IPY_MODEL_b42144b851b84647b141d9f502d2113a
#             max: 15
#             min: 5
#             style: IPY_MODEL_edf588567a9f45fd88681722ea897b37
#             value: 11
#         29806774732543f4996711bc8b7f9a13:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Time per presc (min):'
#             layout: IPY_MODEL_6772f235c0f44d92828bd381da24b86f
#             max: 2
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_8e196ac9de77442fa9a70c133b76c8f1
#             value: 0.5
#         2d9e695740d1441d84ccd01594c2293a:
#           model_module: '@jupyter-widgets/output'
#           model_module_version: 1.0.0
#           model_name: OutputModel
#           state:
#             layout: IPY_MODEL_3082466ff97642d984fe74ba12b4e163
#             outputs:
#             - name: stdout
#               output_type: stream
#               text: "Total 28-day prescriptions = 87,207,906 \nPercent 1 month (of\
#                 \ all 1+2+3 month prescriptions) = 66% \nMean price per item = \xA3\
#                 1.04 \n\nDispensing fees =  \xA333.0M \nStaff cost =  \xA312.3M \n\
#                 Wasted meds =  \xA39.3M \nPatient cost =  \xA364.0M \n \nOverall impact:\
#                 \ =  \xA385.5M\n"
#         2dd6eeeda54445cb8d8e9b226eeb10df:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         2e063288a1cc4bbba4b19cb901a87b94:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         2e273b1d03ce4e3887c9f8a802e0eef5:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         2f22688f4e39430da900ed55b2c13ed3:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         2f9888506ccf480caa696c826136cdcf:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         3082466ff97642d984fe74ba12b4e163:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         329d2ecdf5eb4f6eb3ccd178b53fee28:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Time to collect (min):'
#             layout: IPY_MODEL_44c2c24a6d1e4c11a41390e64fd1ab9b
#             max: 30
#             style: IPY_MODEL_8b3fcb5a002843478c569884b0596f33
#             value: 10
#         331caf21b66642519fcf887a3deee8aa:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: HBoxModel
#           state:
#             children:
#             - IPY_MODEL_5abffcaf863b4cefaff7096ed2dde3be
#             layout: IPY_MODEL_e2ad49ec6fbe417cb964956eb0b36711
#         347119322d9b41b5a2fccee2bc6ad20c:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         34d32f43481b4331811f4618dbdf3f8f:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DropdownModel
#           state:
#             _options_labels:
#             - 00C
#             - 00D
#             - 00J
#             - 00K
#             - 00L
#             - 00M
#             - 00N
#             - 00P
#             - 00Q
#             - 00R
#             - 00T
#             - 00V
#             - 00X
#             - 00Y
#             - 01A
#             - 01C
#             - 01D
#             - 01E
#             - 01F
#             - 01G
#             - 01H
#             - 01J
#             - 01K
#             - 01R
#             - 01T
#             - 01V
#             - 01W
#             - 01X
#             - 01Y
#             - 02A
#             - 02D
#             - 02E
#             - 02F
#             - 02G
#             - 02H
#             - 02M
#             - 02N
#             - 02P
#             - 02Q
#             - 02R
#             - 02T
#             - 02W
#             - 02X
#             - 02Y
#             - 03A
#             - 03D
#             - 03E
#             - 03F
#             - 03H
#             - 03J
#             - 03K
#             - 03L
#             - 03M
#             - 03N
#             - 03Q
#             - 03R
#             - 03T
#             - 03V
#             - 03W
#             - 04C
#             - 04D
#             - 04E
#             - 04F
#             - 04G
#             - 04H
#             - 04K
#             - 04L
#             - 04M
#             - 04N
#             - 04Q
#             - 04V
#             - 04Y
#             - 05A
#             - 05C
#             - 05D
#             - 05F
#             - 05G
#             - 05H
#             - 05J
#             - 05L
#             - 05N
#             - 05Q
#             - 05R
#             - 05T
#             - 05V
#             - 05W
#             - 05X
#             - 05Y
#             - 06A
#             - 06D
#             - 06F
#             - 06H
#             - 06K
#             - 06L
#             - 06M
#             - 06N
#             - 06P
#             - 06Q
#             - 06T
#             - 06V
#             - 06W
#             - 06Y
#             - 07G
#             - 07H
#             - 07J
#             - 07K
#             - 07L
#             - 07M
#             - 07N
#             - 07P
#             - 07Q
#             - 07R
#             - 07T
#             - 07V
#             - 07W
#             - 07X
#             - 07Y
#             - 08A
#             - 08C
#             - 08D
#             - 08E
#             - 08F
#             - 08G
#             - 08H
#             - 08J
#             - 08K
#             - 08L
#             - 08M
#             - 08N
#             - 08P
#             - 08Q
#             - 08R
#             - 08T
#             - 08V
#             - 08W
#             - 08X
#             - 08Y
#             - 09A
#             - 09C
#             - 09D
#             - 09E
#             - 09F
#             - 09G
#             - 09H
#             - 09J
#             - 09L
#             - 09N
#             - 09P
#             - 09W
#             - 09X
#             - 09Y
#             - 10A
#             - 10C
#             - 10D
#             - 10E
#             - 10J
#             - 10K
#             - 10L
#             - 10Q
#             - 10R
#             - 10V
#             - 10X
#             - 11A
#             - 11E
#             - 11J
#             - 11M
#             - 11N
#             - 11X
#             - 12D
#             - 12F
#             - 13T
#             - 14L
#             - 14Y
#             - 15A
#             - 15C
#             - 15D
#             - 15E
#             - 15F
#             - 15M
#             - 15N
#             - 99A
#             - 99C
#             - 99D
#             - 99E
#             - 99F
#             - 99G
#             - 99H
#             - 99J
#             - 99K
#             - 99M
#             - 99N
#             - All
#             description: 'CCG:'
#             index: 191
#             layout: IPY_MODEL_1396965b792248b1aa7ecbde34c354bb
#             style: IPY_MODEL_b7724de2e24d439cbc90f013f9c40a4d
#         37eaf857e5e4432cb5b982e88e4253fc:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion amenable:'
#             layout: IPY_MODEL_91f29a93aa524b3fb505c0cd469f191d
#             max: 0.95
#             min: 0.2
#             step: 0.05
#             style: IPY_MODEL_3a410f63c91445c0ac073876a0947c83
#             value: 0.9
#         3914c16768f3458291e0ce9222df3d31:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'e-RD proportion:'
#             layout: IPY_MODEL_5bf771dc45da4d2d91bc9bfca0ff6ee9
#             max: 1
#             step: 0.1
#             style: IPY_MODEL_cf98378f0984482da80f4bb1b8472034
#             value: 0.5
#         3a410f63c91445c0ac073876a0947c83:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         3a65e0f3e8614889a58dacba573d81d8:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Months supply:'
#             layout: IPY_MODEL_ffe4ec48f4b24b84a3636b2e5b5bfe1f
#             max: 4
#             min: 1
#             style: IPY_MODEL_d1f2afa89ddb41fbbc8a0e63113a099d
#             value: 3
#         3b9d969d72a84e018c0d765206c4a5c0:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion GP:'
#             layout: IPY_MODEL_d20a3b4c8ca04d3f9a615e7a3b6b3170
#             max: 0.9
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_2dd6eeeda54445cb8d8e9b226eeb10df
#             value: 0.5
#         3cf090004fce4c4aa2ea83f8ce0f5c34:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: "Cost of public time (\xA3):"
#             layout: IPY_MODEL_9d8ff1050ab04be6bd5c8fe016a3faa3
#             max: 15
#             min: 5
#             style: IPY_MODEL_139eb8ae1ae7441f9535f9fd5a3a2e67
#             value: 11
#         4142de5e35e148b181dbcec672edbcfe:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Months supply:'
#             layout: IPY_MODEL_cac5563991004ce8af0cd5f830975127
#             max: 4
#             min: 1
#             style: IPY_MODEL_bdd879dd72374a74b8d3c0b61414e8eb
#             value: 3
#         44c2c24a6d1e4c11a41390e64fd1ab9b:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         458a443ba93d42aba1d07b1300f1db45:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'e-RD proportion:'
#             layout: IPY_MODEL_a1a36baefc62414586274f6e44c292ab
#             max: 1
#             step: 0.1
#             style: IPY_MODEL_9687a3a01510467db0546520a7d30048
#             value: 0.5
#         45d72c50c8474e2fabc4f562f6532e07:
#           model_module: '@jupyter-widgets/output'
#           model_module_version: 1.0.0
#           model_name: OutputModel
#           state:
#             layout: IPY_MODEL_16b72d3d83ae4d31842686cf0f48ed91
#             outputs:
#             - name: stdout
#               output_type: stream
#               text: "Total 28-day prescriptions = f{prescriptions:,.0f} \nPercent\
#                 \ 1 month (of all 1+2+3 month prescriptions) = f{percent_28d:,.0f}%\
#                 \ \nMean price per item = \xA3 f{priceperitem:,.2f} \n\nDispensing\
#                 \ fees =  \xA3 f{dispensing_fees:,.0f} \nStaff cost =  \xA3 f{staff_cost:,.0f}\
#                 \ \nWasted meds =  \xA3 f{waste:,.0f} \nPatient cost =  \xA3 f{patient_cost:,.0f}\
#                 \ \n \nOverall impact: =  \xA3 f{staff_cost + waste + patient_cost:,.0f}\n"
#         464f0a80bfa04a26b66e95460d63f351:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         470cd9fb51e343939fe979b35d46cebe:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         4889df4b39f6412195687b684ad9ecae:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Time per presc (min):'
#             layout: IPY_MODEL_bd0f1b183e9941b5a0c4d3926035a71d
#             max: 2
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_88bc2874300647e79fab8d2d6145b1a4
#             value: 0.5
#         499bd089984c4a1ea53badbfc14c5299:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         4ab2d7da9e89493d84b0df0a36bb8a06:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         4ad580f5a2e9454ebfe63d927e736912:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         4c405b5eeede48a5aabea1815f7bde12:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         4c8d3b247a1343db99352c67f6ab5b37:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion GP:'
#             layout: IPY_MODEL_20d4e666cbb94873be18303cb272f769
#             max: 0.9
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_e9e749d1df6745ee80903cdebe20f0de
#             value: 0.5
#         4e9b90b76df5441495bd1451a5c1135a:
#           model_module: '@jupyter-widgets/output'
#           model_module_version: 1.0.0
#           model_name: OutputModel
#           state:
#             layout: IPY_MODEL_b2932ed526f44580b4079c50d84b2457
#             outputs:
#             - name: stdout
#               output_type: stream
#               text: "Total 28-day prescriptions = 87,207,906 \nPercent 1 month (of\
#                 \ all 1+2+3 month prescriptions) = 66% \nMean price per item = \xA3\
#                 1.04 \n\nDispensing fees =  \xA398,893,765 \nStaff cost =  \xA330,740,787\
#                 \ \nWasted meds =  \xA33,296,194 \nPatient cost =  \xA3159,881,161\
#                 \ \n \nOverall impact: =  \xA3193,918,142\n"
#         503549a68311467b93d052036223d54b:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DescriptionStyleModel
#           state:
#             description_width: ''
#         559b4f0f02394607a0dbc68d88697146:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DescriptionStyleModel
#           state:
#             description_width: ''
#         55e37c60ccc14e8a9fd02081b09c977c:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         55ecd4c4977c4e6ba54e16c2d3979e9b:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DescriptionStyleModel
#           state:
#             description_width: ''
#         572c8b3d3c634fe18bde6859317001be:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         579a57de9f5649b2b61bf2a75a1fc0a1:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         595e82f9893546b9a82ac6133b412830:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         59f3dbb797e14226809c09d1d52b8cf6:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         5a560fc034fc44f1bb965862fb7e44dd:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: "Cost of public time (\xA3):"
#             layout: IPY_MODEL_d44baa9220f8481b8b868196d5771272
#             max: 15
#             min: 5
#             style: IPY_MODEL_ed7fe31eb23148dfa0237bb8668710bd
#             value: 11
#         5abffcaf863b4cefaff7096ed2dde3be:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: VBoxModel
#           state:
#             children:
#             - IPY_MODEL_3a65e0f3e8614889a58dacba573d81d8
#             - IPY_MODEL_88ed46792d8f45b5ae9ef06f7f4a60ed
#             - IPY_MODEL_b565d576e80443f883b804c8f6737d11
#             - IPY_MODEL_b4a22712a30d45088f98765774556c1b
#             - IPY_MODEL_b829c5fe8afe4af68b85b1c1cd35cd37
#             - IPY_MODEL_bcdac408f3664f8ab3134abe1c2f5dea
#             - IPY_MODEL_006c5887e5944579a1a43bd78a3ca194
#             - IPY_MODEL_60690a380bb74afdb33e1f4a8e706984
#             - IPY_MODEL_14b1771f419b4baf8ccae80d68b6d582
#             layout: IPY_MODEL_470cd9fb51e343939fe979b35d46cebe
#         5b0c7a98207b4a23a0d4de789b5a4b45:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         5baf95409f694e3ba2a20bb0490b762a:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         5bf771dc45da4d2d91bc9bfca0ff6ee9:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         5dba1f1239eb456aa03516f614047434:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         60690a380bb74afdb33e1f4a8e706984:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DropdownModel
#           state:
#             _options_labels:
#             - 00C
#             - 00D
#             - 00J
#             - 00K
#             - 00L
#             - 00M
#             - 00N
#             - 00P
#             - 00Q
#             - 00R
#             - 00T
#             - 00V
#             - 00X
#             - 00Y
#             - 01A
#             - 01C
#             - 01D
#             - 01E
#             - 01F
#             - 01G
#             - 01H
#             - 01J
#             - 01K
#             - 01R
#             - 01T
#             - 01V
#             - 01W
#             - 01X
#             - 01Y
#             - 02A
#             - 02D
#             - 02E
#             - 02F
#             - 02G
#             - 02H
#             - 02M
#             - 02N
#             - 02P
#             - 02Q
#             - 02R
#             - 02T
#             - 02W
#             - 02X
#             - 02Y
#             - 03A
#             - 03D
#             - 03E
#             - 03F
#             - 03H
#             - 03J
#             - 03K
#             - 03L
#             - 03M
#             - 03N
#             - 03Q
#             - 03R
#             - 03T
#             - 03V
#             - 03W
#             - 04C
#             - 04D
#             - 04E
#             - 04F
#             - 04G
#             - 04H
#             - 04K
#             - 04L
#             - 04M
#             - 04N
#             - 04Q
#             - 04V
#             - 04Y
#             - 05A
#             - 05C
#             - 05D
#             - 05F
#             - 05G
#             - 05H
#             - 05J
#             - 05L
#             - 05N
#             - 05Q
#             - 05R
#             - 05T
#             - 05V
#             - 05W
#             - 05X
#             - 05Y
#             - 06A
#             - 06D
#             - 06F
#             - 06H
#             - 06K
#             - 06L
#             - 06M
#             - 06N
#             - 06P
#             - 06Q
#             - 06T
#             - 06V
#             - 06W
#             - 06Y
#             - 07G
#             - 07H
#             - 07J
#             - 07K
#             - 07L
#             - 07M
#             - 07N
#             - 07P
#             - 07Q
#             - 07R
#             - 07T
#             - 07V
#             - 07W
#             - 07X
#             - 07Y
#             - 08A
#             - 08C
#             - 08D
#             - 08E
#             - 08F
#             - 08G
#             - 08H
#             - 08J
#             - 08K
#             - 08L
#             - 08M
#             - 08N
#             - 08P
#             - 08Q
#             - 08R
#             - 08T
#             - 08V
#             - 08W
#             - 08X
#             - 08Y
#             - 09A
#             - 09C
#             - 09D
#             - 09E
#             - 09F
#             - 09G
#             - 09H
#             - 09J
#             - 09L
#             - 09N
#             - 09P
#             - 09W
#             - 09X
#             - 09Y
#             - 10A
#             - 10C
#             - 10D
#             - 10E
#             - 10J
#             - 10K
#             - 10L
#             - 10Q
#             - 10R
#             - 10V
#             - 10X
#             - 11A
#             - 11E
#             - 11J
#             - 11M
#             - 11N
#             - 11X
#             - 12D
#             - 12F
#             - 13T
#             - 14L
#             - 14Y
#             - 15A
#             - 15C
#             - 15D
#             - 15E
#             - 15F
#             - 15M
#             - 15N
#             - 99A
#             - 99C
#             - 99D
#             - 99E
#             - 99F
#             - 99G
#             - 99H
#             - 99J
#             - 99K
#             - 99M
#             - 99N
#             - All
#             description: 'CCG:'
#             index: 191
#             layout: IPY_MODEL_ae57c599de0447efb548a9baff04202a
#             style: IPY_MODEL_55ecd4c4977c4e6ba54e16c2d3979e9b
#         6350c1e4353d40029903d413fb467ee3:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion GP:'
#             layout: IPY_MODEL_d6410dcc4bba45478f48f2d58e997c27
#             max: 0.9
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_f44f36c4df1744d2a539dde910e3ec54
#             value: 0.5
#         63e7ac14f3d64de2a4578ba6089cf44e:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: HBoxModel
#           state:
#             children:
#             - IPY_MODEL_f04a2ccd6d714d68a9a909b047b525ee
#             layout: IPY_MODEL_e419a883ef8d402cbcebf78e7143262a
#         640c71878dec48d599fb65d72aabb5ba:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Time per presc (min):'
#             layout: IPY_MODEL_f181796b669c40ee98a6369a6ba96a91
#             max: 2
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_dc89b321058d46b0b20924a1e4d81e45
#             value: 0.5
#         640e730f50384bdd8f7a3788678e3885:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion amenable:'
#             layout: IPY_MODEL_667db8b0f0a94ba5a07678238806c0fa
#             max: 0.95
#             min: 0.2
#             step: 0.05
#             style: IPY_MODEL_499bd089984c4a1ea53badbfc14c5299
#             value: 0.9
#         65248358e48d4e06a75c3a6b24f91719:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         6558d8165a7e495484486120ca2364d5:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: HBoxModel
#           state:
#             children:
#             - IPY_MODEL_f516d2f394f24d84a9978f76bc1e9876
#             layout: IPY_MODEL_d30cf61de06142b9ab7b613bd35b7526
#         667db8b0f0a94ba5a07678238806c0fa:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         6772f235c0f44d92828bd381da24b86f:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         683b92fb78ef478887dddb28a109207a:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion GP:'
#             layout: IPY_MODEL_28c1d445be7344869d093c56ac29dab4
#             max: 0.9
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_cd3851f880b0492f8a8d80e230bff1a8
#             value: 0.5
#         688a3cd17a244186aae96cf3d4925079:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Time to collect (min):'
#             layout: IPY_MODEL_16114efd37bc467bac2afbb722fe8e7c
#             max: 30
#             style: IPY_MODEL_b01aad5f51a746558f7c4a79676b4ae8
#             value: 10
#         6af911478693467a876bff97b1957ad3:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Time to collect (min):'
#             layout: IPY_MODEL_ddc1b4baaa8140f5b7a1e397c889246a
#             max: 30
#             style: IPY_MODEL_0b3a5c3463804bcfa786534b5bd0ba6f
#             value: 10
#         6ccc9faae2694450ba2e2e3dc1c8ce8a:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         703a6c9c27fb42568bb84d63ff961243:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'e-RD proportion:'
#             layout: IPY_MODEL_65248358e48d4e06a75c3a6b24f91719
#             max: 1
#             step: 0.1
#             style: IPY_MODEL_e08eb505c19d4c249ba1189bed48d72d
#             value: 0.5
#         7274b91a02114e00b72304ca3e29e644:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: VBoxModel
#           state:
#             children:
#             - IPY_MODEL_ace96a7a9a074b23b127cde02a268a99
#             - IPY_MODEL_640e730f50384bdd8f7a3788678e3885
#             - IPY_MODEL_11f3af56fffd4aee971f9fc5fb91d976
#             - IPY_MODEL_4889df4b39f6412195687b684ad9ecae
#             - IPY_MODEL_3914c16768f3458291e0ce9222df3d31
#             - IPY_MODEL_d2687c59190a46d3a558d97ae46a31e7
#             - IPY_MODEL_329d2ecdf5eb4f6eb3ccd178b53fee28
#             - IPY_MODEL_b00fb9647ce84755967290267595a340
#             - IPY_MODEL_4e9b90b76df5441495bd1451a5c1135a
#             layout: IPY_MODEL_dfc0b8d399ac4b698a83339c19c4b5cb
#         7294dd5c6837451b909c716f03eeddd4:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         73033f6129d74f9bb542d1822f9231bf:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         739ac11a69124490bc5196c9bd139192:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         7413d0962d6645dfac1a95a36fb34fb4:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: HBoxModel
#           state:
#             children:
#             - IPY_MODEL_7274b91a02114e00b72304ca3e29e644
#             layout: IPY_MODEL_be621bec6ecd4a2d9899cc49cc89dd8c
#         746c7efbe0eb432b9f5363bd5a9eff55:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         74974dffb09b4b2a938548293895879f:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         74bf8356b19e456eb0cf2041101bc4a8:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: "Cost of public time (\xA3):"
#             layout: IPY_MODEL_82f0c68cdf8442f2a0d1444ce827af78
#             max: 15
#             min: 5
#             style: IPY_MODEL_d7ebc0eee4b24899b939cf866f2b37ad
#             value: 11
#         752fd3903ddb4caca3e917a8a4e53ccc:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         753a3b0de3ab476e9a63ede9d260fb2b:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         784c04cab34549de921d5271b55f98f5:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         7c39eb959d924c659f9fc29bd9672da9:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DropdownModel
#           state:
#             _options_labels:
#             - 00C
#             - 00D
#             - 00J
#             - 00K
#             - 00L
#             - 00M
#             - 00N
#             - 00P
#             - 00Q
#             - 00R
#             - 00T
#             - 00V
#             - 00X
#             - 00Y
#             - 01A
#             - 01C
#             - 01D
#             - 01E
#             - 01F
#             - 01G
#             - 01H
#             - 01J
#             - 01K
#             - 01R
#             - 01T
#             - 01V
#             - 01W
#             - 01X
#             - 01Y
#             - 02A
#             - 02D
#             - 02E
#             - 02F
#             - 02G
#             - 02H
#             - 02M
#             - 02N
#             - 02P
#             - 02Q
#             - 02R
#             - 02T
#             - 02W
#             - 02X
#             - 02Y
#             - 03A
#             - 03D
#             - 03E
#             - 03F
#             - 03H
#             - 03J
#             - 03K
#             - 03L
#             - 03M
#             - 03N
#             - 03Q
#             - 03R
#             - 03T
#             - 03V
#             - 03W
#             - 04C
#             - 04D
#             - 04E
#             - 04F
#             - 04G
#             - 04H
#             - 04K
#             - 04L
#             - 04M
#             - 04N
#             - 04Q
#             - 04V
#             - 04Y
#             - 05A
#             - 05C
#             - 05D
#             - 05F
#             - 05G
#             - 05H
#             - 05J
#             - 05L
#             - 05N
#             - 05Q
#             - 05R
#             - 05T
#             - 05V
#             - 05W
#             - 05X
#             - 05Y
#             - 06A
#             - 06D
#             - 06F
#             - 06H
#             - 06K
#             - 06L
#             - 06M
#             - 06N
#             - 06P
#             - 06Q
#             - 06T
#             - 06V
#             - 06W
#             - 06Y
#             - 07G
#             - 07H
#             - 07J
#             - 07K
#             - 07L
#             - 07M
#             - 07N
#             - 07P
#             - 07Q
#             - 07R
#             - 07T
#             - 07V
#             - 07W
#             - 07X
#             - 07Y
#             - 08A
#             - 08C
#             - 08D
#             - 08E
#             - 08F
#             - 08G
#             - 08H
#             - 08J
#             - 08K
#             - 08L
#             - 08M
#             - 08N
#             - 08P
#             - 08Q
#             - 08R
#             - 08T
#             - 08V
#             - 08W
#             - 08X
#             - 08Y
#             - 09A
#             - 09C
#             - 09D
#             - 09E
#             - 09F
#             - 09G
#             - 09H
#             - 09J
#             - 09L
#             - 09N
#             - 09P
#             - 09W
#             - 09X
#             - 09Y
#             - 10A
#             - 10C
#             - 10D
#             - 10E
#             - 10J
#             - 10K
#             - 10L
#             - 10Q
#             - 10R
#             - 10V
#             - 10X
#             - 11A
#             - 11E
#             - 11J
#             - 11M
#             - 11N
#             - 11X
#             - 12D
#             - 12F
#             - 13T
#             - 14L
#             - 14Y
#             - 15A
#             - 15C
#             - 15D
#             - 15E
#             - 15F
#             - 15M
#             - 15N
#             - 99A
#             - 99C
#             - 99D
#             - 99E
#             - 99F
#             - 99G
#             - 99H
#             - 99J
#             - 99K
#             - 99M
#             - 99N
#             - All
#             description: 'CCG:'
#             index: 191
#             layout: IPY_MODEL_2f9888506ccf480caa696c826136cdcf
#             style: IPY_MODEL_d11b704cc6d3474b803db2d0c37c6f11
#         7d79ea1967e64f13a943a3d215d8b6e1:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Months supply:'
#             layout: IPY_MODEL_8ed97c9f2c8e4b45a8e947d455c74a35
#             max: 4
#             min: 2
#             style: IPY_MODEL_0b30a29446d149bf94e23ace70f600ff
#             value: 3
#         804aa9506e0a4fa3b184d7fd8fb3caed:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         821e987d67cd4291b19a567ac35257a6:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         82f0c68cdf8442f2a0d1444ce827af78:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         858b01d62fbe4192b24e01f212c56a3f:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         88bc2874300647e79fab8d2d6145b1a4:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         88ed46792d8f45b5ae9ef06f7f4a60ed:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion amenable:'
#             layout: IPY_MODEL_753a3b0de3ab476e9a63ede9d260fb2b
#             max: 0.95
#             min: 0.2
#             step: 0.05
#             style: IPY_MODEL_804aa9506e0a4fa3b184d7fd8fb3caed
#             value: 0.9
#         8b3fcb5a002843478c569884b0596f33:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         8e196ac9de77442fa9a70c133b76c8f1:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         8ed97c9f2c8e4b45a8e947d455c74a35:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         91f29a93aa524b3fb505c0cd469f191d:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         92d653cda86a4cbe9a12bfe774eee114:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion amenable:'
#             layout: IPY_MODEL_ca6ee7c99c8e4499a9cc7aaaf726ba5f
#             max: 0.95
#             min: 0.2
#             step: 0.05
#             style: IPY_MODEL_a699ab985b2b40a5aaed2c696dceded7
#             value: 0.9
#         9497a65536e8451c99e16967f295ea2a:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Time to collect (min):'
#             layout: IPY_MODEL_069a3eb8f4a541beb8cb77c1d2d669c7
#             max: 30
#             style: IPY_MODEL_2f22688f4e39430da900ed55b2c13ed3
#             value: 10
#         9687a3a01510467db0546520a7d30048:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         96c0f51cf4824b4aa5e6da6543eec87a:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         9ad146fea9cc40ed99bcccd58bcc556d:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         9b60817ee94e4e6f83eb335d663ed87c:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         9d814774e3964cf8bac2c62f0106f4a8:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         9d8ff1050ab04be6bd5c8fe016a3faa3:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         a1a36baefc62414586274f6e44c292ab:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         a1aad0cd303742aebf3cbd31f481affd:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         a699ab985b2b40a5aaed2c696dceded7:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         aad3ec2643b4457baaa063546b3b3df1:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         ac6b620e318d43cdacf1922aa0d1af2e:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         ace96a7a9a074b23b127cde02a268a99:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Months supply:'
#             layout: IPY_MODEL_10d8a202f5a245ae9ebe5e0fe6fcddb3
#             max: 4
#             min: 1
#             style: IPY_MODEL_2e273b1d03ce4e3887c9f8a802e0eef5
#             value: 1
#         ae57c599de0447efb548a9baff04202a:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         ae7650b2b1d44f93a6645cbf7bf8d7ec:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         b00fb9647ce84755967290267595a340:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DropdownModel
#           state:
#             _options_labels:
#             - 00C
#             - 00D
#             - 00J
#             - 00K
#             - 00L
#             - 00M
#             - 00N
#             - 00P
#             - 00Q
#             - 00R
#             - 00T
#             - 00V
#             - 00X
#             - 00Y
#             - 01A
#             - 01C
#             - 01D
#             - 01E
#             - 01F
#             - 01G
#             - 01H
#             - 01J
#             - 01K
#             - 01R
#             - 01T
#             - 01V
#             - 01W
#             - 01X
#             - 01Y
#             - 02A
#             - 02D
#             - 02E
#             - 02F
#             - 02G
#             - 02H
#             - 02M
#             - 02N
#             - 02P
#             - 02Q
#             - 02R
#             - 02T
#             - 02W
#             - 02X
#             - 02Y
#             - 03A
#             - 03D
#             - 03E
#             - 03F
#             - 03H
#             - 03J
#             - 03K
#             - 03L
#             - 03M
#             - 03N
#             - 03Q
#             - 03R
#             - 03T
#             - 03V
#             - 03W
#             - 04C
#             - 04D
#             - 04E
#             - 04F
#             - 04G
#             - 04H
#             - 04K
#             - 04L
#             - 04M
#             - 04N
#             - 04Q
#             - 04V
#             - 04Y
#             - 05A
#             - 05C
#             - 05D
#             - 05F
#             - 05G
#             - 05H
#             - 05J
#             - 05L
#             - 05N
#             - 05Q
#             - 05R
#             - 05T
#             - 05V
#             - 05W
#             - 05X
#             - 05Y
#             - 06A
#             - 06D
#             - 06F
#             - 06H
#             - 06K
#             - 06L
#             - 06M
#             - 06N
#             - 06P
#             - 06Q
#             - 06T
#             - 06V
#             - 06W
#             - 06Y
#             - 07G
#             - 07H
#             - 07J
#             - 07K
#             - 07L
#             - 07M
#             - 07N
#             - 07P
#             - 07Q
#             - 07R
#             - 07T
#             - 07V
#             - 07W
#             - 07X
#             - 07Y
#             - 08A
#             - 08C
#             - 08D
#             - 08E
#             - 08F
#             - 08G
#             - 08H
#             - 08J
#             - 08K
#             - 08L
#             - 08M
#             - 08N
#             - 08P
#             - 08Q
#             - 08R
#             - 08T
#             - 08V
#             - 08W
#             - 08X
#             - 08Y
#             - 09A
#             - 09C
#             - 09D
#             - 09E
#             - 09F
#             - 09G
#             - 09H
#             - 09J
#             - 09L
#             - 09N
#             - 09P
#             - 09W
#             - 09X
#             - 09Y
#             - 10A
#             - 10C
#             - 10D
#             - 10E
#             - 10J
#             - 10K
#             - 10L
#             - 10Q
#             - 10R
#             - 10V
#             - 10X
#             - 11A
#             - 11E
#             - 11J
#             - 11M
#             - 11N
#             - 11X
#             - 12D
#             - 12F
#             - 13T
#             - 14L
#             - 14Y
#             - 15A
#             - 15C
#             - 15D
#             - 15E
#             - 15F
#             - 15M
#             - 15N
#             - 99A
#             - 99C
#             - 99D
#             - 99E
#             - 99F
#             - 99G
#             - 99H
#             - 99J
#             - 99K
#             - 99M
#             - 99N
#             - All
#             description: 'CCG:'
#             index: 191
#             layout: IPY_MODEL_f0eca3b0919647989771697393c22627
#             style: IPY_MODEL_503549a68311467b93d052036223d54b
#         b01aad5f51a746558f7c4a79676b4ae8:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         b24ba66d65094aa1b4c0cc78bfca7d91:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         b2932ed526f44580b4079c50d84b2457:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         b42144b851b84647b141d9f502d2113a:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         b4a22712a30d45088f98765774556c1b:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Time per presc (min):'
#             layout: IPY_MODEL_16d596ece4e042ecbbe935b7b5fae13d
#             max: 2
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_59f3dbb797e14226809c09d1d52b8cf6
#             value: 0.5
#         b565d576e80443f883b804c8f6737d11:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion GP:'
#             layout: IPY_MODEL_0a2e020bb83e4c30b6af479d67ae5141
#             max: 0.9
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_c17b326e780943d3af6fb3429b6a05bd
#             value: 0.5
#         b74c2848dfe14b269cdf26938fc7dac4:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Time to collect (min):'
#             layout: IPY_MODEL_752fd3903ddb4caca3e917a8a4e53ccc
#             max: 30
#             style: IPY_MODEL_da5732005e2e43f0a7f971440e18eb34
#             value: 10
#         b7724de2e24d439cbc90f013f9c40a4d:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DescriptionStyleModel
#           state:
#             description_width: ''
#         b829c5fe8afe4af68b85b1c1cd35cd37:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'e-RD proportion:'
#             layout: IPY_MODEL_7294dd5c6837451b909c716f03eeddd4
#             max: 1
#             step: 0.1
#             style: IPY_MODEL_ddd57415fc0c40c3bb2033265bfbc6bb
#             value: 0.5
#         bb61b7ec786148d7bd87e2b17e941725:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: "Price per item (\xA3):"
#             layout: IPY_MODEL_2e063288a1cc4bbba4b19cb901a87b94
#             max: 2
#             min: 0.5
#             step: 0.1
#             style: IPY_MODEL_ded7eef2fefb44a9901fcdcf007353e6
#             value: 0.8
#         bc48a8092e1846a5b8757098a72b9252:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Time per presc (min):'
#             layout: IPY_MODEL_f308b6dee9e142248714dd410e8ee40c
#             max: 2
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_5dba1f1239eb456aa03516f614047434
#             value: 0.5
#         bc73ad9645374c1eb046ea3346bce87a:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         bcdac408f3664f8ab3134abe1c2f5dea:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: "Cost of public time (\xA3):"
#             layout: IPY_MODEL_55e37c60ccc14e8a9fd02081b09c977c
#             max: 15
#             min: 5
#             style: IPY_MODEL_092e3843ddc04859943ebc8f967aa3ac
#             value: 11
#         bd0f1b183e9941b5a0c4d3926035a71d:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         bd6be7a84a5d44ffbbdf944d4c6a7f95:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Months supply:'
#             layout: IPY_MODEL_739ac11a69124490bc5196c9bd139192
#             max: 4
#             min: 1
#             style: IPY_MODEL_f09d6872f78a45598cc61b40b790a1e8
#             value: 1
#         bdd879dd72374a74b8d3c0b61414e8eb:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         be621bec6ecd4a2d9899cc49cc89dd8c:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         bea52f0756994415988752fffecdf4b2:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         bebabeeef0a243df90e2dbef670dad45:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DropdownModel
#           state:
#             _options_labels:
#             - 00C
#             - 00D
#             - 00J
#             - 00K
#             - 00L
#             - 00M
#             - 00N
#             - 00P
#             - 00Q
#             - 00R
#             - 00T
#             - 00V
#             - 00X
#             - 00Y
#             - 01A
#             - 01C
#             - 01D
#             - 01E
#             - 01F
#             - 01G
#             - 01H
#             - 01J
#             - 01K
#             - 01R
#             - 01T
#             - 01V
#             - 01W
#             - 01X
#             - 01Y
#             - 02A
#             - 02D
#             - 02E
#             - 02F
#             - 02G
#             - 02H
#             - 02M
#             - 02N
#             - 02P
#             - 02Q
#             - 02R
#             - 02T
#             - 02W
#             - 02X
#             - 02Y
#             - 03A
#             - 03D
#             - 03E
#             - 03F
#             - 03H
#             - 03J
#             - 03K
#             - 03L
#             - 03M
#             - 03N
#             - 03Q
#             - 03R
#             - 03T
#             - 03V
#             - 03W
#             - 04C
#             - 04D
#             - 04E
#             - 04F
#             - 04G
#             - 04H
#             - 04K
#             - 04L
#             - 04M
#             - 04N
#             - 04Q
#             - 04V
#             - 04Y
#             - 05A
#             - 05C
#             - 05D
#             - 05F
#             - 05G
#             - 05H
#             - 05J
#             - 05L
#             - 05N
#             - 05Q
#             - 05R
#             - 05T
#             - 05V
#             - 05W
#             - 05X
#             - 05Y
#             - 06A
#             - 06D
#             - 06F
#             - 06H
#             - 06K
#             - 06L
#             - 06M
#             - 06N
#             - 06P
#             - 06Q
#             - 06T
#             - 06V
#             - 06W
#             - 06Y
#             - 07G
#             - 07H
#             - 07J
#             - 07K
#             - 07L
#             - 07M
#             - 07N
#             - 07P
#             - 07Q
#             - 07R
#             - 07T
#             - 07V
#             - 07W
#             - 07X
#             - 07Y
#             - 08A
#             - 08C
#             - 08D
#             - 08E
#             - 08F
#             - 08G
#             - 08H
#             - 08J
#             - 08K
#             - 08L
#             - 08M
#             - 08N
#             - 08P
#             - 08Q
#             - 08R
#             - 08T
#             - 08V
#             - 08W
#             - 08X
#             - 08Y
#             - 09A
#             - 09C
#             - 09D
#             - 09E
#             - 09F
#             - 09G
#             - 09H
#             - 09J
#             - 09L
#             - 09N
#             - 09P
#             - 09W
#             - 09X
#             - 09Y
#             - 10A
#             - 10C
#             - 10D
#             - 10E
#             - 10J
#             - 10K
#             - 10L
#             - 10Q
#             - 10R
#             - 10V
#             - 10X
#             - 11A
#             - 11E
#             - 11J
#             - 11M
#             - 11N
#             - 11X
#             - 12D
#             - 12F
#             - 13T
#             - 14L
#             - 14Y
#             - 15A
#             - 15C
#             - 15D
#             - 15E
#             - 15F
#             - 15M
#             - 15N
#             - 99A
#             - 99C
#             - 99D
#             - 99E
#             - 99F
#             - 99G
#             - 99H
#             - 99J
#             - 99K
#             - 99M
#             - 99N
#             - All
#             description: 'CCG:'
#             index: 191
#             layout: IPY_MODEL_d854993d72c24d1990227ed9fdb9bb73
#             style: IPY_MODEL_e96ed0eae5014c6d85abbd2eb7c5d86e
#         c17b326e780943d3af6fb3429b6a05bd:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         c441ac658bcd4a70b854c78d35ec8c59:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: HBoxModel
#           state:
#             children:
#             - IPY_MODEL_f153843a5f6d4fa39d7318fc8b9b05fc
#             layout: IPY_MODEL_464f0a80bfa04a26b66e95460d63f351
#         c4c3aa87e3a84629ad13fb279ba8b497:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'e-RD proportion:'
#             layout: IPY_MODEL_6ccc9faae2694450ba2e2e3dc1c8ce8a
#             max: 1
#             step: 0.1
#             style: IPY_MODEL_5b0c7a98207b4a23a0d4de789b5a4b45
#             value: 0.5
#         c5cb833375d74915a76c2391b80b1431:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         c6fdaa0e03544147833ac45315f0b2c2:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         c778db39893a4ffb9b355ca7102b92ab:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         ca6ee7c99c8e4499a9cc7aaaf726ba5f:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         cac5563991004ce8af0cd5f830975127:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         cbc38d8878fb4c488283ab59c169eb12:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'e-RD proportion:'
#             layout: IPY_MODEL_ae7650b2b1d44f93a6645cbf7bf8d7ec
#             max: 1
#             step: 0.1
#             style: IPY_MODEL_0683704fc53243a7ab5286d366de55f9
#             value: 0.5
#         cd3851f880b0492f8a8d80e230bff1a8:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         cf98378f0984482da80f4bb1b8472034:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         d0f4aab4810f40d285812f93f2eedd3a:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         d11b704cc6d3474b803db2d0c37c6f11:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DescriptionStyleModel
#           state:
#             description_width: ''
#         d169a3ef10274375ac0aecbf222b6178:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Months supply:'
#             layout: IPY_MODEL_5baf95409f694e3ba2a20bb0490b762a
#             max: 4
#             min: 1
#             style: IPY_MODEL_01b9ee8797e842e8b325a8b97e49d0c9
#             value: 3
#         d1bd140fe5d94160b976fa1638fd8e2b:
#           model_module: '@jupyter-widgets/output'
#           model_module_version: 1.0.0
#           model_name: OutputModel
#           state:
#             layout: IPY_MODEL_a1aad0cd303742aebf3cbd31f481affd
#             outputs:
#             - name: stdout
#               output_type: stream
#               text: "Total 28-day prescriptions = 87,207,906 \nPercent 1 month (of\
#                 \ all 1+2+3 month prescriptions) = 66% \nMean price per item = \xA3\
#                 1.04 \n\nDispensing fees =  \xA398.9 M \nStaff cost =  \xA330.7 M\
#                 \ \nWasted meds =  \xA33.3 M \nPatient cost =  \xA3159.9 M \n \nOverall\
#                 \ impact: =  \xA3193.9 M\n"
#         d1f2afa89ddb41fbbc8a0e63113a099d:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         d20a3b4c8ca04d3f9a615e7a3b6b3170:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         d2687c59190a46d3a558d97ae46a31e7:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: "Cost of public time (\xA3):"
#             layout: IPY_MODEL_347119322d9b41b5a2fccee2bc6ad20c
#             max: 15
#             min: 5
#             style: IPY_MODEL_fc2e9e1b957c4e1fbe2dc99e1e3c4250
#             value: 11
#         d2e642b8e2284e1f8235697b7b9b0773:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         d30cf61de06142b9ab7b613bd35b7526:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         d44baa9220f8481b8b868196d5771272:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         d459732f2bf74a28b0f5e97e35664b42:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: VBoxModel
#           state:
#             children:
#             - IPY_MODEL_bd6be7a84a5d44ffbbdf944d4c6a7f95
#             - IPY_MODEL_37eaf857e5e4432cb5b982e88e4253fc
#             - IPY_MODEL_3b9d969d72a84e018c0d765206c4a5c0
#             - IPY_MODEL_bc48a8092e1846a5b8757098a72b9252
#             - IPY_MODEL_cbc38d8878fb4c488283ab59c169eb12
#             - IPY_MODEL_297b2c51ee8b442387eebcc79e8f04c6
#             - IPY_MODEL_6af911478693467a876bff97b1957ad3
#             - IPY_MODEL_34d32f43481b4331811f4618dbdf3f8f
#             - IPY_MODEL_d1bd140fe5d94160b976fa1638fd8e2b
#             layout: IPY_MODEL_14165161302d425c8870b6db055ab571
#         d6410dcc4bba45478f48f2d58e997c27:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         d7ebc0eee4b24899b939cf866f2b37ad:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         d854993d72c24d1990227ed9fdb9bb73:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         d976abf58d8545c5b00a401967581db7:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion GP:'
#             layout: IPY_MODEL_821e987d67cd4291b19a567ac35257a6
#             max: 0.9
#             min: 0.1
#             step: 0.1
#             style: IPY_MODEL_572c8b3d3c634fe18bde6859317001be
#             value: 0.5
#         da5732005e2e43f0a7f971440e18eb34:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         dc89b321058d46b0b20924a1e4d81e45:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         ddc1b4baaa8140f5b7a1e397c889246a:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         ddd57415fc0c40c3bb2033265bfbc6bb:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         ded7eef2fefb44a9901fcdcf007353e6:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         dfc0b8d399ac4b698a83339c19c4b5cb:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         e08eb505c19d4c249ba1189bed48d72d:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         e2ad49ec6fbe417cb964956eb0b36711:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         e419a883ef8d402cbcebf78e7143262a:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         e7249d10b563404aaca5c3660da1f008:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         e96ed0eae5014c6d85abbd2eb7c5d86e:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: DescriptionStyleModel
#           state:
#             description_width: ''
#         e9e749d1df6745ee80903cdebe20f0de:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         ed3037a3440f4dc2aa5c8058ea537a4d:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         ed7fe31eb23148dfa0237bb8668710bd:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         edf588567a9f45fd88681722ea897b37:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         f04a2ccd6d714d68a9a909b047b525ee:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: VBoxModel
#           state:
#             children:
#             - IPY_MODEL_4142de5e35e148b181dbcec672edbcfe
#             - IPY_MODEL_92d653cda86a4cbe9a12bfe774eee114
#             - IPY_MODEL_6350c1e4353d40029903d413fb467ee3
#             - IPY_MODEL_29806774732543f4996711bc8b7f9a13
#             - IPY_MODEL_703a6c9c27fb42568bb84d63ff961243
#             - IPY_MODEL_74bf8356b19e456eb0cf2041101bc4a8
#             - IPY_MODEL_f99a2a49a9bc45e3ac004c00cc770d3b
#             - IPY_MODEL_089ea883e97043bebae1760673972732
#             - IPY_MODEL_f410854f26754a86b5929c792f4a59a9
#             layout: IPY_MODEL_aad3ec2643b4457baaa063546b3b3df1
#         f09d6872f78a45598cc61b40b790a1e8:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         f0eca3b0919647989771697393c22627:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         f153843a5f6d4fa39d7318fc8b9b05fc:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: VBoxModel
#           state:
#             children:
#             - IPY_MODEL_7d79ea1967e64f13a943a3d215d8b6e1
#             - IPY_MODEL_fc631556413f496b8d7d5aeac78ce8b3
#             - IPY_MODEL_4c8d3b247a1343db99352c67f6ab5b37
#             - IPY_MODEL_2683f8ea1d9f49149a7cba9dae2f56f6
#             - IPY_MODEL_28fc4881230541dd82fd29f08146470e
#             - IPY_MODEL_bb61b7ec786148d7bd87e2b17e941725
#             - IPY_MODEL_f4856bd76d3c44a58493b2f44c78d800
#             - IPY_MODEL_688a3cd17a244186aae96cf3d4925079
#             - IPY_MODEL_1429337cafa048dd9265f10747086de7
#             layout: IPY_MODEL_bea52f0756994415988752fffecdf4b2
#         f181796b669c40ee98a6369a6ba96a91:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         f308b6dee9e142248714dd410e8ee40c:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         f410854f26754a86b5929c792f4a59a9:
#           model_module: '@jupyter-widgets/output'
#           model_module_version: 1.0.0
#           model_name: OutputModel
#           state:
#             layout: IPY_MODEL_9ad146fea9cc40ed99bcccd58bcc556d
#             outputs:
#             - name: stdout
#               output_type: stream
#               text: "Total 28-day prescriptions = 106,436 \nPercent 1 month (of all\
#                 \ 1+2+3 month prescriptions) = 40% \nMean price per item = \xA31.00\
#                 \ \n\nDispensing fees =  \xA340,233 \nStaff cost =  \xA315,007 \n\
#                 Wasted meds =  \xA310,923 \nPatient cost =  \xA378,053 \n \nOverall\
#                 \ impact: =  \xA3103,983\n"
#         f44f36c4df1744d2a539dde910e3ec54:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         f4856bd76d3c44a58493b2f44c78d800:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: "Cost of public time (\xA3):"
#             layout: IPY_MODEL_f5ed39cfc5b845df9d76695570e0d8db
#             max: 15
#             min: 5
#             style: IPY_MODEL_c6fdaa0e03544147833ac45315f0b2c2
#             value: 11
#         f516d2f394f24d84a9978f76bc1e9876:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: VBoxModel
#           state:
#             children:
#             - IPY_MODEL_d169a3ef10274375ac0aecbf222b6178
#             - IPY_MODEL_f58b1ae4b46b45aaacdaebbc3b21a65e
#             - IPY_MODEL_683b92fb78ef478887dddb28a109207a
#             - IPY_MODEL_0803253b9b8e42d6a9b6a9adfc00fef1
#             - IPY_MODEL_458a443ba93d42aba1d07b1300f1db45
#             - IPY_MODEL_3cf090004fce4c4aa2ea83f8ce0f5c34
#             - IPY_MODEL_b74c2848dfe14b269cdf26938fc7dac4
#             - IPY_MODEL_7c39eb959d924c659f9fc29bd9672da9
#             - IPY_MODEL_2d9e695740d1441d84ccd01594c2293a
#             layout: IPY_MODEL_b24ba66d65094aa1b4c0cc78bfca7d91
#         f529bd8d02bc42e7b8faa5b0a9e2a48c:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: HBoxModel
#           state:
#             children:
#             - IPY_MODEL_1c6abc57904e4a0ba39ce0df435588fa
#             layout: IPY_MODEL_595e82f9893546b9a82ac6133b412830
#         f58b1ae4b46b45aaacdaebbc3b21a65e:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion amenable:'
#             layout: IPY_MODEL_0befbab010424a899e7e15a6c8fd0fbf
#             max: 0.95
#             min: 0.2
#             step: 0.05
#             style: IPY_MODEL_4ad580f5a2e9454ebfe63d927e736912
#             value: 0.9
#         f5ed39cfc5b845df9d76695570e0d8db:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#         f66157ad640a4b50a71c04bf22095e63:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         f99a2a49a9bc45e3ac004c00cc770d3b:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: IntSliderModel
#           state:
#             description: 'Time to collect (min):'
#             layout: IPY_MODEL_ac6b620e318d43cdacf1922aa0d1af2e
#             max: 30
#             style: IPY_MODEL_bc73ad9645374c1eb046ea3346bce87a
#             value: 10
#         fc2e9e1b957c4e1fbe2dc99e1e3c4250:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: SliderStyleModel
#           state:
#             description_width: initial
#         fc631556413f496b8d7d5aeac78ce8b3:
#           model_module: '@jupyter-widgets/controls'
#           model_module_version: 1.5.0
#           model_name: FloatSliderModel
#           state:
#             description: 'Proportion amenable:'
#             layout: IPY_MODEL_784c04cab34549de921d5271b55f98f5
#             max: 0.95
#             min: 0.2
#             step: 0.05
#             style: IPY_MODEL_f66157ad640a4b50a71c04bf22095e63
#             value: 0.9
#         ffe4ec48f4b24b84a3636b2e5b5bfe1f:
#           model_module: '@jupyter-widgets/base'
#           model_module_version: 1.2.0
#           model_name: LayoutModel
#           state: {}
#       version_major: 2
#       version_minor: 0
# ---

# ## Aim: To model the cost impact of dispensing 2 or 3 months rather than single months
#
# We examined the cost of a policy switch to recommend two or three monthly prescriptions across the NHS where there is no clinical rationale for issuing shorter durations. 
#

import os
from ebmdatalab import bq
import pandas as pd
import ipywidgets as widgets
from IPython.display import display, Markdown
from ipywidgets import Layout

# ## Assumptions
# - We assume that approx 10% of one-month prescriptions are appropriate (e.g. newly initiated patients). 

# ### What are the costs to include?

# > Longer prescription lengths were associated with more medication waste per prescription. However, when including dispensing fees and prescriber time, longer prescription lengths resulted in lower TUC. This finding was consistent across all five cohorts. Savings ranged from £8.38 to £12.06 per prescription per 120 days if a single long prescription was issued instead of multiple short prescriptions. Prescriber time costs accounted for the largest component of TUC.
#
# [Doble et al 2017]
#
# **1. Dispensing fees**
#
# - Currently 126p per item. 
# - Plus 2% of the cost per prescription (cost per day multiplied by prescription length) for prescriptions over £100 \*see below
#
# (https://psnc.org.uk/dispensing-supply/endorsement/fees-allowances/) 
#
# *Fees for expensive prescriptions (over £100)*
#
# Not a consideration for the drugs we are looking at, all of which are available generically:
# - Ramipril £2-5 /pack https://openprescribing.net/tariff/?codes=0205051R0AAADAD&codes=0205051R0AAANAN&codes=0205051R0AAAAAA&codes=0205051R0AAAKAK&codes=0205051R0AAABAB&codes=0205051R0AAALAL&codes=0205051R0AAACAC&codes=0205051R0AAAMAM
# - Atorvastatin <£2/pack https://openprescribing.net/tariff/?codes=0212000B0AAAAAA&codes=0212000B0AAABAB&codes=0212000B0AAACAC&codes=0212000B0AAADAD
# - Simvastatin <£2/pack https://openprescribing.net/tariff/?codes=0212000Y0AAAAAA&codes=0212000Y0AAABAB&codes=0212000Y0AAADAD&codes=0212000Y0AAAHAH
# - Levothyroxine max £15/pack during 18-19 https://openprescribing.net/tariff/?codes=0602010V0AABZBZ&codes=0602010V0AAGHGH&codes=0602010V0AABWBW&codes=0602010V0AABXBX&codes=0602010V0AABYBY
# - Amlodipine <£2/pack https://openprescribing.net/tariff/?codes=0206020A0AAABAB&codes=0206020A0AAAAAA
#
# **2. Prescriber time**
#
# Depending on the item, the prescriber time per prescription varies [Doble et al 2017]
# - antihypertensives: £3.77 (in 3-month scenario), £3.76 (28 days)	
# - diabetes: £3.55 (in 3-month scenario), £3.54 (28 days)	
# - SSRIs: £3.18 (in 3-month scenario), £3.23 (28 days)
#
# Note they use Figures from Curtis et al 2015, which are:
# - GP time £3.80/min, all practice expenses and including qualification costs (excluding quals it would be £3.20/min) - however, these are costs per minute **of patient contact** i.e. denominator used to calculate this rate was total patient contact time rather than total working hours?  
# - GP Nurse time £0.93/min (£56/hr per hour of F2F contact time), including qualification costs. (Basic rate is £36/hr / 0.6/min)
#
# Latest GP/nurse Figures from Curtis et al 2019:
# - GP  £132/hr (£2.20/min)
# - Nurse £37/hr (£0.62/min)
#
# With electronic repeat _dispensing_, it is possible that 12 months' of 28+ days' supply are authorised in one go, which means that changing the duration of each prescription would have no effect on prescriber time. With repeat _prescribing_, the patient must still request each prescription from the practice. 
#
# **3. Wastage**
#
# Depending on the item, the longer the duration, the more medicines will be wasted [Doble et al 2017]
# - antihypertensives: £0.51 (in 3-month scenario), £0.07 (28 days)	
# - diabetes: £1.37 (in 3-month scenario), £0.33 (28 days)	
# - SSRIs: £0.43 (in 3-month scenario), £0.21 (28 days)
#
# - For statins (secondary prevention) they found that 3.325% days of shorter duration 
#   (under 60 days) prescription supplies were wasted,
#   compared to 3.663% of longer duration (>=60 days) prescriptions. 
#
# **4. Patient time and expenses**
# - Time required to travel to pharmacy / GP?
# - DIfferences for dispensing practices (>1.6m)?
# - Time taken to collect prescription? Under electronic prescribing prescriptions may already be ready to collect when the patient arrives. 
#
# - Sliding scale might be the best way! 
# - The majority of population live within 20 mins walk of a pharmacy (few years old maybe)
#
# **5. Income generation**
# - Patients eligible to pay for prescriptions pay a fixed amount per prescription which contributes towards the total prescribing bill. For each prescription dispensed for 84 rather than 28 days, income would be reduced by 2/3.
#
# - However, the majority of prescriptions (90%?) are exempt from charges, for example over 60s, under 19s, people on low incomes etc. Those eligible to pay who collect a lot of medications can have their total capped. 
#
# - Therefore, for the medications we are considering we may expect that >95% of the prescriptions (2x statins, largely over-60s) are not paid for by patients. 
#
# - Crucially, where patients pay for routine prescriptions, it is likely that they are already given 84 days supply to reduce the cost burden on them.
#
# - Therefore, we would expect a very small decrease in income from changing patients from 28 day prescriptions to longer durations.
#
# **Refs**
# - *Doble B, Payne R, Harshfield A, Wilson EC. BMJ Open. 2017;7(12):e019382.*
# - *Curtis L , Burns A . Unit Costs of Health and Social Care. Canterbury, UK: Personal Social Services Research Unit, The University of Kent, 2015*

# **Example from previous literature**
#
# > **Three-Month Versus 28-Day Prescribing of Antihypertensives**
#
# > We conducted two analyses representing alternative scenarios. 
# In both cases we first added in the transaction and drug wastage costs (Table 3). 
#
# > For the 3-month arm this equated to an extra 
# £21.01 per annum [= **dispensing fees** (£0.90) + **prescriber time** (£3.77) + **wastage costs** (£0.51) × (365/90)], 
#
# > and in the 28-day arm, 
# £61.68 [= dispensing fees (£0.90) + prescriber time (£3.76) + wastage costs (£0.07) × (365/28)].
#
# From Martin A, Payne R, Wilson EC. Appl Health Econ Health Policy 2018;16:317–30. doi:10.1007/s40258-018-0383-9

# ## Load summary prescribing data

df = pd.read_csv(os.path.join('..','data','table1_qpi_summary.csv'))
prescribing_data = df.set_index('quantity_per_item')['items']
display(prescribing_data)

# # Calculations - formation of model

# ## 1. Dispensing fees

# - 126p - cost per item dispensed (not divided across items on same prescription form)
#

# +
dispensing = 1.26

dispensing_28 = dispensing*prescribing_data[28]

display(Markdown(f"Current total dispensing cost for all 28-day supplies: **£{dispensing_28/1E6:.1f} M**"))

# Calculate cost of dispensing 90% of 28-day prescriptions in 3-month batches:
n=0.9*dispensing_28/3

display(Markdown(
    f"Potential reduction in cost if 90% one-month prescriptions were 3-months: **£{n/1E6:.1f} M** ({100*n/dispensing_28:.1f}% of total 28-day dispensing fees)"
    ))
# -

# ## 2. Prescriber time

# +
cdoc = 2.2 # cost per minute for GP time
cnur = 0.62 # cost per minute for nurse time

# note the values for the following variables are selected arbitrarily
prop_doc = 0.5 # proportion approved by a GP
prop_nur = 1-prop_doc # proportion approved by a nurse

t_approve = 0.5 # time taken to approve a repeat prescription (minutes)
prop_erd = 0.5 # proportion of prescriptions on electronic repeat dispensing (assume zero cost - or one cost per 12 months?)

cpp_doc = cdoc*t_approve*(1-prop_erd) # cost per average prescription (doc)
cpp_nur = cnur*t_approve*(1-prop_erd) # cost per average prescription (nur)

approval = (prop_doc*cpp_doc) + (prop_nur*cpp_nur)
approval_28 = prescribing_data[28]*approval # cost to approve all 28-day prescriptions

display(Markdown(f"Current total estimated approval cost for all 28-day supplies: **£{approval_28/1E6:.1f} M**"),
       Markdown(f"Potential reduction in cost if 90% were 84-days: **£{(0.9*approval_28/3)/1E6:.1f} M** ({100*(0.9*approval_28/3)/approval_28:.1f}% of total 28-day approval fees)"
    ))
# -

# ## 3. Wastage

# +
waste_s = 0.03325 # 3.325% days wasted of shorter duration (\<60 days) prescription supplies
waste_l = 0.03663 # 3.663% of longer duration  (\>=60 days) prescriptions. 
# [Doble et al 2017]

display(Markdown("#### Example: Atorvastatin (For price estimate, 20mg tabs averaged around 80p per 28-tablet pack in 2018-19)"))
priceperitem = 0.8
print ("£%8.5f"%(priceperitem*waste_s), " (3.325%) wasted per 28-day supply")
print ("£%8.5f"%(3*priceperitem*waste_l), " (3.663%) wasted per 84-day supply")

# -

# ### Extract prescribing data at CCG level with costs to calculate mean price-per-item

# +
### extract 28-day prescribing data for modelling


sql = '''
    SELECT
      pct,
      SUM(IF(quantity_per_item=28,items,0)) AS items_28d,
      SUM(items) AS total_items,
      SUM(IF(quantity_per_item=28,net_cost,0)) AS net_cost_28d

    FROM
     ebmdatalab.hscic.raw_prescribing_normalised AS presc
    INNER JOIN  hscic.ccgs AS ccgs ON presc.pct=ccgs.code AND ccgs.org_type='CCG'

    WHERE
    quantity_per_item IN (28,56,84)
    AND month BETWEEN '2018-08-01' AND '2019-07-01'
    AND 
    (bnf_code LIKE "0205051R0%" OR  ##ramipril
    bnf_code LIKE "0212000B0%" OR ##atrovastatin
    bnf_code LIKE "0212000Y0%" OR ##simvastatin
    bnf_code LIKE "0602010V0%" OR ##levothyroxine
    bnf_code LIKE "0206020A0%") ##amlodipine
    AND
    (bnf_name LIKE '%_Tab%' or bnf_name LIKE '%_Cap%') ##this restricts to tablets or capsules

    GROUP BY pct
        '''

df_ltc = bq.cached_read(sql, csv_path=os.path.join("..", "data", "ltc_qty_cost.csv"))

def calc_cost_per_item(df):
    # calculate cost per item per ccg and overall

    data = df.set_index("pct").sort_index()
    # add a total row
    data = data.append(data.sum().rename("All")).reset_index()

    # calculate additional fields
    data["percent_28d"] = 100*data['items_28d']/data['total_items']
    data["cost_per_item"] = data['net_cost_28d']/data['items_28d']

    priceperitem = data.loc[data["pct"]=="All", "cost_per_item"].item()
    display(Markdown(f"Latest mean price-per-item: **£{round(priceperitem,4)}**"))
    return priceperitem, data

priceperitem, df_ltc = calc_cost_per_item(df_ltc)

# +
# Scale up to all of our 5 medicines...
display(Markdown("#### Scaling up estimated wastage using £1.04 per item"))

waste_28 = priceperitem*prescribing_data[28]*waste_s

print ("£{:,.2f}".format(waste_28/1E6), "M (3.325%) estimated current wastage of all 28-day supplies")
print ("£{:,.2f}".format((priceperitem*waste_l*prescribing_data[28]*3*0.9)/1E6 + (waste_28*0.1)/1E6), "M wasted if 90% of all 28-day supplies were 84-day")
# -

# ## 4. Patient time and expenses

# +
# Conservatively assume 10 mins per prescription (a low estimate to account for most people going to the pharmacy while nearby)
time_collect = 10/60 # hours per prescription
print ("{:,.1f}".format((time_collect*12)), " estimated hours per patient per year on 28-day supplies")
print ("{:,.1f}".format((time_collect*12/3)), " estimated hours per patient per year on 84-day supplies")

cost_public = 11 # cost of public time per hour
total_time_28 = time_collect*prescribing_data[28]
total_time_switch = ((0.1)+(0.9/3))*total_time_28
display(Markdown (f"{total_time_28/1E6:,.0f} M estimated total patient hours to collect all 28-day supplies (**£{cost_public*total_time_28/1E6:.1f}M** at £{cost_public}/h)"),
        Markdown (f"{total_time_switch/1E6:,.0f} M total patient hours if 90% 28-day supplies were 84 days (**£{cost_public*total_time_switch/1E6:.1f}M** at £{cost_public}/h)"))


# -


# # Model
#  This estimates the total costs for switching a given percentage of 28-day prescriptions to 2/3/4 month supplies.
#  (It does not add on the cost for existing 56 and 84 day supplies)

# +
from model import cost_model

# -


# # Apply Model

# +
prescriptions=prescribing_data[28]
percent_amenable = 0.9   
time_collect = 10

months_supply_list = [1,2,3] # current status vs switch to 2 or 3 months



def apply_model(months_supply_list, prescriptions, percent_amenable, dispensing, prop_doc, prop_erd, t_approve, priceperitem, cost_public, time_collect, save_output=True):
    
    model_output = pd.DataFrame(index=["dispensing","staff","waste","patient"], columns=[1,2,3])
    
    for months_supply in months_supply_list: 

        results = cost_model(prescriptions=prescriptions, 
                             months_supply=months_supply, 
                             percent_amenable=percent_amenable, 
                             dispensing=dispensing, 
                             prop_doc=prop_doc, 
                             prop_erd=prop_erd, 
                             t_approve=t_approve, 
                             priceperitem=priceperitem, 
                             cost_public=cost_public, 
                             time_collect=time_collect)
        model_output[months_supply] = results/1E6

        display_text =f"Estimated cost for 28-day prescriptions with {percent_amenable*100}% switched to **{months_supply} month** supplies: "
        if months_supply==1:
            display_text = "Current estimated cost for 28-day prescriptions: "
        display(Markdown(f"{display_text} **£{(results.sum()) /1E6:.1f} M** ")
               )

    # calculate total and savings    
    model_output = model_output.transpose()
    model_output["total"] = model_output.sum(axis=1)
    model_output["saving"] = model_output["total"][1] - model_output["total"]

    if save_output == True:
        model_output.round(1).to_csv(os.path.join('..','data','cost_model_summary.csv'))
    display(model_output.round(1))
    
apply_model(months_supply_list, prescriptions, percent_amenable, dispensing, prop_doc, prop_erd, t_approve, priceperitem, cost_public, time_collect)
# -

# ## Apply model to larger basket of drugs
# **Note larger basket includes 2/3-per-day drugs so we will infer the proportion 28-day from the smaller basket, per CCG.**

# +
larger_basket = pd.read_csv(os.path.join('..','data','data_cost_model.csv'), index_col=0)

# proportion 28d from small basket for each ccg:
larger_basket = larger_basket.merge(df_ltc[["pct","percent_28d"]], on="pct")
larger_basket["items_28d"] = larger_basket["percent_28d"]*larger_basket["total_items"]/100

larger_basket.head() 


# +
# get average costs per item for larger basket
chemicals = "'" + "','".join(larger_basket.chemical_code.unique()) +"'"

sql2=f'''
SELECT
SUBSTR(presc.bnf_code,0,9) as chemical_code,
SUM(IF(quantity_per_item=28,items,0)) AS items_28d,
SUM(IF(quantity_per_item=28,net_cost,0)) AS net_cost_28d

FROM
  ebmdatalab.hscic.raw_prescribing_normalised AS presc
-- use a view which has form_route field from dmd for each bnf_code to filter by form
INNER JOIN  measures_v2.dmd_objs_with_form_route as form ON presc.bnf_code=form.bnf_code
AND form_route like '%oral' and (form_route like 'tab%' or form_route like 'cap%')

WHERE
SUBSTR(presc.bnf_code,0,9) IN ({chemicals}) 
AND (month BETWEEN '2018-09-01' AND '2019-08-01')
    
GROUP BY
chemical_code
ORDER BY
chemical_code
'''

df_lb_costs = bq.cached_read(sql2, csv_path=os.path.join('..','data','df_lb_costs.csv'))
df_lb_costs.head()

# +
# summarise cost per item across larger basket

df_lb_costs_2 = df_lb_costs.copy()
df_lb_costs_2["cost_per_item"] = df_lb_costs_2['net_cost_28d']/df_lb_costs_2['items_28d']
# note cost_per_item is for a 28-day supply
display(df_lb_costs_2[["cost_per_item"]].describe())

# -

# ### Because costs per item vary more widely in this larger basket we will model the costs for each chemical individually

# +
# add cost per item onto data
lb = larger_basket.merge(df_lb_costs_2[["chemical_code","cost_per_item"]], on="chemical_code")

# list chemicals in descending order of total 28-day prescriptions
chem_list = lb.groupby("chemical")["items_28d"].sum().sort_values(ascending=False)

for c in chem_list.index:
    data = lb.loc[lb["chemical"]==c]
    prescriptions = data.items_28d.sum()
    priceperitem = data.cost_per_item.mean()
    display (Markdown(f"## {c}"),
             Markdown(f"### Prescriptions: {round(prescriptions/1E6,1)} M, mean price per item: £{round(priceperitem,2)}"))
    apply_model(months_supply_list, prescriptions, percent_amenable, dispensing, prop_doc, prop_erd, t_approve, priceperitem, cost_public, time_collect, save_output=False)
# -


