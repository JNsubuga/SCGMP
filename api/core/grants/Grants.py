from api.core.helper import helper
from api.models import *

from api.core.users.Users import Users
from api.core.locale.Locale import Locale


class Grants:
    def __init__(self):
        self.users = Users()

    def getAllGrants(self, request, lang):
        results = []
        grants = Grant.objects.filter(is_disabled=False).order_by("id")
        for grant in grants:
            grant_item = {
                "id": grant.pk,
                "GrantName": grant.GrantName,
                "GrantAbriviation":grant.GrantAbriviation,
                "submitted_by": self.users.getAuthUserById(request, lang, grant.submitted_by.pk),
                "is_disabled": grant.is_disabled,
                "created": grant.created
            }
            results.append(grant_item)
        return results
    
    def GrantExists(self, request, lang, grantid):
        return Grant.objects.filter(pk=int(grantid)).exists()
    
    def getGrantById(self, request, lang, grantid):
        grant = Grant.objects.filter(pk=int(grantid)).get()
        return {
            "id": grant.pk,
            "GrantName": grant.GrantName,
            "GrantAbriviation":grant.GrantAbriviation,
            "submitted_by": self.users.getAuthUserById(request, lang, grant.submitted_by.pk),
            "is_disabled": grant.is_disabled,
            "created": grant.created
        }
        
    def createGrant(self, request, lang, userid, data):
        grant = Grant.objects.create(
            GrantName = data["GrantName"],
            GrantAbriviation = data["GrantAbriviation"],
            submitted_by = User(pk=userid),
            is_disabled = data["is_disabled"]
        )    
        grant.save()
        return True
    
    def updateGrant(self, request, lang, grantid, data):
        toUpdate = Grant.objects.filter(pk=int(grantid))
        dbRecToUpdate = toUpdate.get()
        updateRecord_dic = {
            "GrantName":(data["GrantName"] if data["GrantName"] else dbRecToUpdate.GrantName),
            "GrantAbriviation":(data["GrantAbriviation"] if data["GrantAbriviation"] else dbRecToUpdate.GrantAbriviation),
            "is_disabled":(data["is_disabled"] if data["is_disabled"] else dbRecToUpdate.is_disabled)
        }
        toUpdate.update(**updateRecord_dic)
        return True