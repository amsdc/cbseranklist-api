from app.api import bp
from app.api.endpoints import auth as e_auth
from app.api.endpoints import school as e_school

bp.add_url_rule("/auth/login", view_func=e_auth.Login.as_view("login"))
# bp.add_url_rule("/auth/register", view_func=e_auth.RegistrationGUI.as_view("register_gui"))

bp.add_url_rule("/users/me", view_func=e_auth.MeUser.as_view("me_user"))
bp.add_url_rule("/users/me/preferences/<string:key>", view_func=e_auth.UserPreferences.as_view("userprefs"))