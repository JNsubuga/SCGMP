from .Grants import Grants
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from api.core.helper.helper import Helper

DEFAULT_LANG = "en"

# instantiate grants class

_grant = Grants()
_helper = Helper()

class getAllGrants(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def get(self, request, lang):
        lang = DEFAULT_LANG if lang == None else lang
        response = _grant.getAllGrants(request, lang)
        return Response(response)
    
class getGrantById(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def get(self, request, lang, grantid):
        lang = DEFAULT_LANG if lang == None else lang
        if not grantid:
            return Response(
                {"message": "Incomplete data request!!!", "status": False},
                status=400
            )
        elif not _grant.GrantExists(request, lang, grantid):
            return Response(
                {"message": "Grant doesn't exist!!!", "status": False},
                status=400
            )
        else:
            response = _grant.getGrantById(request, lang, grantid)
            return Response(response)
        
class createGrant(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["post"]

    def post(self, request, lang):
        lang = DEFAULT_LANG if lang == None else lang
        data = request.data
        # return Response({"data":data})
        #############################################
        auth_token = _helper.getAuthToken(request)
        if not auth_token["status"]:
            return Response(
                auth_token,
                status=400
            )
        token = auth_token["token"]
        #############################################
        userid = Token.objects.get(key=token).user_id
        if len(data) > 0:
            if not data["GrantName"]:
                return Response(
                    {"message": "Grant Name is a required field!!!", "status": False}
                )
            elif not data["GrantAbriviation"]:
                return Response(
                    {"message": "Grant Abriviation is a required field!!!", "status": False}
                )
            else:
                _grant.createGrant(request, lang, userid, data)
                return Response(
                    {"message": "Grant Registered Successfully!!", "status": True},
                    status=201
                )
        else:
            return Response(
                {"message": "No data submited to the database!!!", "status": False},
                status=403
            )
        
class updateGrant(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["put"]

    def put(self, request, lang, grantid):
        lang = DEFAULT_LANG if lang == None else lang
        if not grantid:
            return Response(
                {"message": "Incomplete data request!!!", "status": False},
                status=400
            )
        if not _grant.GrantExists(request, lang, grantid):
            return Response(
                {"message": "Grant doesn't Exist!!!", "status": False}
            )
        else:
            data = request.data
            _grant.updateGrant(request, lang,  grantid, data)
            return Response(
                {"message": "Grant Successfully Updated!!", "status": True},
                status=201
            )