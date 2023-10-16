"""Generate test images."""
import importlib
from pathlib import Path
import pkgutil
import shutil

import pyvista as pv
from pytest_pyvista import VerifyImageCache

import geovista as gv
import geovista.examples
from geovista.cache import CACHE
from geovista.report import Report


SCRIPTS = sorted(
    [submodule.name for submodule in pkgutil.iter_modules(gv.examples.__path__)]
)

pv.global_theme.load_theme(pv.plotting.themes._TestingTheme())
pv.OFF_SCREEN = True
gv.GEOVISTA_IMAGE_TESTING = True

n_scripts: int = len(SCRIPTS)
width: int = len(str(n_scripts))

cache_dir = Path(__file__).parent.resolve() / "image_cache"
if cache_dir.is_dir():
    shutil.rmtree(str(cache_dir))
if not cache_dir.exists():
    cache_dir.mkdir()

print(f'\nGenerating {n_scripts} test images in "{cache_dir} ...')

for i, script in enumerate(SCRIPTS):
    print(
        f'[{i+1:0{width}d}/{n_scripts}] Generating image for "{script}" example ... ',
        end="",
        flush=True,
    )
    module = importlib.import_module(f"geovista.examples.{script}")
    _ = CACHE.fetch(f"tests/images/{script}.png")
    verify_image_cache = VerifyImageCache(f"test_{script}", cache_dir)
    verify_image_cache.add_missing_images = True
    pv.global_theme.before_close_callback = verify_image_cache
    module.main()
    print("done!", flush=True)

fname = "README.md"
with open(fname, "w", encoding="utf-8") as fh:
    fh.write("# ⚠\n\n")
    fh.write(
        "Please **do not** manually edit this `README.md` as the contents will be overwritten by the `generate_images.py` script.\n\n"
    )
    fh.write(
        "This directory contains test images generated on the following platform:\n"
    )
    fh.write(f"{str(Report())}\n")

print('\nUpdated report details in "README.md"\n')
print("👍 All done!")
