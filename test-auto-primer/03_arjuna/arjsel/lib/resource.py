from arjuna import *
from .wordpress import WordPress

@for_test
def wordpress(request):
    yield WordPress()