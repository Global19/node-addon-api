{
  'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
  'cflags': [ '-fno-exceptions' ],
  'cflags_cc': [ '-fno-exceptions' ],
  'msvs_settings': {
    'VCCLCompilerTool': {
      'ExceptionHandling': 0,
      'EnablePREfast': 'true',
    },
  },
  'xcode_settings': {
    'CLANG_CXX_LIBRARY': 'libc++',
    'MACOSX_DEPLOYMENT_TARGET': '10.7',
    'GCC_ENABLE_CPP_EXCEPTIONS': 'NO',
  },
}
