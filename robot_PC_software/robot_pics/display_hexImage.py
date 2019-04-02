import display

def display_image(fileName):
    d = display.Display()
    d.clear()
    d.hexImage(fileName)

if __name__=="__main__":
    display_image("elai.hexImage")
