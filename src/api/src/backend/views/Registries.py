from backend.views.RestrictedAPIView import RestrictedAPIView
from backend.views.http.responses import BaseResponse

class Registries(RestrictedAPIView):
    def get(self, request):
        return BaseResponse(result={"test": "test"})