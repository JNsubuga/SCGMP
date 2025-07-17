from .GoodSamaritans import GoodSamaritans
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from datetime import date, datetime

from api.core.helper.helper import Helper


DEFAULT_LANG = "en"

# instantiate grants class

_goodSamaritan = GoodSamaritans()
_helper = Helper()

class getAllGoodSamaritans(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def get(self, request, lang):
        lang = DEFAULT_LANG if None else lang
        response = _goodSamaritan.getAllGoodSamaritans(request, lang)
        return Response(response)
    
# class getAllGrantGoodSamaritans(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     http_method_names = ["get"]

#     def get(self, request, lang):
#         lang = DEFAULT_LANG if None else lang
#         response = _goodSamaritan.getAllGrantGoodSamaritans(request, lang)
#         return Response(response)
    
# class getAllGrantGoodSamaritansNGrantType(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     http_method_names = ["get"]

#     def get(self, request, lang, grantId):
#         lang = DEFAULT_LANG if None else lang
#         response = _goodSamaritan.getAllGrantGoodSamaritansNGrantType(request, lang, grantId)
#         return Response(response)
    
class getGoodSamaritanById(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def get(self, request, lang, goodsamaritanid):
        lang = DEFAULT_LANG if None else lang
        if not goodsamaritanid:
            return Response(
                {"message": "Incomplete data request!!!", "status": False},
                status=400
            )
        elif not _goodSamaritan.GoodSamaritanExists(request, lang, goodsamaritanid):
            return Response(
                {"message": "Good Samaritan doesn't!!!", "status": False},
                status=400
            )
        else:
            response = _goodSamaritan.getGoodSamaritanById(request, lang, goodsamaritanid)
            return Response(response)
        
class createGoodSamaritan(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["post"]

    def checkAge(self, birthDate):
        dob = datetime.strptime(birthDate, "%Y-%m-%d")
        today = date.today()
        age = today.year - dob.year
        # return age
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            age -= 1
        if age >= 65:
            return True
        else:
            return False

    def post(self, request, lang):
        lang = DEFAULT_LANG if lang == None else lang
        data = request.data
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
            if not data["names"]:
                return Response(
                    {"message": "Names is a reuqired field!!!", "status": False}
                )
            elif not data["phoneNumber"]:
                return Response(
                    {"message": "Phone Number is a required field!!!", "status": False}
                )
            elif not data["BirthDate"]:
                return Response(
                    {"message": "Date of Birth is a required field!!!", "status": False}
                )
            elif not self.checkAge(data["BirthDate"]):
                return Response(
                    {"message": "The Member's age is below the minimum elderly Age (65 yr)", "status": False}
                )
            elif not data["placeOfResidence"]:
                return Response(
                    {"message": "Place of residence is a required field!!!", "status": False}
                )
            elif not data["timeOfStay"]:
                return Response(
                    {"message": "Time of Stay is a required field!!!", "status": False}
                )
            elif not data["hasDependants"]:
                return Response(
                    {"message": "Has Dependants is a required field!!!", "status": False}
                )
            elif data["hasDependants"] and not data["numberOfDependants"]:
                return Response(
                    {"message": "Number Of Dependants is a required field!!!", "status": False}
                )
            elif not data["hasNationalID"]:
                return Response(
                    {"message": "Has Natioal ID is a required field!!!", "status": False}
                )
            elif data["hasNationalID"] and len(data["NIN"]) != 14:
                return Response(
                    {"message": "Invalid NIN!!!", "status": False}
                )
            elif not data["youthHoodBusiness"]:
                return Response(
                    {"message": "Youthhood Business is a required field!!!", "status": False}
                )
            elif data["getsGrant"] and not data["forHowLong"]:
                return Response(
                    {"message": "For how long is a required field!!!", "status": False}
                )
            elif data["getsGrant"] and not data["howMuch"]:
                return Response(
                    {"message": "How much is a required field!!!", "status": False}
                )
            elif data["getsGrant"] and not data["howItHelpedYou"]:
                return Response(
                    {"message": "How It Helped You is a required field!!!", "status": False}
                )
            elif data["getsGrant"] and not data["BenefitsFromGoodSamaritan"]:
                return Response(
                    {"message": "Benefit Of Good Samaritan Group is a required field!!!", "status": False}
                )
            elif data["getsGrant"] and not data["grant"]:
                return Response(
                    {"message": "Grant is a required field!!!", "status": False}
                )
            elif not data["howDoYouSurvive"]: 
                return Response(
                    {"message": "How Do You Survive is a required field!!!", "status": False}
                )
            elif not data["placeOfWorship"]:
                return Response(
                    {"message": "Place of Worship is a required field!!!", "status": False}
                )
            elif not data["yourNeedFromGovtAsAGrand"]:
                return Response(
                    {"message": "Your Need From Gov't is a required field!!!", "status": False}
                )
            else:
                _goodSamaritan.createGoodSamaritan(request, lang, userid, data)
                return Response(
                    {"message": "Good Samaritan Registered Successfully!!", "status": True},
                    status=201
                )
        else:
            return Response(
                {"message": "No data submited to the database!!!", "status": False},
                status=403
            )
        # return Response({data["numberOfDependants"]})
        
class updateGoodSamaritan(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["put"]

    def put(self, request, lang, goodSamaritanid):
        lang = DEFAULT_LANG if lang == None else lang
        if not goodSamaritanid:
            return Response(
                {"message": "Incomplete data request!!!", "status": False},
                status=400
            )
        if not _goodSamaritan.GoodSamaritanExists(request, lang, goodSamaritanid):
            return Response(
                {"message": "Good Samaritan doesn't Exist!!!", "status": False}
            )
        else:
            data = request.data  
            _goodSamaritan.updateGoodSamaritan(request, lang, data, goodSamaritanid)
            return Response(
                {"message": "Good Samaritan Successfully Updated!!", "status": True},
                status=201
            )