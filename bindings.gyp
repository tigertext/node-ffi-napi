{
  'targets': [
    {
      'target_name': 'ffi_bindings',
      'sources': [
          'src/ffi.cc'
        , 'src/callback_info.cc'
        , 'src/pointer.cc'
        , 'src/threaded_callback_invokation.cc'
        , 'src/foreign_caller.cc'
      ],
      'include_dirs': [ 'deps/libffi/include' ],
      'conditions': [
        ['OS=="win"', {
          'libraries': [ 'deps/libffi/.libs/libffi.lib' ],
          'dependencies': [
              'deps/dlfcn-win32/dlfcn.gyp:dlfcn'
          ]
        }, {
          'libraries': [ 'deps/libffi/.libs/libffi.a' ],
        }]
      ]
    }
  ]
}