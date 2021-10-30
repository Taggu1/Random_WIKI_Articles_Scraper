from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import time
import wikipedia
BACKGROUND_COLOR = "#003f5c"


def wiki_scraping():
    try:
        page = wikipedia.page(wikipedia.random())
    except wikipedia.exceptions.DisambiguationError:
        page = wikipedia.page(wikipedia.random())
    
    return page




def generate():
    startTime = time.time()

    page = wiki_scraping()
    
    st_label.configure(text=page.title)
    st.configure(state="normal")
    st.delete('1.0', END)
    st.insert('insert', page.content)
    st.configure(state="disabled")

    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


root = Tk()
root.title("WikiScraper")
root.configure(bg=BACKGROUND_COLOR)
root.geometry("800x600+120+50")
root.resizable(False, False) 
root.tk.call('lappend', 'auto_path', '/home/titus/Work/Programming/Depns/Tkk_themes/awthemes-10.4.0/')
root.tk.call('package', 'require', 'awdark')

styel = ttk.Style()
styel.theme_use('awdark')
print(styel.theme_names())

st_label = ttk.Label(root,text="",background=BACKGROUND_COLOR)
st_label.pack()

text_var = StringVar()
st = ScrolledText(root,background=BACKGROUND_COLOR,width=111,height=35)
st.place(x=0,y=30)
st.configure(state="disabled")


button = ttk.Button(text="Generate",command=generate)
button.place(x=10,y=565)




root.mainloop()