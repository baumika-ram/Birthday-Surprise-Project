import tkinter as tk
import pygame
from PIL import Image, ImageTk

pygame.mixer.init()
pygame.mixer.music.load("birthday_song.mp3")

root = tk.Tk()
root.title("something🎂")
root.geometry("800x500")
root.configure(bg="black")

loading = tk.Label(
    root,
    text="Loading Secret Files...❤️",
    font=("calibri",25, "bold"),
    fg="white",
    bg="black"
)

loading.pack(pady=200)

def gift_open():

    popup = tk.Toplevel()
    popup.title("small messege🎁")
    popup.geometry("450x600")
    popup.configure(bg="pink")

    msg = tk.Label(
        popup,
        text="""
MESSEGE FOR YOU ❤️

somes messages to the loved one 
that what you want to tell themm!!
some think that sparke me to do this project 
so i do this one with basics of python 
--> used tkinter to import buttons, labels, frame
--> used pygame to import the audio to play in the background  
while displaying the messeges, photos....
--> used PIL library to import Image Module/Class to include
as well as ImageTk also used to convert the format of PIL Image 
to Tkinter format so that it will understand..!

""",
        font=("Comic Sans MS",10,"bold"),
        bg="pink",
        wraplength=350
    )

    msg.pack(pady=20)

    photos = [
        "image.jpeg",
        "image2.jpeg",
        "image3.jpeg",
    ]

    image_label = tk.Label(
        popup,
        bg="pink"
        )

    image_label.pack()


    def slideshow(i=0):

        img = Image.open(
            photos[i]
        )

        img = img.resize((150,150))

        photo = ImageTk.PhotoImage(img)

        image_label.config(
            image=photo
        )

        image_label.image = photo


        popup.after(
            2000,
            lambda: slideshow(
                (i+1) % len(photos)
            )
        )


    slideshow()

def surprise():

    loading.destroy()

    countdown = tk.Label(
        root,
        text="3",
        font=("calibri",80,"bold"),
        fg="white",
        bg="black"
    )

    countdown.pack(pady=100)

    def update_count(n):

        if n > 0:
            countdown.config(text=str(n))
            root.after(1000, lambda: update_count(n-1))

        elif n == 0:
            countdown.config(text=" BOOM 💥")
            root.after(1000, lambda: update_count(-1))

        else:

            countdown.destroy()

            pygame.mixer.music.play()

            title = tk.Label(
                root,
                text="OIII 😍",
                font=("calibri",32),
                fg="yellow",
                bg="black"
            )

            title.pack(pady=60)

            msg = tk.Label(
                root,
                text="",
                font=("Comic Sans MS",16),
                fg="white",
                bg="black",
                justify="center",
                height=8
            )

            msg.pack(pady=30)

            message = """
        Happy Birthdayy 🎂❤️

May all your dreams come true,
and may this year bring you
countless reasons to smile.
Have an amazing day! ✨ 

"""

            def type_text(i=0):

                if i < len(message):

                    msg.config(
                    text=message[:i+1]
                )

                    root.after(
                        50,
                        lambda: type_text(i+1)
                    )


            type_text()


            button_frame = tk.Frame(
                root,
                bg="black"
            )

            button_frame.pack(
                side="bottom",
                pady=30
            )


            gift_btn = tk.Button(
                button_frame,
                text=" CLICK HERE ",
                font=("Arial",18,"bold"),
                command=gift_open
            )

            gift_btn.pack(
                pady=5
            )

            footer = tk.Label(
                root,
                text="made with little efforts to feel that it is made for you ❤️",
                font=("Arial",10),
                fg="grey",
                bg="black"
            )

            footer.pack(
                side="bottom",
                pady=5
            )

    update_count(3)

root.after(3000, surprise)

root.mainloop()