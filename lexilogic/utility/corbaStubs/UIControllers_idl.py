# Python stubs generated by omniidl from UIControllers.idl
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


#
# Start of module "org"
#
__name__ = "lexilogic/utility/corbaModules.org"
_0_org = omniORB.openModule("lexilogic/utility/corbaModules.org", r"UIControllers.idl")
_0_org__POA = omniORB.openModule("lexilogic/utility/corbaModules.org__POA", r"UIControllers.idl")


#
# Start of module "org.amalgam"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam"
_0_org.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam", r"UIControllers.idl")
_0_org__POA.amalgam = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam", r"UIControllers.idl")


#
# Start of module "org.amalgam.ControllerException"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam.ControllerException"
_0_org.amalgam.ControllerException = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.ControllerException", r"UIControllers.idl")
_0_org__POA.amalgam.ControllerException = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.ControllerException", r"UIControllers.idl")


# exception InvalidRequestException
_0_org.amalgam.ControllerException.InvalidRequestException = omniORB.newEmptyClass()
class InvalidRequestException (CORBA.UserException):
    _NP_RepositoryId = "IDL:org/amalgam/ControllerException/InvalidRequestException:1.0"

    def __init__(self, message):
        CORBA.UserException.__init__(self, message)
        self.message = message

_0_org.amalgam.ControllerException.InvalidRequestException = InvalidRequestException
_0_org.amalgam.ControllerException._d_InvalidRequestException  = (omniORB.tcInternal.tv_except, InvalidRequestException, InvalidRequestException._NP_RepositoryId, "InvalidRequestException", "message", (omniORB.tcInternal.tv_string,0))
_0_org.amalgam.ControllerException._tc_InvalidRequestException = omniORB.tcInternal.createTypeCode(_0_org.amalgam.ControllerException._d_InvalidRequestException)
omniORB.registerType(InvalidRequestException._NP_RepositoryId, _0_org.amalgam.ControllerException._d_InvalidRequestException, _0_org.amalgam.ControllerException._tc_InvalidRequestException)
del InvalidRequestException

#
# End of module "org.amalgam.ControllerException"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam"


#
# Start of module "org.amalgam.UIControllers"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam.UIControllers"
_0_org.amalgam.UIControllers = omniORB.openModule("lexilogic/utility/corbaModules.org.amalgam.UIControllers", r"UIControllers.idl")
_0_org__POA.amalgam.UIControllers = omniORB.openModule("lexilogic/utility/corbaModules.org__POA.amalgam.UIControllers", r"UIControllers.idl")


# interface PlayerCallback
_0_org.amalgam.UIControllers._d_PlayerCallback = (omniORB.tcInternal.tv_objref, "IDL:org/amalgam/UIControllers/PlayerCallback:1.0", "PlayerCallback")
omniORB.typeMapping["IDL:org/amalgam/UIControllers/PlayerCallback:1.0"] = _0_org.amalgam.UIControllers._d_PlayerCallback
_0_org.amalgam.UIControllers.PlayerCallback = omniORB.newEmptyClass()
class PlayerCallback :
    _NP_RepositoryId = _0_org.amalgam.UIControllers._d_PlayerCallback[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_org.amalgam.UIControllers.PlayerCallback = PlayerCallback
_0_org.amalgam.UIControllers._tc_PlayerCallback = omniORB.tcInternal.createTypeCode(_0_org.amalgam.UIControllers._d_PlayerCallback)
omniORB.registerType(PlayerCallback._NP_RepositoryId, _0_org.amalgam.UIControllers._d_PlayerCallback, _0_org.amalgam.UIControllers._tc_PlayerCallback)

# PlayerCallback operations and attributes
PlayerCallback._d__get_username = ((),((omniORB.tcInternal.tv_string,0),),None)
PlayerCallback._d__set_username = (((omniORB.tcInternal.tv_string,0),),(),None)
PlayerCallback._d_uiCall = (((omniORB.tcInternal.tv_string,0), ), (), {_0_org.amalgam.ControllerException.InvalidRequestException._NP_RepositoryId: _0_org.amalgam.ControllerException._d_InvalidRequestException})

# PlayerCallback object reference
class _objref_PlayerCallback (CORBA.Object):
    _NP_RepositoryId = PlayerCallback._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def _get_username(self, *args):
        return self._obj.invoke("_get_username", _0_org.amalgam.UIControllers.PlayerCallback._d__get_username, args)

    def _set_username(self, *args):
        return self._obj.invoke("_set_username", _0_org.amalgam.UIControllers.PlayerCallback._d__set_username, args)

    username = property(_get_username, _set_username)


    def uiCall(self, *args):
        return self._obj.invoke("uiCall", _0_org.amalgam.UIControllers.PlayerCallback._d_uiCall, args)

omniORB.registerObjref(PlayerCallback._NP_RepositoryId, _objref_PlayerCallback)
_0_org.amalgam.UIControllers._objref_PlayerCallback = _objref_PlayerCallback
del PlayerCallback, _objref_PlayerCallback

# PlayerCallback skeleton
__name__ = "lexilogic/utility/corbaModules.org__POA.amalgam.UIControllers"
class PlayerCallback (PortableServer.Servant):
    _NP_RepositoryId = _0_org.amalgam.UIControllers.PlayerCallback._NP_RepositoryId


    _omni_op_d = {"_get_username": _0_org.amalgam.UIControllers.PlayerCallback._d__get_username, "_set_username": _0_org.amalgam.UIControllers.PlayerCallback._d__set_username, "uiCall": _0_org.amalgam.UIControllers.PlayerCallback._d_uiCall}

PlayerCallback._omni_skeleton = PlayerCallback
_0_org__POA.amalgam.UIControllers.PlayerCallback = PlayerCallback
omniORB.registerSkeleton(PlayerCallback._NP_RepositoryId, PlayerCallback)
del PlayerCallback
__name__ = "lexilogic/utility/corbaModules.org.amalgam.UIControllers"

#
# End of module "org.amalgam.UIControllers"
#
__name__ = "lexilogic/utility/corbaModules.org.amalgam"


#
# End of module "org.amalgam"
#
__name__ = "lexilogic/utility/corbaModules.org"


#
# End of module "org"
#
__name__ = "lexilogic/utility/corbaStubs.UIControllers_idl"

_exported_modules = ( "lexilogic/utility/corbaModules.org", "lexilogic/utility/corbaModules.org.amalgam", "lexilogic/utility/corbaModules.org.amalgam.ControllerException", "lexilogic/utility/corbaModules.org.amalgam.UIControllers")

# The end.
