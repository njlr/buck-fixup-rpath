# buck-fix-rpath

You may need to install `patchelf`.

```bash
sudo apt install -y patchelf
```

## Build the App

```bash
make
buck run :main
```

## Inspect the dynamic libraries

```bash
ldd buck-out/gen/main
```

## Make the bundle

```bash
buck build :main-bundle
ls buck-out/gen/main-bundle/out
```

## Inspect the dynamic libraries

```bash
patchelf --print-rpath ./buck-out/gen/main-bundle/out/main
ldd buck-out/gen/main-bundle/out/main
```
