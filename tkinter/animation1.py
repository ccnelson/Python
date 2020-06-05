# the right way!
import tkinter as tk

class Admin():
    count = 0
    
a = Admin()
root = tk.Tk()
text = tk.Text(root, background='black', foreground='lawn green',\
               font=('Courier', 3), height=20, width=40)

animation = ["""
                                        
                MMMMMMM                 
             MMMMM    MMMM              
           MM   M      MMMMM            
          M    M         M  MM          
        MM     M         M    M         
        MM      M      MM     M         
       M         MMMMMM        M        
       M                       M        
       M                       M        
       M                       M        
        MM                    M         
        MM                    M         
          M                 MM          
           MM             MM            
             MMM       MMM              
                MMMMMMM                 

""", """

                MMMMMMM                 
            MMMM       MMMM             
           MM         MMMMMM            
         MM         MM      MM         
        MM          M       MMM         
        MM         MM         M         
       M            M       MM M        
       M             MMMM  MMM M        
       M               MMMMM   M        
       M                       M        
        MM                    M         
        MM                    M         
         MM                 MM         
           MM             MM            
            MMMM       MMMM             
                MMMMMMM                 
                                                                           
""", """                    
                                        
                MMMMMMM                 
             MMM       MMM              
           MM             MM            
          M                 MM          
         M                    M         
        MM              MMMMM M         
       M              MM     MMM        
       M             M         M        
       M             M         M        
       M             M         M        
        MM            MMM   MMM         
        MM               MMMMMM         
          M                 MM          
           MM             MM            
             MMM       MMM              
                MMMMMMM                 
                                         
""", """
                                        
                MMMMMMM                 
            MMMM       MMMM             
           MM             MM            
         MM                 MM         
        MM                    M         
        MM                    M         
       M                       M        
       M               MMMMM   M        
       M             MMMM  MMM M        
       M            M       MM M        
        MM         MM         M         
        MM          M       MMM         
         MM         MM      MM         
           MM         MMMMMM            
            MMMM       MMMM             
                MMMMMMM                 
                                 
""", """                       
                                        
                MMMMMMM                 
             MMM       MMM              
           MM             MM            
          M                 MM          
        MM                    M         
        MM                    M         
       M                       M        
       M                       M        
       M                       M        
       M         MMMM          M        
        MM     M      M       M         
        MM   MM        MM     M         
          M  MM        MM   MM          
           MMNMM      M   MM            
             MMMM    MMMMM              
                MMMMMMM                                                  
""", """

                MMMMMMM                 
            MMMM       MMMM             
           MM             MM            
         MM                 MM         
        MM                    M         
        MM                    M         
       M                       M        
       M    MMMM               M        
       M  MM   MMM             M        
       M  M       MM           M        
        MM        MM          M         
        MMM       MM          M         
         MM      MM         MM         
           MMMMMM         MM            
            MMMM       MMMM             
                MMMMMMM                 
                                 
""", """
           
                MMMMMMM                 
             MMM       MMM              
           MM             MM            
          M                 MM          
        MMMMMMM               M         
        MMM    MM             M         
       M         M             M        
       M         M             M        
       M         M             M        
       MMM      M              M        
        MM MMMM               M         
        MM                    M         
          M                 MM          
           MM             MM            
             MMM       MMM              
                MMMMMMM                 

""", """
                       
                MMMMMMM                 
            MMMM       MMMM             
           MMMMM          MM            
         MM       MM        MM         
        MMM       MM          M         
        MM        MMM         M         
       M  M       MM           M        
       M  MM   M M             M        
       M   M MMM               M        
       M                       M        
        MM                    M         
        MM                    M         
         MM                 MM         
           MM             MM            
            MMMM       MMMM             
                MMMMMMM                                     
"""]

def update():
    text.delete(1.0, 'end')
    text.insert('end', animation[a.count])
    text.pack()
    a.count +=1
    if a.count == 8:
        a.count = 0
    root.after(100, update)

root.after(0, update)
root.mainloop()
