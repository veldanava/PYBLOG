from venv import create
import pymongo
import datetime
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

# env
client = MongoClient('mongodb+srv://@.mongodb.net/')
db = client.kiana
collection = db.test_collection
posts = db.posts

print('''
 ▄▄▄· ▄· ▄▌▄▄▄▄· ▄▄▌         ▄▄ • 
▐█ ▄█▐█▪██▌▐█ ▀█▪██•  ▪     ▐█ ▀ ▪
 ██▀·▐█▌▐█▪▐█▀▀█▄██▪   ▄█▀▄ ▄█ ▀█▄
▐█▪·• ▐█▀·.██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█▄▪▐█
.▀     ▀ • ·▀▀▀▀ .▀▀▀  ▀█▄▀▪·▀▀▀▀ 
coded by kiana - github.com/veldanava
''')

# create
def createPost(posts):
  print("\nCreate Post")
  authorFirstName = input("Enter author first name>> ")
  authorLastName =  input("Enter author last name>> ")
  postTitle = input("Enter post title>> ")
  postBody = input("Enter post body>> ")
  
  post = {"author first name": authorFirstName, "author last name": authorLastName, "title": postTitle, "text": postBody, "date": datetime.datetime.utcnow()}
  
  print(post)
  post_id = posts.insert_one(post).inserted_id

  print("Post successful!")

# read
def readPost(posts):
  print("\nRead")
  print("1 >> Read by author first name")
  print("2 >> Read by author last name")
  print("3 >> Read by post title")
  print("4 >> Exit Read")

  readChoice = input("uwu>>  ")
  
  while readChoice != "4":
    if readChoice == "1":
      authorFirstName = input("Enter author first name>>  ")
      pprint.pprint(posts.find_one({"author first name": authorFirstName}))
      break
    if readChoice == "2":
      authorLastName = input("Enter author last name>>  ")
      pprint.pprint(posts.find_one({"author last name": authorLastName}))
      break
    if readChoice == "3":
      postTitle = input("Enter post title>> ")
      pprint.pprint(posts.find_one({"title": postTitle}))
      break
    elif readChoice == "4":
      break
    
# update
def updatePost(posts):
  print("\nUpdate")
    
  print("1 >> Update by author first name")
  print("2 >> Update by author last name")
  print("3 >> Update by post title")
  print("4 >> Exit Update")

  updateChoice = input("uwu>>  ")
  
  while updateChoice != "4":
    if updateChoice == "1":
      authorFirstName = input("Enter author first name>>  ")
      post = posts.find_one({"author first name": authorFirstName})
      pprint.pprint(post)
      post_id = post["_id"]
      print("post_id: " + str(post_id))
      updateByPostID(post, post_id)
      break
    if updateChoice == "2":
      authorLastName = input("Enter author last name>>  ")
      post = posts.find_one({"author last name": authorLastName})
      pprint.pprint(post)
      post_id = post["_id"]
      print("post_id: " + str(post_id))
      updateByPostID(post, post_id)
      break
    if updateChoice == "3":
      postTitle = input("Enter post title>> ")
      post = posts.find_one({"title": postTitle})
      pprint.pprint(post)
      post_id = post["_id"]
      print("post_id: " + str(post_id))
      updateByPostID(post, post_id)
      break
    elif updateChoice == "4":
      break
    
# update by post
def updateByPostID(post, post_id):
  
  updatePost = ""
  while ((updatePost != "Y") or (updatePost != "n")):
    updatePost = "n"
    updatePost = input("Update this post [Y/n]? Default is [n].")
    if updatePost == "n":
      break
    else:
      print("1 >> Update author first name")
      print("2 >> Update author last name")
      print("3 >> Update post title")
      print("4 >> Update post body")
      print("5 >> Exit Update")
      
      selection = input("uwu>>  ")
      
      while selection != "5":
        if selection == "1":
          authorFirstName = input("Enter new author first name: ")
          posts.update_one({"_id": post_id}, { "$set": {"author first name": authorFirstName}})
          post = posts.find_one({"author first name": authorFirstName})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "2":
          authorLastName = input("Enter new author last name: ")
          posts.update_one({"_id": post_id}, { "$set": {"author last name": authorLastName}})
          post = posts.find_one({"author last name": authorFirstName})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "3":
          postTitle = input("Enter new post title: ")
          posts.update_one({"_id": post_id}, { "$set": {"title": postTitle}})
          post = posts.find_one({"title": postTitle})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "4":
          postBody = input("Enter new post body: ")
          posts.update_one({"_id": post_id}, { "$set": {"text": postBody}})
          post = posts.find_one({"text": postBody})
          pprint.pprint(post)
          print("Update successful.")
          break
        elif selection == "5":
          break
      break
    break

# give some change
def doStuff(db, collection, posts):
  choice = 0
  while choice != 5:
    print("\nWelcome to PYBLOG, ur admin bruh")
    print("1 >> Create Post")
    print("2 >> Read Post")
    print("3 >> Update Post")
    print("4 >> Delete Post")
    print("5 >> Exit")
    
    choice = input()
    if choice == "1":
      createPost(posts)
    elif choice == "2":
      readPost(posts)
    elif choice == "3":
      updatePost(posts)
    elif choice == "4":
      print("\nDelete")
    elif choice == "5":
      print("\nExit")
      dropDatabase = "n"
      dropDatabase = input("Drop database kiana [Y/n]? Default is [n] ")
      if dropDatabase == "Y":
        client.drop_database('kiana')
      break

doStuff(db, collection, posts)
