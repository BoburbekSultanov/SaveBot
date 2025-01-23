from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from db import db
from db.modles import Category, Image, Video, Document, Other, MyEnum
from web.provider import UsernameAndPasswordProvider

app = Starlette()
admin = Admin(db._engine,
              title="SaveBot Admin",
              base_url= "/",
              auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key="sdgfhjhhsfdghn")]
              )

admin.add_view(ModelView(Category))
admin.add_view(ModelView(Image))
admin.add_view(ModelView(Video))
admin.add_view(ModelView(Document))
admin.add_view(ModelView(Other))
admin.add_view(ModelView(MyEnum))

admin.mount_to(app)



