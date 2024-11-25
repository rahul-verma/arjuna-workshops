import pytest

from arjuna.engine.pytest import PytestHooks


try:
    from arjsel.lib.resource import *
except ModuleNotFoundError as e:
    if e.name not in {"arjsel.lib", "arjsel.lib.resource"}:
        raise Exception(e.name)

