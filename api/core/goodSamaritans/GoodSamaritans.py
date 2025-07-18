from api.core.helper import helper
from api.models import *
from datetime import date
from django.db.models import Q

from api.core.users.Users import Users
from api.core.grants.Grants import Grants
from api.core.locale.Locale import Locale


class GoodSamaritans:
    def __init__(self):
        self.users = Users()
        self.grants = Grants()

    def calculate_age(self, request, birthdate):
        today = date.today()
        age = today.year - birthdate.year
        if today.month < birthdate.month or (
            today.month == birthdate.month and today.day < birthdate.day
        ):
            age -= 1
        return age

    def getAllGoodSamaritans(self, request, lang, getsGrant=None, grantNameId=None):
        results = []
        goodSamaritans = GoodSamaritan.objects.filter(is_disabled=False)
        # Filter gets grant
        if getsGrant and not (goodSamaritans == None):
            goodSamaritans = goodSamaritans.filter(getsGrant=getsGrant)
        # Filter grantById
        if (
            grantNameId
            and not (grantNameId == None)
            and self.grants.GrantExists(request, lang, grantNameId)
        ):
            goodSamaritans = goodSamaritans.filter(grant_id=int(grantNameId))
        # lastly Order By
        goodSamaritans = goodSamaritans.order_by("id")
        for goodSamaritan in goodSamaritans:
            goodSamaritan_item = {
                "id": goodSamaritan.pk,
                "names": goodSamaritan.names,
                "phoneNumber": goodSamaritan.phoneNumber,
                "BirthDate": goodSamaritan.BirthDate,
                "age": self.calculate_age(request, goodSamaritan.BirthDate),
                "placeOfResidence": goodSamaritan.placeOfResidence,
                "timeOfStay": goodSamaritan.timeOfStay,
                "hasDependants": goodSamaritan.hasDependants,
                "numberOfDependants": goodSamaritan.numberOfDependants,
                "hasNationalID": goodSamaritan.hasNationalID,
                "NIN": goodSamaritan.NIN,
                "youthHoodBusiness": goodSamaritan.youthHoodBusiness,
                "getsGrant": goodSamaritan.getsGrant,
                "forHowLong": goodSamaritan.forHowLong,
                "howMuch": goodSamaritan.howMuch,
                "howItHelpedYou": goodSamaritan.howItHelpedYou,
                "BenefitsFromGoodSamaritan": goodSamaritan.BenefitsFromGoodSamaritan,
                "grant": self.grants.getGrantById(
                    request, lang, goodSamaritan.grant.pk
                ),
                "howDoYouSurvive": goodSamaritan.howDoYouSurvive,
                "placeOfWorship": goodSamaritan.placeOfWorship,
                "yourNeedFromGovtAsAGrand": goodSamaritan.yourNeedFromGovtAsAGrand,
                "adviseToTheYouth": goodSamaritan.adviseToTheYouth,
                "submitted_by": self.users.getAuthUserById(
                    request, lang, goodSamaritan.submitted_by.pk
                ),
                "is_disabled": goodSamaritan.is_disabled,
                "created": goodSamaritan.created,
            }
            results.append(goodSamaritan_item)
        return results

    # def getAllGrantGoodSamaritans(self, request, lang):
    #     results = []
    #     goodSamaritans = GoodSamaritan.objects.filter(Q(is_disabled=False) & Q(getsGrant=True)).order_by("id")
    #     for goodSamaritan in goodSamaritans:
    #         goodSamaritan_item = {
    #             "id": goodSamaritan.pk,
    #             "names": goodSamaritan.names,
    #             "phoneNumber": goodSamaritan.phoneNumber,
    #             "BirthDate": goodSamaritan.BirthDate,
    #             "age": self.calculate_age(request, goodSamaritan.BirthDate),
    #             "placeOfResidence": goodSamaritan.placeOfResidence,
    #             "timeOfStay": goodSamaritan.timeOfStay,
    #             "hasDependants": goodSamaritan.hasDependants,
    #             "numberOfDependants": goodSamaritan.numberOfDependants,
    #             "hasNationalID": goodSamaritan.hasNationalID,
    #             "NIN": goodSamaritan.NIN,
    #             "youthHoodBusiness": goodSamaritan.youthHoodBusiness,
    #             "getsGrant": goodSamaritan.getsGrant,
    #             "forHowLong": goodSamaritan.forHowLong,
    #             "howMuch": goodSamaritan.howMuch,
    #             "howItHelpedYou": goodSamaritan.howItHelpedYou,
    #             "BenefitsFromGoodSamaritan": goodSamaritan.BenefitsFromGoodSamaritan,
    #             "grant": self.grants.getGrantById(request, lang, goodSamaritan.grant.pk),
    #             "howDoYouSurvive": goodSamaritan.howDoYouSurvive,
    #             "placeOfWorship": goodSamaritan.placeOfWorship,
    #             "yourNeedFromGovtAsAGrand": goodSamaritan.yourNeedFromGovtAsAGrand,
    #             "adviseToTheYouth": goodSamaritan.adviseToTheYouth,
    #             "submitted_by":  self.users.getAuthUserById(request, lang, goodSamaritan.submitted_by.pk),
    #             "is_disabled": goodSamaritan.is_disabled,
    #             "created": goodSamaritan.created
    #         }
    #         results.append(goodSamaritan_item)
    #     return results

    # def getAllGrantGoodSamaritansNGrantType(self, request, lang, grantId):
    #     results = []
    #     goodSamaritans = GoodSamaritan.objects.filter(Q(is_disabled=False) & Q(getsGrant=True) & Q(grant=grantId)).order_by("id")
    #     for goodSamaritan in goodSamaritans:
    #         goodSamaritan_item = {
    #             "id": goodSamaritan.pk,
    #             "names": goodSamaritan.names,
    #             "phoneNumber": goodSamaritan.phoneNumber,
    #             "BirthDate": goodSamaritan.BirthDate,
    #             "age": self.calculate_age(request, goodSamaritan.BirthDate),
    #             "placeOfResidence": goodSamaritan.placeOfResidence,
    #             "timeOfStay": goodSamaritan.timeOfStay,
    #             "hasDependants": goodSamaritan.hasDependants,
    #             "numberOfDependants": goodSamaritan.numberOfDependants,
    #             "hasNationalID": goodSamaritan.hasNationalID,
    #             "NIN": goodSamaritan.NIN,
    #             "youthHoodBusiness": goodSamaritan.youthHoodBusiness,
    #             "getsGrant": goodSamaritan.getsGrant,
    #             "forHowLong": goodSamaritan.forHowLong,
    #             "howMuch": goodSamaritan.howMuch,
    #             "howItHelpedYou": goodSamaritan.howItHelpedYou,
    #             "BenefitsFromGoodSamaritan": goodSamaritan.BenefitsFromGoodSamaritan,
    #             "grant": self.grants.getGrantById(request, lang, goodSamaritan.grant.pk),
    #             "howDoYouSurvive": goodSamaritan.howDoYouSurvive,
    #             "placeOfWorship": goodSamaritan.placeOfWorship,
    #             "yourNeedFromGovtAsAGrand": goodSamaritan.yourNeedFromGovtAsAGrand,
    #             "adviseToTheYouth": goodSamaritan.adviseToTheYouth,
    #             "submitted_by":  self.users.getAuthUserById(request, lang, goodSamaritan.submitted_by.pk),
    #             "is_disabled": goodSamaritan.is_disabled,
    #             "created": goodSamaritan.created
    #         }
    #         results.append(goodSamaritan_item)
    #     return results

    def GoodSamaritanExists(self, request, lang, goodSamaritanid):
        return GoodSamaritan.objects.filter(pk=int(goodSamaritanid)).exists()

    def getGoodSamaritanById(self, request, lang, goodSamaritanid):
        goodSamaritan = GoodSamaritan.objects.filter(pk=int(goodSamaritanid)).get()
        return {
            "id": goodSamaritan.pk,
            "names": goodSamaritan.names,
            "phoneNumber": goodSamaritan.phoneNumber,
            "BirthDate": goodSamaritan.BirthDate,
            "age": self.calculate_age(request, goodSamaritan.BirthDate),
            "placeOfResidence": goodSamaritan.placeOfResidence,
            "timeOfStay": goodSamaritan.timeOfStay,
            "hasDependants": goodSamaritan.hasDependants,
            "numberOfDependants": goodSamaritan.numberOfDependants,
            "hasNationalID": goodSamaritan.hasNationalID,
            "NIN": goodSamaritan.NIN,
            "youthHoodBusiness": goodSamaritan.youthHoodBusiness,
            "getsGrant": goodSamaritan.getsGrant,
            "forHowLong": goodSamaritan.forHowLong,
            "howMuch": goodSamaritan.howMuch,
            "howItHelpedYou": goodSamaritan.howItHelpedYou,
            "BenefitsFromGoodSamaritan": goodSamaritan.BenefitsFromGoodSamaritan,
            "grant": self.grants.getGrantById(request, lang, goodSamaritan.grant.pk),
            "howDoYouSurvive": goodSamaritan.howDoYouSurvive,
            "placeOfWorship": goodSamaritan.placeOfWorship,
            "yourNeedFromGovtAsAGrand": goodSamaritan.yourNeedFromGovtAsAGrand,
            "adviseToTheYouth": goodSamaritan.adviseToTheYouth,
            "submitted_by": self.users.getAuthUserById(
                request, lang, goodSamaritan.submitted_by.pk
            ),
            "is_disabled": goodSamaritan.is_disabled,
            "created": goodSamaritan.created,
        }

    def createGoodSamaritan(self, request, lang, userid, data):
        goodSamaritan = GoodSamaritan.objects.create(
            names=data["names"],
            phoneNumber=data["phoneNumber"],
            BirthDate=data["BirthDate"],
            placeOfResidence=data["placeOfResidence"],
            timeOfStay=data["timeOfStay"],
            hasDependants=data["hasDependants"],
            numberOfDependants=data["numberOfDependants"],
            hasNationalID=data["hasNationalID"],
            NIN=data["NIN"],
            youthHoodBusiness=data["youthHoodBusiness"],
            getsGrant=data["getsGrant"],
            forHowLong=data["forHowLong"],
            howMuch=data["howMuch"],
            howItHelpedYou=data["howItHelpedYou"],
            BenefitsFromGoodSamaritan=data["BenefitsFromGoodSamaritan"],
            grant=Grant(pk=data["grant"]),
            howDoYouSurvive=data["howDoYouSurvive"],
            placeOfWorship=data["placeOfWorship"],
            yourNeedFromGovtAsAGrand=data["yourNeedFromGovtAsAGrand"],
            adviseToTheYouth=data["adviseToTheYouth"],
            submitted_by=User(pk=userid),
            is_disabled=data["is_disabled"],
        )
        goodSamaritan.save()
        return True

    def updateGoodSamaritan(self, request, lang, data, goodSamaritanid):
        toUpdate = GoodSamaritan.objects.filter(pk=int(goodSamaritanid))
        dbRecToUpdate = toUpdate.get()
        updateRecord_dic = {
            "names": data["names"] if data["names"] else dbRecToUpdate.names,
            "phoneNumber": (
                data["phoneNumber"]
                if data["phoneNumber"]
                else dbRecToUpdate.phoneNumber
            ),
            "BirthDate": (
                data["BirthDate"] if data["BirthDate"] else dbRecToUpdate.BirthDate
            ),
            "placeOfResidence": (
                data["placeOfResidence"]
                if data["placeOfResidence"]
                else dbRecToUpdate.placeOfResidence
            ),
            "timeOfStay": (
                data["timeOfStay"] if data["timeOfStay"] else dbRecToUpdate.timeOfStay
            ),
            "hasDependants": (
                data["hasDependants"]
                if data["hasDependants"]
                else dbRecToUpdate.hasDependants
            ),
            "numberOfDependants": (
                data["numberOfDependants"]
                if data["numberOfDependants"]
                else dbRecToUpdate.numberOfDependants
            ),
            "hasNationalID": (
                data["hasNationalID"]
                if data["hasNationalID"]
                else dbRecToUpdate.hasNationalID
            ),
            "NIN": data["NIN"] if data["NIN"] else dbRecToUpdate.NIN,
            "youthHoodBusiness": (
                data["youthHoodBusiness"]
                if data["youthHoodBusiness"]
                else dbRecToUpdate.youthHoodBusiness
            ),
            "getsGrant": (
                data["getsGrant"] if data["getsGrant"] else dbRecToUpdate.getsGrant
            ),
            "forHowLong": (
                data["forHowLong"] if data["forHowLong"] else dbRecToUpdate.forHowLong
            ),
            "howMuch": data["howMuch"] if data["howMuch"] else dbRecToUpdate.howMuch,
            "howItHelpedYou": (
                data["howItHelpedYou"]
                if data["howItHelpedYou"]
                else dbRecToUpdate.howItHelpedYou
            ),
            "BenefitsFromGoodSamaritan": (
                data["BenefitsFromGoodSamaritan"]
                if data["BenefitsFromGoodSamaritan"]
                else dbRecToUpdate.BenefitsFromGoodSamaritan
            ),
            "grant": data["grant"] if data["grant"] else dbRecToUpdate.grant,
            "howDoYouSurvive": (
                data["howDoYouSurvive"]
                if data["howDoYouSurvive"]
                else dbRecToUpdate.howDoYouSurvive
            ),
            "placeOfWorship": (
                data["placeOfWorship"]
                if data["placeOfWorship"]
                else dbRecToUpdate.placeOfWorship
            ),
            "yourNeedFromGovtAsAGrand": (
                data["yourNeedFromGovtAsAGrand"]
                if data["yourNeedFromGovtAsAGrand"]
                else dbRecToUpdate.yourNeedFromGovtAsAGrand
            ),
            "adviseToTheYouth": (
                data["adviseToTheYouth"]
                if data["adviseToTheYouth"]
                else dbRecToUpdate.adviseToTheYouth
            ),
            "is_disabled": (
                data["is_disabled"]
                if data["is_disabled"]
                else dbRecToUpdate.is_disabled
            ),
        }
        toUpdate.update(**updateRecord_dic)
        return True
