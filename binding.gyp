{
    "targets": [
        {
            "target_name": "3Ttechapi",
            "sources": [
                "src/3Ttechapi.cc",
                "src/TTTRtcEngine.h",
                "src/TTTEngineEventHandler.h",
                "src/TTTstruct.h",
                "src/TTTEngineEventHandler.cpp",
                "src/TTTstruct.h",
		"src/JSON/jsoncpp.cpp",
		"src/base64.c",
		"inc/MyAudioApi.h",
		"inc/MyVideoApi.h"
            ],
            "cflags!": [
                "-fno-exceptions"
            ],
            "cflags_cc!": [
                "-fno-exceptions"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
		"<!(node -e \"require('nan')\")", 
		"<!(node -e \"require('streaming-worker-sdk')\")"
            ],
            "dependencies": [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
	     "conditions": [
                [
                    "OS==\"win\"",
                    {
                        "msvs_settings": {
                            "VCCLCompilerTool": {
                                "ExceptionHandling": 1
                            }
                        },
                        "libraries": [
                            "<(module_root_dir)/lib/myaudiodll.lib",
                            "<(module_root_dir)/lib/wstechapi.lib",
                            "<(module_root_dir)/lib/GSVideo.lib",
                        ],
                        "copies": [
                            {
                                "destination": "<(module_root_dir)/build/Release/",
                                "files": [
                                    "<(module_root_dir)/lib/myaudiodll.dll",
                                    "<(module_root_dir)/lib/wstechapi.dll",
									"<(module_root_dir)/lib/GSVideo.dll"
                                ]
                            }
                        ]
                    }
                ],
                [
                    "OS==\"mac\"",
                    {
          "xcode_settings": {
            "CLANG_CXX_LIBRARY": "libc++",
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
            "MACOSX_DEPLOYMENT_TARGET": "10.7"
                        }
                    }
                ]
            ]
    }
  ]
}
