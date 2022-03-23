from typing import List
from typing import Optional

from fastapi import Request


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        self.mobile: Optional[int] = None
        self.username: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None
        self.organization: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.first_name = form.get("first_name")
        self.last_name = form.get("last_name")
        self.mobile = form.get("mobile")
        self.username = form.get("username")
        self.email = form.get("email")
        self.password = form.get("password")
        self.organization = form.get("organization")

    async def is_valid(self):
        if not self.first_name or not len(self.first_name) < 50:
            self.errors.append("first name should be < 50 chars")
        if not self.last_name or not len(self.last_name) < 50:
            self.errors.append("last name should be < 50 chars")
        if not self.mobile or not len(self.mobile) == 10:
            self.errors.append("Mobile number should be 10 chars")
        if not self.username or not len(self.username) > 3:
            self.errors.append("Username should be > 3 chars")
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Email is required")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("Password must be > 4 chars")
        if not self.organization or not len(self.organization) < 100:
            self.errors.append("organization name should be < 100 chars")
        if not self.errors:
            return True
        return False
