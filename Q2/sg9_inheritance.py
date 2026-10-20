class Publication: #nagddefine ng parent class para sa publication
    def __init__(self, title, author): #nagddefine ng function para mag accept ng title at author
        self.title = title
        self.author = author
    def get_title(self): #nagddefine ng method para kunin yung title
        print(f'Title: {self.title}') #tigpprint yung title
        return self.title #return yung title 
    def get_author(self): #nagddefine ng method para kunin yung author name
        print(f'Author: {self.author}') #tigpprint yung author name
        return self.author #return yung author name
    def set_title(self, new_title): #nagddefine ng method para maupdate yung title ng publication
        self.title = new_title #nagaassign ng new titel sa title
        return self.title #tigrreturn yung updated title 
    def set_author(self, new_author): #nagddefine ng method para iupdate yung author name
        self.author = new_author #nagaassign ng new author name sa author
        return self.author #tigrreturn yung updated author name
    def display_info(self): #nagddefine ng method para idisplay yung publication details
        print(f'Title: {self.title} \nAuthor: {self.author}') #tigpprint yung title and author name sa bagong line

class Book(Publication): #nagddefine ng subclass para sa book
    def __init__(self, title, author, number_of_pages): #nagddefine ng function para mag accept ng title, author, at number of pages
        super().__init__(title, author) #call yung parent class para ma set yung title at author
        self.number_of_pages = number_of_pages #tigsstore yung total page count sa number_of_pages
    def get_number_of_pages(self): #nagddefine ng method para kunin yung page count
        return self.number_of_pages #return yung number_of_pages
    def set_number_of_pages(self, new_page_count): # nagddefine ng method para iupdate yung page count
        if new_page_count > 0: #tigccheck if negative o positibe yung page count
            self.number_of_pages = new_page_count #inuupdate yung total pages if positibe yung new page count
            return self.number_of_pages #tigrreturn yung bagong page count
        else: #else
            print("The number of pages must be positive") #nagpprint ng syntax error message
    def display_info(self): #nagddefine ng method para maedit yung details ng Book class
        print(f'Title: {self.title} \nAuthor: {self.author} \nNumber of pages: {self.number_of_pages}')#tigpprint yung title, author, at number of pages

class Magazine(Publication): #nagddefine ng bagong subclass para sa Magazine
    def __init__(self, title, author, issue_number): #nagddefine function para mag accept ng title, author, at issue number
        super().__init__(title, author) #call yung parent class para ma set yung title and author
        self.issue_number = issue_number #tigsstore yung issue number sa issue_number
    def get_issue_number(self): #nagddefine ng method para kunin yung issue number
        return self.issue_number #tigrreturn yung issue number
    def set_issue_number(self, new_issue_number): #nagddefine ng method para iupdate yung yung issue number
        if new_issue_number > 0: #tigccheck kung negative yung issue number
            self.issue_number = new_issue_number #tiguupdate yung issue number if positive 
            return self.issue_number #tigrreturn yung updated issue number
        else: #else
            print("The issue number must be positive") #nagpprint ng syntax error message
    def display_info(self): #nagddegfine ng method para maedit yung info sa magazine
        print(f'Title: {self.title} \nAuthor: {self.author} \nIssue number: {self.issue_number}') #tigpprint yung title, author, at issue number.
      
paper_entry = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") #nagaassign ng mga titles and authors
novel_entry = Book("The Hobbit", "J.R.R. Tolkien", 310) #nagaassign ng titles, authors, and pages
periodical_entry = Magazine("National Geographic", "Various Authors", 202) #nagaassign ng title, authors at issue number

print("Publication Information:") #nagpprint ng label para sa publication information
paper_entry.display_info() #tigccall yung display_info at paper_entry para iprint

print("\nBook Information:") #nagpprint ng label para sa book information
novel_entry.set_number_of_pages(-310) #tigccall yung set_number_of_pages na may negative na count para iprint yung syntax error output
novel_entry.display_info() #tigpprint yung details ng class Book

print("\nMagazine Information:")#tigpprint yung label ng Magazine Information
periodical_entry.display_info() #tigccall yung display_info sa periodical_entry para iprint yung details
