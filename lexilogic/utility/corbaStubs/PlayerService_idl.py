# Python stubs generated by omniidl from PlayerService.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


# #include "ProgramUtilities.idl"
import lexilogic.utility.corbaStubs.ProgramUtilities_idl
_0_org = omniORB.openModule("lexilogic/utility/corbaModules.org")
_0_org__POA = omniORB.openModule("lexilogic/utility/corbaModules.org__POA")
_0_org.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam")
_0_org__POA.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam")
_0_org.amalgam.Utils = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.Utils")
_0_org__POA.amalgam.Utils = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.Utils")
_0_org.amalgam.Utils.Exceptions = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.Utils.Exceptions")
_0_org__POA.amalgam.Utils.Exceptions = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.Utils.Exceptions")

# #include "UIControllers.idl"
import lexilogic/utility/corbaStubs.UIControllers_idl
_0_org = omniORB.openModule("lexilogic/utility/corbaModules.org")
_0_org__POA = omniORB.openModule("lexilogic/utility/corbaModules.org__POA")
_0_org.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam")
_0_org__POA.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam")
_0_org.amalgam.ControllerException = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.ControllerException")
_0_org__POA.amalgam.ControllerException = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.ControllerException")
_0_org.amalgam.UIControllers = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.UIControllers")
_0_org__POA.amalgam.UIControllers = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.UIControllers")

#
# Start of module "org"
#
__name__ = "lexilogic/utility/corbaModules.org"
_0_org = omniORB.openModule("lexilogic/utility/corbaModules.org", r"PlayerService.idl")
_0_org__POA = omniORB.openModule("lexilogic/utility/corbaModules.org__POA", r"PlayerService.idl")


#
# Start of module "org.amalgam"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam"
_0_org.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam", r"PlayerService.idl")
_0_org__POA.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam", r"PlayerService.idl")


#
# Start of module "org.amalgam.Service"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam.Service"
_0_org.amalgam.Service = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.Service", r"PlayerService.idl")
_0_org__POA.amalgam.Service = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.Service", r"PlayerService.idl")


#
# Start of module "org.amalgam.Service.PlayerServiceModule"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam.Service.PlayerServiceModule"
_0_org.amalgam.Service.PlayerServiceModule = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.Service.PlayerServiceModule", r"PlayerService.idl")
_0_org__POA.amalgam.Service.PlayerServiceModule = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.Service.PlayerServiceModule", r"PlayerService.idl")


# interface PlayerService
_0_org.amalgam.Service.PlayerServiceModule._d_PlayerService = (omniORB.tcInternal.tv_objref, "IDL:org/amalgam/Service/PlayerServiceModule/PlayerService:1.0", "PlayerService")
omniORB.typeMapping["IDL:org/amalgam/Service/PlayerServiceModule/PlayerService:1.0"] = _0_org.amalgam.Service.PlayerServiceModule._d_PlayerService
_0_org.amalgam.Service.PlayerServiceModule.PlayerService = omniORB.newEmptyClass()
class PlayerService :
    _NP_RepositoryId = _0_org.amalgam.Service.PlayerServiceModule._d_PlayerService[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # typedef ... PlayerCallback
    class PlayerCallback:
        _NP_RepositoryId = "IDL:org/amalgam/Service/PlayerServiceModule/PlayerService/PlayerCallback:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_PlayerCallback  = omniORB.typeMapping["IDL:org/amalgam/UIControllers/PlayerCallback:1.0"]
    _ad_PlayerCallback = (omniORB.tcInternal.tv_alias, PlayerCallback._NP_RepositoryId, "PlayerCallback", omniORB.typeMapping["IDL:org/amalgam/UIControllers/PlayerCallback:1.0"])
    _tc_PlayerCallback = omniORB.tcInternal.createTypeCode(_ad_PlayerCallback)
    omniORB.registerType(PlayerCallback._NP_RepositoryId, _ad_PlayerCallback, _tc_PlayerCallback)


_0_org.amalgam.Service.PlayerServiceModule.PlayerService = PlayerService
_0_org.amalgam.Service.PlayerServiceModule._tc_PlayerService = omniORB.tcInternal.createTypeCode(_0_org.amalgam.Service.PlayerServiceModule._d_PlayerService)
omniORB.registerType(PlayerService._NP_RepositoryId, _0_org.amalgam.Service.PlayerServiceModule._d_PlayerService, _0_org.amalgam.Service.PlayerServiceModule._tc_PlayerService)

# PlayerService operations and attributes
PlayerService._d_login = ((omniORB.typeMapping["IDL:org/amalgam/Service/PlayerServiceModule/PlayerService/PlayerCallback:1.0"], (omniORB.tcInternal.tv_string,0)), (), {_0_org.amalgam.Utils.Exceptions.AlreadyLoggedInException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_AlreadyLoggedInException, _0_org.amalgam.Utils.Exceptions.InvalidCredentialsException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_InvalidCredentialsException, _0_org.amalgam.Utils.Exceptions.UserExistenceException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_UserExistenceException})
PlayerService._d_logout = (((omniORB.tcInternal.tv_string,0), ), (), {_0_org.amalgam.Utils.Exceptions.NotLoggedInException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_NotLoggedInException})
PlayerService._d_createAccount = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), {_0_org.amalgam.Utils.Exceptions.AccountCreationFailedException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_AccountCreationFailedException})
PlayerService._d_changeUsername = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), {_0_org.amalgam.Utils.Exceptions.ChangeUsernameFailedException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_ChangeUsernameFailedException})
PlayerService._d_changePassword = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), {_0_org.amalgam.Utils.Exceptions.ChangePasswordFailedException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_ChangePasswordFailedException})
PlayerService._d_accountDeletionRequest = (((omniORB.tcInternal.tv_string,0), ), (), {_0_org.amalgam.Utils.Exceptions.DeleteAccountFailedException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_DeleteAccountFailedException})
PlayerService._d_getGameHistory = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), {_0_org.amalgam.Utils.Exceptions.GameHistoryUnavailableException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_GameHistoryUnavailableException, _0_org.amalgam.Utils.Exceptions.InGameException._NP_RepositoryId: _0_org.amalgam.Utils.Exceptions._d_InGameException})

# PlayerService object reference
class _objref_PlayerService (CORBA.Object):
    _NP_RepositoryId = PlayerService._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def login(self, *args):
        return self._obj.invoke("login", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_login, args)

    def logout(self, *args):
        return self._obj.invoke("logout", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_logout, args)

    def createAccount(self, *args):
        return self._obj.invoke("createAccount", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_createAccount, args)

    def changeUsername(self, *args):
        return self._obj.invoke("changeUsername", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_changeUsername, args)

    def changePassword(self, *args):
        return self._obj.invoke("changePassword", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_changePassword, args)

    def accountDeletionRequest(self, *args):
        return self._obj.invoke("accountDeletionRequest", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_accountDeletionRequest, args)

    def getGameHistory(self, *args):
        return self._obj.invoke("getGameHistory", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_getGameHistory, args)

omniORB.registerObjref(PlayerService._NP_RepositoryId, _objref_PlayerService)
_0_org.amalgam.Service.PlayerServiceModule._objref_PlayerService = _objref_PlayerService
del PlayerService, _objref_PlayerService

# PlayerService skeleton
__name__ = "lexilogic/utility/corbaModules.org__POA.amalgam.Service.PlayerServiceModule"
class PlayerService (PortableServer.Servant):
    _NP_RepositoryId = _0_org.amalgam.Service.PlayerServiceModule.PlayerService._NP_RepositoryId


    _omni_op_d = {"login": _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_login, "logout": _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_logout, "createAccount": _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_createAccount, "changeUsername": _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_changeUsername, "changePassword": _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_changePassword, "accountDeletionRequest": _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_accountDeletionRequest, "getGameHistory": _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_getGameHistory}

PlayerService._omni_skeleton = PlayerService
_0_org__POA.amalgam.Service.PlayerServiceModule.PlayerService = PlayerService
omniORB.registerSkeleton(PlayerService._NP_RepositoryId, PlayerService)
del PlayerService
__name__ = "lexilogic/utility/corbaModules.org.amalgam.Service.PlayerServiceModule"

#
# End of module "org.amalgam.Service.PlayerServiceModule"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam.Service"


#
# End of module "org.amalgam.Service"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam"


#
# End of module "org.amalgam"
#
__name__ = "lexilogic/utility/corbaModules.org"


#
# End of module "org"
#
__name__ = "lexilogic/utility/corbaStubs.PlayerService_idl"

_exported_modules = ( "lexilogic/utility/corbaModules.org", "lexilogic/utility/corbaModules.org.amalgam", "lexilogic/utility/corbaModules.org.amalgam.Service", "lexilogic/utility/corbaModules.org.amalgam.Service.PlayerServiceModule")

# The end.
