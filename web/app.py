from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from db import db
from db.modles import User, Customer, Post, Job, Subjob, Employee, PostSubjob, SubjobEmployee
from web.provider import UsernameAndPasswordProvider

app = Starlette()
admin = Admin(db._engine,
              title="Kwork Admin",
              base_url= "/",
              auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key="sdgfhjhhsfdghn")]
              )

admin.add_view(ModelView(User))
admin.add_view(ModelView(Customer))
admin.add_view(ModelView(Post))
admin.add_view(ModelView(Job))
admin.add_view(ModelView(Subjob))
admin.add_view(ModelView(Employee))
admin.add_view(ModelView(PostSubjob))
admin.add_view(ModelView(SubjobEmployee))

admin.mount_to(app)



