
class Library:

    def __init__(self, list):
        self.list = list  # dynamic list

        self.list1 = self.list.copy()

    def booklist(self):
        print("*****BOOK LIST*****")
        for item in self.list:
            print(" - " + item)
        return ""

    def borrowbook(self, bookname):
        if (bookname in self.list):
            self.list.remove(bookname)
            return f"you take the {bookname} book from the jp's library!! please return the book in 30 days."
        else:
            return"the book is not avaible in the libarary"

    def returnbook(self, bookname):
        if (bookname in self.list1):
            self.list.append(bookname)
            return "Thank you for the return the book!! Have a Great day.."
        else:
            return"You don't take this book from this library"

    def addbook(self, bookname):
        self.list.append(bookname)
        return f"You successfully add the {bookname} in this library!!"

    def removebook(self, bookname):
        if (bookname in self.list):
            self.list.remove(bookname)
            return f"you remove the {bookname} book from the jp's library!! "
        else:
            return"the book is not avaible in the libarary"


class Student:

    def reqbook(self):
        self.name = input("please enter the book name you request::")
        return self.name

    def retbook(self):
        self.name = input("please enter the book name you return::")
        return self.name


class Libirian:

    def addbook(self):
        self.name = input("Please enter the book name you add::")
        return self.name

    def removebook(self):
        self.name = input("please enter the book name you remove::")
        return self.name


book_list = ["the nun", "jaguar", "ramayan", "mahabhrat", "jungle book"]
l = Library(book_list)
student = Student()
libirian = Libirian()


welmsg1 = '''\n*****Welcome to the Jp 's Library*****
Enter The Roll
1.Administor
2.User
3.exit'''


def intro():

    print(welmsg1)
    global b
    b = input("Enter Your Roll::")
    try:
        b = int(b)
        return b
    except:
        print("**********WARNING:: ENTER THE ONLY INTEGER NUMBER FOR CHOICE**********")
        return intro()


j = intro()
if(j == 1):
    while(True):
        passworddefault = "jp@1234"
        password1 = input("Enter Your Password!!")
        if (password1 == passworddefault):

            welmsg = '''\n*****Welcome to the Jp's library*****
            Enter the choice
            1.Show The List
            2.Add  The Book
            3.Delete The Book
            4.exit'''
            while(True):
                print(welmsg)
                choice = input("Please Enter The Choice::")
                try:
                    choice = int(choice)
                except:
                    print(
                        "**********WARNING:: ENTER THE ONLY INTEGER NUMBER FOR CHOICE**********")
                if(choice == 1):
                    print(l.booklist())
                elif(choice == 2):
                    print(l.addbook(libirian.addbook()))
                elif(choice == 3):
                    print(l.removebook(libirian.removebook()))
                elif(choice == 4):
                    print("\nThanks for the using the jp's Library!!")
                    exit()

                else:
                    print("\nGive The Valid Choice!!")
        else:
            print("WARNING:::PASSWORD IS INCORRECT!!! TRY AGAIN")

elif(j == 2):
    welmsg = '''\n******Welcome to the Jp's library******
        Enter the choice 
        1.Show The List
        2.Borrow The Book
        3.Return a Book
        4.Quit'''
    while(True):
        print(welmsg)
        choice = input("Please Enter The Choice::")
        try:
            choice = int(choice)
        except:
            print(
                "**********WARNING:: ENTER THE ONLY INTEGER NUMBER FOR CHOICE**********")
        if(choice == 1):
            print(l.booklist())
        elif(choice == 2):
            print(l.borrowbook(student.reqbook()))
        elif(choice == 3):
            print(l.returnbook(student.retbook()))
        elif(choice == 4):
            exit()

        else:
            print("\nGive The Valid Choice!!")

elif (j == 3):
    print("\nThanks for the using the jp's Library!!")
    exit()

else:
    print("\n Give The valid Roll")
