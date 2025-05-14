from setuptools import setup

setup(
    # Compile C extensions
    cffi_modules=["pyargon2/_compiler.py:ffi"],
)
