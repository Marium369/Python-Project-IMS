from tkinter import*
from PIL import Image,ImageTk
import time
from employee import EmployeeWindow
from supplier import SupplierWindow 
from product import ProductWindow
from sales import SalesWindow
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+0+0")
        self.root.title("Inventory Management System   |  Developed By Marryum Ayub")
        self.root.config(bg="white")

        #===title=====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#708090",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow").place(x=1300
        ,y=10,height=50,width=160)
        #===clock=====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        self.update_time()

        #====Left Menu==
        self.MenuLogo=Image.open("images/Menulogo 2.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=610)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        self.icon_side=PhotoImage(file="images/logo3.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#C0C0C0").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit_system,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)

        #====content=========

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#FFDAB9",fg="#DC143C",font=("times new roman",20,"bold"))
        self.lbl_employee.place(x=300,y=140,height=180,width=350)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#FFDAB9",fg="#DC143C",font=("times new roman",20,"bold"))
        self.lbl_supplier.place(x=677,y=140,height=180,width=350)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#FFDAB9",fg="#DC143C",font=("times new roman",20,"bold"))
        self.lbl_product.place(x=1050,y=140,height=180,width=350)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#FFDAB9",fg="#DC143C",font=("times new roman",20,"bold"))
        self.lbl_sales.place(x=300,y=400,height=180,width=350)
       #===footer=====
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By Marryum Ayub",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
#============================================================================
    

    def employee(self):
        self.EmployeeWindow=Toplevel(self.root)
        self.new_obj=EmployeeWindow(self.EmployeeWindow)

#============================================================================

    def supplier(self):
        self.SupplierWindow=Toplevel(self.root)
        self.new_sup=SupplierWindow(self.SupplierWindow)
    
#============================================================================
    def product(self):
        self.ProductWindow=Toplevel(self.root)
        self.new_prod=ProductWindow(self.ProductWindow)

#============================================================================
    def sales(self):
        self.SalesWindow=Toplevel(self.root)
        self.new_sal=SalesWindow(self.SalesWindow)

#============================================================================
    def exit_system(self):
        self.root.destroy()

#============================================================================
    def update_time(self):
        current_time=time.strftime('%I:%M:%S %p') 
        current_date=time.strftime('%d-%m-%Y')    
        
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:{current_date}\t\t Time:{current_time}")
        self.lbl_clock.after(1000,self.update_time)


if __name__=="__main__":
    root=Tk()
    obj=IMS(root) 
    root.mainloop()
