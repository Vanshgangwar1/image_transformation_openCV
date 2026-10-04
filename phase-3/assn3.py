"""
user se file location ask kro 
then give multiple options for 
line circle rectangle text 


take inputs then ask to save or not 
"""

import cv2
image = cv2.imread("phase-3/vansh_palak.jpg")
if image is not None:
    print("image loaded successfully")
    print("which operation you want to choose :\n")
    print("1. line \n")
    print("2. circle \n")
    print("3. rectangle\n")
    print("4. text\n")
    choice=int(input("enter your choice :"))
    match choice:
        case 1:
            print("enter the dimentions for the point 1:")
            pt1x=int(input("enter x axis value for pt1:"))
            pt1y=int(input("enter y axis value for pt1:"))
            pt1=(pt1x,pt1y)
            print("enter the dimentions for the point 2:")
            pt2x=int(input("enter x axis value for pt2:"))
            pt2y=int(input("enter y axis value for pt2:"))
            pt2=(pt2x,pt2y)
            color=(12,43,222)
            thickness=4
            cv2.line(image,pt1,pt2,color,thickness)
            cv2.imshow("image with a line is :",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
                        
        case 2:
            print("enter the centre coordinates for circle:\n")
            cx=int(input("enter x - coordinate:"))
            cy=int(input("enter y - coordinate:"))
            center=(cx,cy)
            rad=int(input("enter the radious for the circle :"))
            thickness=-1
            color=(0,0,0)
            cv2.circle(image,center,rad,color,thickness)
            cv2.imshow("image with a circle :",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        case 3:
            print("enter the coordinates for top left corner :")
            tlx=int(input("enter the x coordinate:"))
            tly=int(input("enter the y coordinate:"))
            tl=(tlx,tly)
            print("enter the coordinates for bottom right corner :")
            brx=int(input("enter the x coordinate:"))
            bry=int(input("enter the y coordinate:"))
            br=(brx,bry)
            color=(12,43,24)
            thickness=3
            cv2.rectangle(image,tl,br,color,thickness)
            cv2.imshow("image with a rectangle :",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            
        case 4:
            x=int(input("enter the x coordinate for the text :"))
            y=int(input("enter the y coordinate for the text :"))
            coordinate=(x,y)
            txt=input("enter the text you want :")
            color=(23,24,122)
            thickness=2
            cv2.putText(image,txt,coordinate,cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1.2,color,thickness)
            cv2.imshow("image with a text :",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
             
        case _:
            print("invalid choice !!!!!!!!!!!")
else:
    print("image not found ")