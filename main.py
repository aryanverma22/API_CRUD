from Users.controller.Runuser import app as users
from Posts.controller.Runposts import app as posts

if __name__ == '__main__':
    # users.run(port=3600,debug=True)
    posts.run(port=300,debug= True)