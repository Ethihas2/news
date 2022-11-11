from tkinter import *
import requests
import json

root = Tk()
root.title("News")
root.geometry("900x800")
root.overrideredirect(True)

label_title = Label(root,text="BBC News Update",font=("Arial",20,"bold"))
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label_head1 = Label(root,font=("Arial",15,"bold"),fg="red",wraplength=700,justify=LEFT)
label_head1.place(relx=0.5,rely=0.2,anchor=CENTER)
label_desc1 = Label(root,font=("Arial",15,),wraplength=700,justify=LEFT)
label_desc1.place(relx=0.5,rely=0.3,anchor=CENTER)

label_head2 = Label(root,font=("Arial",15,"bold"),fg="red",wraplength=700,justify=LEFT)
label_head2.place(relx=0.5,rely=0.4,anchor=CENTER)
label_desc2 = Label(root,font=("Arial",15,),wraplength=700,justify=LEFT)
label_desc2.place(relx=0.5,rely=0.5,anchor=CENTER)

label_head3 = Label(root,font=("Arial",15,"bold"),fg="red",wraplength=700,justify=LEFT)
label_head3.place(relx=0.5,rely=0.6,anchor=CENTER)
label_desc3 = Label(root,font=("Arial",15,),wraplength=700,justify=LEFT)
label_desc3.place(relx=0.5,rely=0.7,anchor=CENTER)

label_head4 = Label(root,font=("Arial",15,"bold"),fg="red",wraplength=700,justify=LEFT)
label_head4.place(relx=0.5,rely=0.8,anchor=CENTER)
label_desc4 = Label(root,font=("Arial",15,),wraplength=700,justify=LEFT)
label_desc4.place(relx=0.5,rely=0.9,anchor=CENTER)


def news():
    api_requests = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=64250819468342609736dd8871799891")
    api_output_json = json.loads(api_requests.content)
    
    news_title1 = api_output_json["articles"][0]['title']
    news_desc1 = api_output_json["articles"][0]["description"]
    label_head1["text"]="Title: "+news_title1
    label_desc1["text"]="Description: "+news_desc1
    
    news_title2 = api_output_json["articles"][1]['title']
    news_desc2 = api_output_json["articles"][1]["description"]
    label_head2["text"]="Title: "+news_title2
    label_desc2["text"]="Description: "+news_desc2
    
    news_title3 = api_output_json["articles"][2]['title']
    news_desc3 = api_output_json["articles"][2]["description"]
    label_head3["text"]="Title: "+news_title3
    label_desc3["text"]="Description: "+news_desc3
    
    news_title4 = api_output_json["articles"][3]['title']
    news_desc4 = api_output_json["articles"][3]["description"]
    label_head4["text"]="Title: "+news_title4
    label_desc4["text"]="Description: "+news_desc4
    

news()
root.mainloop()