import webapp2

from model_post import *
from model_user import *
from model_like import *
from model_comment import *


from controller_post import *
from controller_user import *
from controller_edit import *
from controller_like import *
from controller_drop import *
from controller_comment import *
from controller_comment_edit import *
from controller_comment_drop import *
from handler import *


                              #Route
app = webapp2.WSGIApplication([('/', MainPage),  ##welcome.html extrend base.html
                               ('/signup', Signup),  ##signup-form.html
                               ('/login', Login),  ##login-form.html
                               ('/logout', Logout),  ##index.html
                               ('/newpost', NewPost),  ##newpost.html
                               ('/([0-9]+)', PostPage),  ##permalink.html
                               ('/([0-9]+)/like', LikePost),
                               ('/([0-9]+)/edit', Edit),  ##edit.html
                               ('/([0-9]+)/delete', DropPost),
                               ('/([0-9]+)/comment/([0-9]+)', CommentPost),  ##after_comment
                               ('/([0-9]+)/comment/([0-9]+)/edit/([0-9]+)', CommentEdit),
                               ('/([0-9]+)/comment/([0-9]+)/delete/([0-9]+)', CommentDrop)
                               ],
                              debug=True)   #never "deploy" an application with debug_mode=True
