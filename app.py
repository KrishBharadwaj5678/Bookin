import streamlit as st
from pymongo import MongoClient
import datetime
import secrets
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

st.set_page_config(
    page_title="Bookin",
    page_icon="icon.png",
    menu_items={
        "About":"Bookin provides a powerful admin dashboard for managing hotel bookings. Designed for hotel administrators, this system allows you to effortlessly handle all booking tasks, including adding, editing, viewing, and removing bookings."
    }
)

client = MongoClient(os.getenv("mongodb_url"))
db = client["Hotel_Management"]
booking=db["booking"]

st.write("<h2 style='color:#FFC107;'>Admin Control Panel.</h2>",unsafe_allow_html=True)

tab1,tab2,tab3,tab4=st.tabs(["Add Booking","Read Booking","Update Booking","Delete Booking"])

def addData(bookId,name,email,phone,total_tourist,nightStaying,room_type,payment):
    with st.spinner("This may take few seconds..."):
        book_data={
                "Booking ID":bookId,
                "Full Name": name,
                "Email": email,
                "Phone no": phone,
                "Total Guests":total_tourist,
                "Night Staying":nightStaying,
                "Room Type":room_type,
                "Payment":payment,
                "Arrival Time":datetime.datetime.now()
        }
        booking.insert_one(book_data)

# Add Booking
with tab1:
    name=st.text_input("Full Name",placeholder="Enter Name")
    email=st.text_input("Email",placeholder="Enter Email")
    phone=st.text_input("Phone Number",placeholder="Enter Ph. no",max_chars=10)
    total=st.number_input("Number of Guests",min_value=1,max_value=6)
    nights=st.number_input("Stay Duration",min_value=1)
    room=st.selectbox("Room Type",["Standard Room (1 to 2 People)","Family Room (1 to 4 People)","Private Room (1 to 3 People)","Mix Dorm Room (6 People)","Female Dorm Room (6 People)","Male Dorm Room (6 People)"])
    payment=st.selectbox("Mode of Payment",["Online","Offline"])
    book=st.button("Book")
    if book:
        unique_id = secrets.randbelow(900000) + 100000 
        addData(unique_id,name,email,phone,total,nights,room,payment)
        st.success("Booking Successfull")
        st.write(f"<h2 style='color:lightgreen;'>Booking ID: {unique_id}</h2>",unsafe_allow_html=True)

# Read Booking
with tab2:
    book_id=st.text_input("Booking Id",max_chars=6,placeholder="Enter Booking ID",key=1)
    red_btn=st.button("Show Details")
    if red_btn:
        if len(book_id)==6:
            result=booking.find_one({"Booking ID":int(book_id)})
            with st.spinner("Fetching Details..."):
                try:
                    lst = [
                        {"Field": "Booking ID", "Value": result["Booking ID"]},
                        {"Field": "Full Name", "Value": result["Full Name"]},
                        {"Field": "Email", "Value": result["Email"]},
                        {"Field": "Phone Number", "Value": result["Phone no"]},
                        {"Field": "Total Guests", "Value": result["Total Guests"]},
                        {"Field": "Night Staying", "Value": result["Night Staying"]},
                        {"Field": "Room Type", "Value": result["Room Type"]},
                        {"Field": "Payment", "Value": result["Payment"]},
                        {"Field": "Arrival Time", "Value": result["Arrival Time"]}
                    ]
                    dataf = pd.DataFrame(lst)
                    data_html = dataf.to_html(index=False, header=False, escape=False)
                    st.write(data_html, unsafe_allow_html=True)
                except:
                    st.error("Invalid Booking ID :(")
        else:
            st.error("Invalid Booking ID :(")


with tab3:
    book_id=st.text_input("Booking Id",max_chars=6,placeholder="Enter Booking ID",key=3)
    with st.spinner("This may take few seconds..."):
        try:
            if len(book_id)==6:
                    result=booking.find_one({"Booking ID":int(book_id)})
                    
                    name=st.text_input("Full Name",placeholder="Enter Name",key=21,value=f"{result['Full Name']}")

                    email=st.text_input("Email",placeholder="Enter Email",key=22,value=f"{result['Email']}")

                    phone=st.text_input("Phone Number",placeholder="Enter Ph. no",max_chars=10,key=23,value=f"{result['Phone no']}")

                    total=st.number_input("Number of Guests",min_value=1,max_value=6,key=24,value=int(result['Total Guests']))

                    nights=st.number_input("Stay Duration",min_value=1,key=25,value=int(result['Night Staying']))

                    room=st.selectbox("Room Type",["Standard Room (1 to 2 People)","Family Room (1 to 4 People)","Private Room (1 to 3 People)","Mix Dorm Room (6 People)","Female Dorm Room (6 People)","Male Dorm Room (6 People)"],key=26,index=0 if result["Room Type"]=="Standard Room (1 to 2 People)" else 1 if result["Room Type"]=="Family Room (1 to 4 People)" else 2 if result["Room Type"]=="Private Room (1 to 3 People)" else 3 if result["Room Type"]=="Mix Dorm Room (6 People)" else 4 if result["Room Type"]=="Female Dorm Room (6 People)" else 5)

                    payment=st.selectbox("Mode of Payment",["Online","Offline"],key=27,index=0 if result["Payment"]=="Online" else 1)

                    update_btn=st.button("Update",key=28)

                    if update_btn:
                        with st.spinner("Updating Booking..."):
                            update = {
                            '$set': {
                                "Full Name": name,
                                "Email": email,
                                "Phone no": phone,
                                "Total Guests":total,
                                "Night Staying":nights,
                                "Room Type":room,
                                "Payment":payment,
                            }
                            }
                            booking.update_one({"_id":result["_id"]},update)
                            st.success("Booking Updated Successfully.")
        except:
            st.error("Invalid Booking ID!")

# Delete Booking
with tab4:
    book_id=st.text_input("Booking Id",max_chars=6,placeholder="Enter Booking ID",key=2)
    delete_btn=st.button("Delete")
    if delete_btn:
        if len(book_id)==6:
            with st.spinner("Just a moment, almost there..."):
                result=booking.find_one({"Booking ID":int(book_id)})
                if result==None:
                    st.error("No Booking Found")
                else:
                    booking.delete_one({"Booking ID":int(book_id)})
                    st.success("Booking Deleted Successfully")
        else:
            st.error("Invalid Booking ID!")