from apis.version1 import route_login
from apis.version1 import route_post, route_category_attribute, route_category
from apis.version1 import route_users, route_vendor, route_vendorcompany, route_vendor_login, route_public_contact
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["User"])
api_router.include_router(route_login.router, prefix="/login", tags=["User Login"])
api_router.include_router(route_vendor.router, prefix="/vendor", tags=["Vendor"])
api_router.include_router(route_vendor_login.router, prefix="/vendor/login", tags=["Vendor Login"])
api_router.include_router(route_vendorcompany.router, prefix="/vendorcompany", tags=["Vendor Company"])
api_router.include_router(route_public_contact.router, prefix="/pcw", tags=["Public Contact Window"])
api_router.include_router(route_post.router, prefix="/createpost", tags=["Product"])
api_router.include_router(route_category.router, prefix="/category", tags=["Category"])
api_router.include_router(route_category_attribute.router, prefix="/categoryattr", tags=["Category Attribute"])
