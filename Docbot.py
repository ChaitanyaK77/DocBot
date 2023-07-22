from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from gtts import gTTS
from playsound import playsound
import time

import numpy as np
import pandas as pd
import mysql.connector as m
conn = m.connect(user='root', password='Chaitanya@2003',host='127.0.0.1',database ='patient')
cursor = conn.cursor()

show = "SHOW DATABASES"
cursor.execute(show)
print(cursor)
for db in cursor.fetchall():
    print(db)








l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','Paroymsal Positional Vertigo','Acne','Urinary Tract Infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# Testing the data

df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)



X= df[l1]

y = df[["prognosis"]]
np.ravel(y)


# TRAINING DATA 

tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)



# User Interface


from PIL import ImageTk, Image  
root = Tk()
root.title("DocBot..Predicts your disease accurately!")

image =Image.open('images2.png')

img=image.resize((800, 700))
bg = ImageTk.PhotoImage(img)

window_width = 800
window_height = 700
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2) 
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
label = Label(root, image=bg)
label.place(x = 0,y = 0)
root.eval('tk::PlaceWindow . center')
icon = tk.PhotoImage(file="doc1.png")

root.iconphoto(True, icon)
root.resizable(False, False)


Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()
Age = StringVar()
Height = StringVar()
Weight = StringVar()


def open_win():
    
    
    def DecisionTree():
        global message1
        from sklearn import tree

        clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
        clf3 = clf3.fit(X,y)

        # calculating accuracy
        from sklearn.metrics import accuracy_score
        y_pred=clf3.predict(X_test)
        print("Decision tree accuracy:")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
    

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            # print (k,)
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break


        if (h=='yes'):
            t1.delete("1.0", END)
            t1.insert(END, "A. "+disease[a])
            message1 = disease[a]
        else:
            t1.delete("1.0", END)
            t1.insert(END, "Not Found")


  
    

    # entries
    
    def insert1():
        global x
        if len(NameEn.get())==0 or len(AgeEn.get())==0 or len(HeightEn.get())==0 or len(WeightEn.get())==0:
            messagebox.showerror("No values entered","Please enter the necessary data required for accurate disease predictions!")
        elif (Symptom3.get()=='None' and Symptom4.get()=='None' and Symptom5.get()=='None'):
            messagebox.showwarning("Warning","Please select atleast 3 symptoms for accurate predictions!")
        else:
            ins = "INSERT INTO details(name,age,height,weight) VALUES (%s,%s,%s,%s)"
            x = NameEn.get()
            info = (NameEn.get(),int(AgeEn.get()),int(HeightEn.get()),int(WeightEn.get()))
            cursor.execute(ins,info)
            symp = "INSERT INTO symptom(name,symptom1,symptom2,symptom3,symptom4,symptom5) VALUES (%s,%s,%s,%s,%s,%s)"
            info1 = (NameEn.get(),Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get())
            
            info3 = (NameEn.get(),)
            cursor.execute(symp,info1)
            conn.commit()
    def bmi1():
        bmi = round(int(WeightEn.get())/((int(HeightEn.get())/100)*int(HeightEn.get())/100),3)
        
        t4.insert(END, "{}".format(bmi))
    def randomforest():
        global message2
    
        from sklearn.ensemble import RandomForestClassifier
        clf4 = RandomForestClassifier()
        clf4 = clf4.fit(X,np.ravel(y))

        
        from sklearn.metrics import accuracy_score
        y_pred=clf4.predict(X_test)
        print('Random Forest accuracy:')
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
        

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf4.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break

        if (h=='yes'):
            t2.delete("1.0", END)
            t2.insert(END, "B. "+disease[a])
            message2 = disease[a]
        else:
            t2.delete("1.0", END)
            t2.insert(END, "Not Found")


    def NaiveBayes():
        global message3
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb=gnb.fit(X,np.ravel(y))

       
        from sklearn.metrics import accuracy_score
        y_pred=gnb.predict(X_test)
        print("Gaussian Naive Bayes accuracy:")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
        

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break

        if (h=='yes'):
            t3.delete("1.0", END)
            t3.insert(END, "C. "+disease[a])
            message3 = disease[a]
        else:
            t3.delete("1.0", END)
            t3.insert(END, "Not Found")
    def erase():
        NameEn.delete(0,END)
        HeightEn.delete(0,END)
        WeightEn.delete(0,END)
        AgeEn.delete(0,END)
   
    # labels
    global new
    new = Toplevel(root)
  
    #new.geometry("900x700")
    new.title("Disease Prediction")
    new.resizable(False, False)
    def callback(url):
        webbrowser.open_new_tab(url)
    link = Label(new, text="Visit For Basic Guidelines.",font=('Helveticabold', 15), fg="blue", cursor="hand2")
    link.place(x=350,y=650)
    link.bind("<Button-1>", lambda e:
    callback("https://cdn1.sph.harvard.edu/wp-content/uploads/sites/30/2021/02/HeatlhyLivingGuide20-21.1.pdf"))
    label = Label(new, text="DocBot is used to find a possible \ndiagnosis for your health issue. \nConsult with your doctor if you feel \nyou have a serious medical problem.", relief=RAISED,bg='White',height=20 ,width=30)
    
   
    label.place(x=450,y=50)
    

    window_width1 = 700
    window_height1 = 700
    screen_width1 = new.winfo_screenwidth() 
    screen_height1 = new.winfo_screenheight()
    center_x1 = int(screen_width/2 - window_width / 2) 
    center_y1 = int(screen_height/2 - window_height / 2)
    new.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    #canvas = Canvas(new, width=900, height=700)
    #canvas.pack()
    
    
    window2 = Label(new, justify=CENTER, text="Welcome to DocBot", fg="Red")
    window2.config(font=("Cooper Std Black", 30))
    window2.grid(row=1,column=1,columnspan=2)

    NameLb = Label(new, text="Enter Your Name:",relief=RAISED, fg="DodgerBlue4", bg="LightSkyBlue1", font=("Arial", 15))
    NameLb.grid(row=6, column=0, pady=15, sticky=W)

    AgeLb = Label(new, text="What is your Age?:",relief=RAISED, fg="DodgerBlue4", bg="LightSkyBlue1", font=("Arial", 15))
    AgeLb.grid(row=7, column=0, pady=15, sticky=W)

    HeightLb = Label(new, text="Height(in cms):",relief=RAISED, fg="DodgerBlue4", bg="LightSkyBlue1", font=("Arial", 15))
    HeightLb.grid(row=8, column=0, pady=15, sticky=W)

    WeightLb = Label(new, text="Weight(in Kilograms):",relief=RAISED, fg="DodgerBlue4", bg="LightSkyBlue1", font=("Arial", 15))
    WeightLb.grid(row=9, column=0, pady=15, sticky=W)


    S1Lb = Label(new, text="Please Select all your symptoms carefully!",relief=RAISED, fg="DodgerBlue4", bg="LightSkyBlue1", font=("Arial", 15))
    S1Lb.grid(row=10, column=0, pady=10, sticky=W)

    #S2Lb = Label(new, text="Symptom 2", fg="yellow", bg="black", font=("Arial", 14))
    #S2Lb.grid(row=11, column=0, pady=10, sticky=W)

    #S3Lb = Label(new, text="Symptom 3", fg="yellow", bg="black", font=("Arial", 14))
    #S3Lb.grid(row=12, column=0, pady=10, sticky=W)

    #S4Lb = Label(new, text="Symptom 4", fg="yellow", bg="black", font=("Arial", 14))
    #S4Lb.grid(row=13, column=0, pady=10, sticky=W)

    #S5Lb = Label(new, text="Symptom 5", fg="yellow", bg="black", font=("Arial", 14))
    #S5Lb.grid(row=14, column=0, pady=10, sticky=W)


    lrLb = Label(new, text="Possible contracted disease:", fg="black",relief=RAISED, bg="LightSkyBlue2", font=("Arial", 14))
    lrLb.place(x=100,y=520)
    BMI = Label(new, text="BMI:", fg="black",relief=RAISED, bg="LightSkyBlue2", font=("Arial", 14))
    BMI.place(x=300,y=580)

    #destreeLb = Label(new, text="RandomForest", fg="white", bg="red", font=("Arial", 14))
    #destreeLb.grid(row=18, column=0, pady=10, sticky=W)

    #ranfLb = Label(new, text="NaiveBayes", fg="white", bg="red", font=("Arial", 14))
    #ranfLb.grid(row=19, column=0, pady=10, sticky=W)
   
    OPTIONS = sorted(l1)

   

    NameEn = Entry(new, textvariable=Name, font=("Arial", 15))
    NameEn.place(x=140,y=50)

    AgeEn = Entry(new, textvariable=Age, font=("Arial", 15))
    AgeEn.place(x=160,y=105)

    HeightEn = Entry(new, textvariable=Height, font=("Arial", 14))
    HeightEn.place(x=150,y=155)

    WeightEn = Entry(new, textvariable=Weight, font=("Arial", 14))
    WeightEn.place(x=170,y=210)

    S1En = OptionMenu(new,Symptom1,*OPTIONS)
    S1En.place(x=20,y=320)

    S2En = OptionMenu(new, Symptom2,*OPTIONS)
    S2En.place(x=20,y=350)

    S3En = OptionMenu(new, Symptom3,*OPTIONS)
    S3En.place(x=20,y=380)

    S4En = OptionMenu(new, Symptom4,*OPTIONS)
    S4En.place(x=20,y=410)

    S5En = OptionMenu(new, Symptom5,*OPTIONS)
    S5En.place(x=20,y=440)
   
    dst = Button(new, text="PREDICT",bg="LightSteelBlue1",relief=SUNKEN, command=lambda: [DecisionTree(), randomforest(),NaiveBayes(),insert1(),bmi1(),erase()], fg="black",font=("Arial", 15),activeforeground='blue',activebackground='red')
    dst.place(x=20,y=650)
   

    #rnf = Button(new, text="Randomforest", command=randomforest,bg="green",fg="yellow",font=("Arial", 14))
    #rnf.grid(row=9, column=3,padx=10)

    #lr = Button(new, text="NaiveBayes", command=NaiveBayes,bg="green",fg="yellow",font=("Arial", 14))
    #lr.grid(row=10, column=3,padx=10)

    # textfileds
    t1 = Text(new, height=1, width=40, bg="LightSteelBlue1", fg="black",font=("Arial", 14))
    t1.place(x=350,y=500)

    t2 = Text(new, height=1, width=40, bg="LightSteelBlue1", fg="black",font=("Arial", 14))
    t2.place(x=350,y=520)

    t3 = Text(new, height=1, width=40, bg="LightSteelBlue1", fg="black",font=("Arial", 14))
    t3.place(x=350,y=540)
    t4 = Text(new, height=1, width=40, bg="LightSteelBlue1", fg="black",font=("Arial", 14))
    t4.place(x=350,y=580)
    


# Add Buttons
pred = Button(root ,text="Proceed to prediction",relief=RAISED, bg ='medium turquoise',activebackground='blue',command=open_win,fg='LightSkyBlue',font=("Helvetica", 20)
, activeforeground='blue')
pred.place(x=300,y=600)






root.mainloop()
