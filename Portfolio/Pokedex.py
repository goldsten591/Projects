import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from io import BytesIO
import urllib3

# Initializes the tkinter window
window = tk.Tk()

# Establishes the base size of the popup
window.geometry("900x700")

# Creates a title for our popup
window.title("Goldsten Pokedex")


# Gives a border for our popup
window.config(padx=10, pady=10)

title_label = tk.Label(window, text = "Goldsten Pokedex")

title_label.config(font = ("Arial", 32))

title_label.pack(padx=10, pady =10)



pokemon_image = tk.Label(window)
pokemon_image.pack()

pokemon_info = tk.Label(window)
pokemon_info.config(font = ("Arial", 20))
pokemon_info.pack()

pokemon_types = tk.Label(window)
pokemon_types.config(font = ("Arial", 20))
pokemon_types.pack()

pokemon_moves = tk.Label(window)
pokemon_moves.config(font = ("Arial", 20))
pokemon_moves.pack()

event = 0

# Search Function
def load_pokemon(event = 0):
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img
    pokemon_info.config(text = f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text = " - ".join([t for t in pokemon.types]).title())
    #pokemon_moves.config(text = f"{pokemon.moves}")

#window.bind("<Return>", load_pokemon)

label_id_name = tk.Label(window, text = "ID or NAME")
label_id_name.config(font=("Arial", 16))
label_id_name.pack(padx = 10, pady=10)

text_id_name = tk.Text(window, height = 1)
text_id_name.config(font=("Arial", 16))
text_id_name.pack(padx = 10, pady=10)

btn_load = tk.Button(window, text="Load Pokemon", command = load_pokemon)
btn_load.config(font=("Arial", 16))
btn_load.pack(padx = 10, pady=10)

window.mainloop()
