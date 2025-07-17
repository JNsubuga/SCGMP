import importlib
from pathlib import Path
import os
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from api.core.users import UsersView
from api.core.modules import ModulesView
from api.core.security import SecurityView
from api.core.grants import GrantsView
from api.core.goodSamaritans import GoodSamaritansView

urlpatterns = [
    # Auth
    path("", views.index.as_view(), name="index"),
    path(
        "<str:lang>/auth/login/",
        UsersView.LoginUser.as_view(),
        name="auth-get-user",
    ),
    # GET ALL USERS
    path(
        "<str:lang>/auth/users/",
        UsersView.GetAllUsers.as_view(),
        name="get-auth-users-all",
    ),
    # Token
    path(
        "<str:lang>/auth/user/",
        UsersView.GetAuthUser.as_view(),
        name="get-auth-user-detail",
    ),
    # Token
    path(
        "<str:lang>/auth/user/<int:userid>/",
        UsersView.GetAuthUserById.as_view(),
        name="get-auth-user-details-by-id",
    ),
    #  create User
    path(
        "<str:lang>/auth/user/create/",
        UsersView.CreateAuthUser.as_view(),
        name="auth-create-user",
    ),
    # update user
    path(
        "<str:lang>/auth/user/update/",
        UsersView.UpdateAuthUser.as_view(),
        name="auth-update-user",
    ),
    # update auth user password
    path(
        "<str:lang>/auth/user/<int:userid>/password/update",
        UsersView.UpdateAuthUserPassword.as_view(),
        name="auth-create-user",
    ),
    # # Token
    # path(
    #     "<str:lang>/auth/token/",
    #     UsersView.CreateUserAuthToken.as_view(),
    #     name="auth-create-user-token",
    # ),
    ###########################################
    ########### SECURITY GROUP ###############
    ##########################################
    # SECURITY GROUP
    path(
        "<str:lang>/security/groups/",
        SecurityView.getAllSecurityGroups.as_view(),
        name="get-security-groups",
    ),
    # SECURITY ID
    path(
        "<str:lang>/security/groups/<int:securityid>/",
        SecurityView.getAllSecurityGroupById.as_view(),
        name="get-security-group-by-id",
    ),
    # CREATE NEW SECURITY GROUP
    path(
        "<str:lang>/security/groups/create/",
        SecurityView.CreateSecurityGroup.as_view(),
        name="create-new-security-groups",
    ),
    # UPDATE SECURITY GROUP
    path(
        "<str:lang>/security/groups/<int:securityid>/update/",
        SecurityView.UpdateSecurityGroup.as_view(),
        name="create-new-security-groups",
    ),
    # UPDATE SECURITY GROUP
    path(
        "<str:lang>/security/groups/<int:securityid>/delete/",
        SecurityView.deleteSecurityGroup.as_view(),
        name="delete-security-groups",
    ),
    # GET ALL PERMISSION
    path(
        "<str:lang>/security/permissions/",
        SecurityView.getAllPermissions.as_view(),
        name="get-security-permissions",
    ),
    # GET PERMISSIONS ID
    path(
        "<str:lang>/security/permissions/<int:permissionid>/",
        SecurityView.getPermissionById.as_view(),
        name="get-security-permissions-by-id",
    ),
    ################### USER PERMISSIONS #################
    # GET ALL USER PERMISSIONS
    path(
        "<str:lang>/security/user/permissions/",
        SecurityView.getAllUserPermissions.as_view(),
        name="get-security-user-permissions",
    ),
    # GET USER PERMISSION BY ID
    path(
        "<str:lang>/security/user/permissions/<int:userpermid>/",
        SecurityView.getUserPermissionById.as_view(),
        name="get-security-user-permission-by-id",
    ),
    # GET USER'S PERMISSIONS BY USER ID
    path(
        "<str:lang>/security/user/permissions/",
        SecurityView.getAllUserPermissionsByUserId.as_view(),
        name="get-security-permissions",
    ),
    # GET ALL PERMISSION GIVEN TO USER MIXED WITH THOSE NOT GIVEN
    path(
        "<str:lang>/security/user/permissions/premitive/",
        SecurityView.getPremitiveUserPermissionsByUserId.as_view(),
        name="get-security-permissions",
    ),
    # ADD A SINGLE PERMISSION TO A USER
    path(
        "<str:lang>/security/user/permissions/add/",
        SecurityView.addPermissionToUser.as_view(),
        name="get-security-permissions",
    ),
    # REMOVE A SINGLE PERMISSION TO USER
    path(
        "<str:lang>/security/permission/remove/",
        SecurityView.removePermissionFromUser.as_view(),
        name="get-security-permissions",
    ),
    # ADD A MULTIPLE PERMISSIONS TO A USER
    path(
        "<str:lang>/security/user/permissions/batch/add/",
        SecurityView.addPermissionsToUserInBatch.as_view(),
        name="get-security-permissions",
    ),
    # REMOVE MULTIPLE PERMISSION FROM USER
    path(
        "<str:lang>/security/user/permissions/batch/remove/",
        SecurityView.removePermissionsFromUserInBatch.as_view(),
        name="add-permission-in-batch-to-default",
    ),
    ######################################################
    # CREATE DEFAULT PERMISSIONS FOR CERTAIN USER GROUPS #
    #####################################################
    path(
        "<str:lang>/security/user/group/<int:groupid>/permissions/default/batch/create/",
        SecurityView.addDefaultPermissionsInBatch.as_view(),
        name="get-security-permissions",
    ),
    path(
        "<str:lang>/security/user/group/default/permissions/",
        SecurityView.getAllSecurityGroupPermissions.as_view(),
        name="get-default-group-permissions",
    ),
    path(
        "<str:lang>/security/user/group/<int:groupid>/default/permissions/",
        SecurityView.getAllSecurityGroupPermissionById.as_view(),
        name="get-default-group-permissions",
    ),
    path(
        "<str:lang>/security/user/group/default/permission/batch/delete/",
        SecurityView.removePermissionsFromUserInBatch.as_view(),
        name="delete-default-permission",
    ),
    ####################################################
    # CREATE PERMISSION GROUPS
    path(
        "<str:lang>/security/permissions/groups/create/",
        SecurityView.CreatePermissionGroup.as_view(),
        name="create-permissions-group",
    ),
    # UPDATE PERMISSION GROUPS
    path(
        "<str:lang>/security/permissions/groups/<int:groupid>/update/",
        SecurityView.UpdatePermissionGroup.as_view(),
        name="update-permissions-group",
    ),
    # GET ALL PERMISSION GROUPS
    path(
        "<str:lang>/security/permissions/groups/",
        SecurityView.getAllPermissionGroups.as_view(),
        name="get-all-permission-groups",
    ),
    # CREATE PERMISSION GROUPS
    path(
        "<str:lang>/security/permissions/groups/<int:groupid>/",
        SecurityView.getPermissionGroupById.as_view(),
        name="get-permissions-group-by-id",
    ),
    # DELETE PERMISSION GROUPS
    path(
        "<str:lang>/security/permissions/groups/<int:groupid>/delete/",
        SecurityView.DeletePermission.as_view(),
        name="delete-permissions-group",
    ),
    # GROUPED PERMISSIONS
    # ADD A SINGLE PERMISSION TO A GROUP
    path(
        "<str:lang>/security/permissions/groups/<int:groupid>/permissions/create/",
        SecurityView.addPermissionToGroup.as_view(),
        name="add-permission-to-group",
    ),
    # ADD A BATCH PERMISSION TO A GROUP
    path(
        "<str:lang>/security/permissions/groups/<int:groupid>/permissions/batch/create/",
        SecurityView.addPermissionsToGroupInBatch.as_view(),
        name="add-batch-permission-to-group",
    ),
    path(
        "<str:lang>/security/groups/<int:groupid>/permissions/batch/delete/",
        SecurityView.removePermissionsFromGroupInBatch.as_view(),
        name="add-batch-permission-to-group",
    ),
    path(
        "<str:lang>/security/groups/default/permissions/batch/delete/",
        SecurityView.removeDefaultPermissionsInBatch.as_view(),
        name="delete-a-batch-permissions-group",
    ),
    # GET PERMISSIONS BY GROUP
    path(
        "<str:lang>/security/permissions/groups/all/",
        SecurityView.getAllPermissionsByGroups.as_view(),
        name="get-all-permission-groups",
    ),
    # GET PERMISSIONS IN GROUP
    path(
        "<str:lang>/security/permissions/groups/<int:groupid>/all/",
        SecurityView.getPermissionsByGroupId.as_view(),
        name="get-all-permissions-in-group",
    ),
    # Modules
    path(
        "<str:lang>/modules/getall/",
        ModulesView.getAllModules.as_view(),
        name="get-all-modules",
    ),
    # Get main modules and there sub modules
    path(
        "<str:lang>/modules/getmainmodules/",
        ModulesView.getMainModules.as_view(),
        name="get-main-modules",
    ),
    # Get module By Id
    path(
        "<str:lang>/modules/getmodule/<int:moduleid>/",
        ModulesView.getModuleById.as_view(),
        name="get-module-by-id",
    ),
    # Update module
    path(
        "<str:lang>/modules/updatemodule/<int:moduleid>/",
        ModulesView.UpdateModule.as_view(),
        name="update-module",
    ),
    # Get submodule
    path(
        "<str:lang>/modules/getsubmodules/<int:moduleid>/",
        ModulesView.GetSubModules.as_view(),
        name="get-sub-modules",
    ),
    # Disable module
    path(
        "<str:lang>/modules/disablemodule/<int:moduleid>/",
        ModulesView.DisableModules.as_view(),
        name="disable-enable-modules",
    ),
    # Get Menu
    # Get Side Menu Modules
    path(
        "<str:lang>/modules/getsidemenumodules/",
        ModulesView.getSideMenuModules.as_view(),
        name="get-sidemenu-modules",
    ),
    # Dashboard menu
    path(
        "<str:lang>/modules/getdashboardmodules/",
        ModulesView.getDashboardMenu.as_view(),
        name="get-dashboard-menu",
    ),
    # TENDERING (GRANTS)
    # GRANT ROUTES
    #############################################
    # Get All Grants
    path(
        "<str:lang>/scgmp/grants/",
        GrantsView.getAllGrants.as_view(),
        name="get-all-grants"
    ),
    # Get Grnat By Id
    path(
        "<str:lang>/scgmp/grant/<int:grantid>",
        GrantsView.getGrantById.as_view(),
        name="get-grant-by-id"
    ),
    # Create Grant
    path(
        "<str:lang>/scgmp/register/grant",
        GrantsView.createGrant.as_view(),
        name="register-grant"
    ),
    # Update Grant
    path(
        "<str:lang>/scgmp/update/grant/<int:grantid>",
        GrantsView.updateGrant.as_view(),
        name="update-grant"
    ),
# TENDERING (GOODSAMARITANS)
    # GOODSAMARITAN ROUTES
    #############################################
    # Get All GoodSamaritans
    path(
        "<str:lang>/scgmp/good-samaritans/",
        GoodSamaritansView.getAllGoodSamaritans.as_view(),
        name="get-all-goodsamaritans"
    ),
    # # Get All Granted GoodSamaritans
    # path(
    #     "<str:lang>/scgmp/grant-good-samaritans/",
    #     GoodSamaritansView.getAllGrantGoodSamaritans.as_view(),
    #     name="get-all-granted-goodsamaritans"
    # ),
    # # Get All Granted GoodSamaritans with grant type
    # path(
    #     "<str:lang>/scgmp/grant-good-samaritans-grant-type/<int:grantId>",
    #     GoodSamaritansView.getAllGrantGoodSamaritansNGrantType.as_view(),
    #     name="grant-get-all-goodsamaritans-grant-type"
    # ),
    # Get Good Samaritan By Id
    path(
        "<str:lang>/scgmp/good-samaritan/<int:goodsamaritanid>",
        GoodSamaritansView.getGoodSamaritanById.as_view(),
        name="get-good-samaritan-by-id"
    ),
    # Create Good Samaritan
    path(
        "<str:lang>/scgmp/create/goodsamaritan/",
        GoodSamaritansView.createGoodSamaritan.as_view(),
        name="register-good-samaritan"
    ),
    # Update Good Samaritan
    path(
        "<str:lang>/scgmp/update/goodsamaritan/<int:goodSamaritanid>",
        GoodSamaritansView.updateGoodSamaritan.as_view(),
        name="update-grant"
    )
]
urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)