from apis.version1 import route_login
from apis.version1 import route_users, route_vendor, route_vendorcompany, route_view_user, route_update_user_info, route_edit_vendor_info, route_vendor_login
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["Create User"])
api_router.include_router(route_login.router, prefix="/login", tags=["User Login"])
api_router.include_router(route_vendor.router, prefix="/vendor/register", tags=["Vendor Register"])
api_router.include_router(route_vendor_login.router, prefix="/vendor/login", tags=["Vendor Login"])
api_router.include_router(route_vendorcompany.router, prefix="/vendorcompany", tags=["Vendor Company Register"])
api_router.include_router(route_view_user.router, prefix="/user", tags=["Show user"])
api_router.include_router(route_update_user_info.router, prefix="/updateuser", tags=["Update User Info"])
api_router.include_router(route_edit_vendor_info.router, prefix="/vendor", tags=["Update Vendor Info"])