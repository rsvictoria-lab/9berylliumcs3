class Publication: #nagddefine ng parent class para sa publication
    def __init__(self, item_title, creator_name): #nagddefine ng function para mag accept ng title at creator name
        self.item_title = item_title
        self.creator_name = creator_name
    def get_title(self): #nagddefine ng method para kunin yung title
        print(f'Title: {self.item_title}') #tigpprint yung title
        return self.item_title #return yung title 
    def get_author(self): #nagddefine ng method para kunin yung author name
        print(f'Author: {self.creator_name}') #tigpprint yung author name
        return self.creator_name #return yung author name
    def set_title(self, new_title): #nagddefine ng method para maupdate yung title ng publication
        self.item_title = new_title #nagaassign ng new titel sa item_title
        return self.item_title #tigrreturn yung updated title 
    def set_author(self, new_author): #nagddefine ng method para iupdate yung author name
        self.creator_name = new_author #nagaassign ng new author name sa creator_name
        return self.creator_name #tigrreturn yung updated author name
    def display_info(self): #nagddefine ng method para idisplay yung publication details
        print(f'Title: {self.item_title} \nAuthor: {self.creator_name}') #tigpprint yung title and author name sa bagong line

class Book(Publication): #nagddefine ng subclass para sa book
    def __init__(self, item_title, creator_name, total_pages): #nagddefine ng function para mag accept ng title, creator name, at total pages
        super().__init__(item_title, creator_name) #call yung parent class para ma set yung item_title at creator_name
        self.total_pages = total_pages #tigsstore yung total page count sa total_pages
    def get_number_of_pages(self): #nagddefine ng method para kunin yung page count
        return self.total_pages #return yung total_pages
    def set_number_of_pages(self, new_page_count): # nagddefine ng method para iupdate yung page count
        if new_page_count > 0: #tigccheck if negative o positibe yung page count
            self.total_pages = new_page_count #inuupdate yung total pages if positibe yung new page count
            return self.total_pages #tigrreturn yung bagong page count
        else: #else
            print("The number of pages must be positive") #nagpprint ng syntax error message
    def display_info(self): #nagddefine ng method para maedit yung details ng Book class
        print(f'Title: {self.item_title} \nAuthor: {self.creator_name} \nNumber of pages: {self.total_pages}')#tigpprint yung title, author, at number of pages

class Magazine(Publication): #nagddefine ng bagong subclass para sa Magazine
    def __init__(self, item_title, creator_name, edition_num): #nagddefine function para mag accept ng titel, creator name, at edition number
        super().__init__(item_title, creator_name) #call yung parent class para ma set yung title and creator name
        self.edition_num = edition_num #tigsstore yung edition number sa edition_num
    def get_issue_number(self): #nagddefine ng method para kunin yung edition number
        return self.edition_num #tigrreturn yung edition number
    def set_issue_number(self, new_edition_num): #nagddefine ng method para iupdate yung yung edition number
        if new_edition_num > 0: #tigccheck kung negative yung edition number
            self.edition_num = new_edition_num #tiguupdate yung edition number if positive 
            return self.edition_num #tigrreturn yung updated edition number
        else: #else
            print("The issue number must be positive") #nagpprint ng syntax error message
    def display_info(self): #nagddegfine ng method para maedit yung info sa magazine
        print(f'Title: {self.item_title} \nAuthor: {self.creator_name} \nIssue number: {self.edition_num}') #tigpprint yung titlem author, at edition number.
      
paper_entry = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") #nagaassign ng mga titles and authors
novel_entry = Book("The Hobbit", "J.R.R. Tolkien", 310) #nagaassign ng titles, authors, and pages
periodical_entry = Magazine("National Geographic", "Various Authors", 202) #nagaassign ng title, authors at edition number

print("Publication Information:") #nagpprint ng label para sa publication information
paper_entry.display_info() #tigccall yung display_info at paper_ebtry para iprint

print("\nBook Information:") #nagpprint ng label para sa book information
novel_entry.set_number_of_pages(-310) #tigccall yung set_number_of_pages na may negative na count para iprint yung syntax error output
novel_entry.display_info() #tigpprint yung details ng class Book

print("\nMagazine Information:")#tigpprint yung label ng Magazine Information
periodical_entry.display_info() #tigccall yung display_info sa periodical_entry para iprint yung details
