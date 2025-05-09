from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'/users', UserFViewset)
router.register(r'/statements', StatementViewset)
router.register(r'/reactions', ReactionViewset)