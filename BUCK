prebuilt_cxx_library(
  name = 'test',
  header_namespace = '',
  exported_headers = [
    'test.h'
  ],
  shared_lib = 'libtest.so',
  preferred_linkage = 'shared',
)

cxx_binary(
  name = 'main',
  srcs = [
    'main.cpp',
  ],
  deps = [
    ':test',
  ],
)

genrule(
  name = 'main-bundle',
  out = 'out',
  srcs = [
    'remove-needed-regex.py',
    'libtest.so',
  ],
  cmd = ' && '.join([
    'mkdir -p $OUT',
    'cp $SRCDIR/libtest.so $OUT/libtest.so',
    'cp $(location //:main) $OUT/main',
    '$SRCDIR/remove-needed-regex.py $OUT/main "^.*libtest.*$"',
    'patchelf --set-rpath \'$ORIGIN\' $OUT/main',
    'patchelf --add-needed libtest.so $OUT/main',
  ]),
)
