

class Course:
    def __init__(self):
        self.course_name= "data_science"
        self.price = 35000
    def show_course(self):
        print(self.course_name,self.price)

class programming_course(Course):
    def __init__(self):
        self.language= "English"
        self.duration ="6Months"
        super().__init__()
    def show_programming_course(self):
        print(self.language,self.duration)
        
D=programming_course()
D.show_course()
D.show_programming_course()



class Camera:
    def __init__(self):
        self.camera_mp = "64MP"
        super().__init__()
    def take_photo(self):
        print("take photo with using",self.camera_mp)
class MusicPlayer:
    def __init__(self):
         super().__init__()
         self.brand = "JBL"
    def play_music(self):
        print("playing music with using",self.brand)
class SmartPhone(Camera,MusicPlayer):
    def __init__(self,model_name):
        super().__init__()
        self.model_name = model_name
    def show_details(self):
        print("Model:",self.model_name)
        print("Camera:",self.camera_mp)
        print("Music_brand",self.brand)
    
    
    
PH1 =SmartPhone("Samsung s22 ultra")
PH2 =SmartPhone("Iqoo 11 Pro")

PH1.show_details()
PH1.take_photo()
PH1.play_music()

PH2.show_details()
PH2.take_photo()
PH2.play_music()
    
    