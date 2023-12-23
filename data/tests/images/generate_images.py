"""Generate test images."""
import importlib
from pathlib import Path
import shutil

import pyvista as pv
from pytest_pyvista import VerifyImageCache

import geovista as gv
from geovista.common import get_modules
import geovista.examples
from geovista.report import Report


EXAMPLES = get_modules("geovista.examples")

pv.global_theme.load_theme(pv.plotting.themes._TestingTheme())
pv.OFF_SCREEN = True
gv.GEOVISTA_IMAGE_TESTING = True

n_scripts: int = len(EXAMPLES)
width: int = len(str(n_scripts))

cache_dir = Path(__file__).parent.resolve() / "image_cache"
if cache_dir.is_dir():
    shutil.rmtree(str(cache_dir))
if not cache_dir.exists():
    cache_dir.mkdir()

print(f'\nGenerating {n_scripts} test images in "{cache_dir} ...')

for i, script in enumerate(EXAMPLES):
    print(
        f'[{i+1:0{width}d}/{n_scripts}] Generating image for "{script}" example ... ',
        end="",
        flush=True,
    )
    module = importlib.import_module(f"geovista.examples.{script}")
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
    fh.write("```bash\n")
    fh.write(f"{str(Report())}\n")
    fh.write("```\n")

print('\nUpdated report details in "README.md"\n')
print("👍 All done!")
