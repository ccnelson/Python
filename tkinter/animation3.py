# the right way!

import tkinter as tk

class Admin():
    count = 0
    
a = Admin()
root = tk.Tk()
text = tk.Text(root, background='black', foreground='lawn green',\
               font=('Courier', 3), height=45, width=65)

animation = ["""
                                                            
                              ,,,,,,,,,                     
                    ,,==??I?IIIIII?=+~~,,,,,,               
                  ~~MM88OOOOZZOOOOODDNN??::,,,              
                MMDDOO$$$$$$$$$$$ZZ$$ZZ88II==:,,,,          
               +8O$$$$ZZZZZZZZZZZZZOOZZ$$88MM+::::,,        
               =O8$$$$$$ZZZZZZZZZZZZZZZ$$D8MM+~:::,,        
          ,::??N$$$$$$ZZZZOOOOOOOOOZZZZZZ$7OON?+~~::,,      
         ::NNZZ$OO88OODDDDDNNNNNNNNDD888OOOZZZND??~~::,,    
         ++ZO$$ZOOOO88NNDDDDDDDDDDDNNDD8D88OOZOZNN++::,, ,  
       ,,MM$$ZZO8O88DNDDNDNNMMMMMMM8DDDDNOOOOZZZOONM==::,,  
     ,,??O8$$OOOD8DD88MMMMI7+++++++MMNN888888OZOZ$DD??~~::  
     ,,??88$$OOODDDD88MMMMII??+++++MMNN88DD88OZZ$$DDII~~::  
   ,,MMZZIIZ$OOOOODNMM??==::,,,    ~~??MMOO88OZZZZ$$ZZ==:~,,
   ~~DD7777$$OOZ88MM++~~::,,           ++DD888ZZZZZZNN++~~,,
   ++OOII$$ZZ$$ONNII==::,,             ,,MMOO8ZZZZZZ88II~=::
   II$ZII$$$$$$OMM??~~::,,               ==DDZZZZZ$$OOMM==::
   77$$777$7777$8O++~~::                 ::NNZ$$$$ZZZZNN??::
   77$$77777777$8O++~~::                 ::NNZ$Z$$ZZZZNN??::
   77ZZ$$$$777778O=+~~,,                 ::NNZ$$$$ZZZZNN??~~
   77ZZ$$$$77??78O++~~,,                 ::NNZ77$7$$ZZNNII~~
   II88$Z$$I?~~IMM++~~::                 ==DD7II77$$OONNII~~
   ??DDOO$$II=~=NN??==::,,               MM88III77$$88NN?I~~
   ++DDOOZ$II==~8877==~~,, ,           ::NN$$+II77$$88MM??::
   ~~NN88Z$II++~ZZNN$$==::,,,,       ,,++88II=77$$ZZDDMM==::
   :~NN88ZZII++~Z$NN7$==::::,,       ,,++88II=I7$$ZZDDMM==::
     ==NN88$$77+=~?IZO$$+?~~::,   ,==MMDD++~~=$$ZZ88MM++~~,,
     ,,MMDDZZ$$I::=~??88NNMMII???MMDDZZI7~=++7ZZOODD$$==:~,,
       ::MMO8ZZ$++~~~~77$$ZZ88888OO77??==++II7OODDMN??~~,:  
         I?DD88Z?I==~~==++?I777II??++++==II$7$DDMM??~~::,,  
           I?MMNZZZZ$$+++++========??II7$OZ88D$$??:~::,,    
           IIMMNZZZZ$$++++++=======??II7$OZ88D$$??:~::,,    
             ::MDDO8OO$$77II??III77$$ZZZO88NNM++::,,,,      
               :MMNNDDOOOOZOZZZZZZZOO88DDMNMM=::,,,,        
                ::=+MMNNNNDDDDDDDDDNNMMMM++:::,,            
                    ::++????IIIIIII??++~~,,,,               
                               ,,,,,,,, ,                   
                                                  
""", """
                                                            
                          ,,,,,,,,,,,,,                     
                ::=+II$$$$ZZZZ$$$77++::,,,,                 
               :NN88ZZ777777II777Z$8DMM++::,,,              
             :~MZZ77II??++??+++++++77ZZDD+?:::,,            
           ~~NNZ??II++==??II77IIIII++??7$MM==~::,,          
           ~=NNO??I?++==++??IIIIIII++??77MN==~::,,          
         ==DN$$I?I?+++77$$$$ZZZOOOO$$77IIOOMMI~~::,,        
       ~~DD????I7777$$OOOO88NNNNNDDDDDN88ZZ$$8II~~,,,,      
     ::NN$$??III77$$ZZDD8D88DDD88DDNN88DDOOZOZZZ==::,,      
     MMZZIIIIIII$$OO8888NDMNMMMMMMM88DDDN8D88ZNN??~~::,     
   ~~DDII++II777ZZ8O88MMII++===+=MMNMDDDDDD88O88I7==::,,    
   ~~DD77++II777$Z8888MMII++~~~++MMMMDDDDDD88O88I7==::,,,    
   77II++II77777OODDZZ++~~::,,   ,,??MMMMDDDD8ZZ88II~~::,,  
   ZZ??++II$$II$88MM==~~::,,         ,,MM88DD8OOOZNN++:~,,,  
 ,,MM?+??II7777$NNII==::,,             ?+DD8O8OOZZ8DII~~::,  
 ::NN??II77II77$MM++~~::               ==NNOO8ZZZZ8O77==::,,
 ~~NDII77$$IIIIZ8O++~~::               ,,MMOOOZZZZZZZZ==::,,
 ~~NDII77$$IIIIZ8O++~~::               ,,MMOOOZZZZZZZZ==::,,
 =~ND77$$$$I???ZOO=+~~,,                 MMOOZ$ZZZZZZZ==::,,
 ==NN$$$$77??++$OO=+~~,,                 MMOO7$$$$ZZZZ==:~,,
 ~~NNZZ$$77II++788++~~,,               ~:DN$$?$$$$OOZZ==:~,,
 ~~NNZZ$$7$II++?MM++~~::,,             ++OOII+$$$$88ZZ==::,,
 ::MMOO$$$$77+++NDII==::,, ,           II7$+++$7ZZDD$$~=::,,
   MM88ZZ$$$$II=OOMMI7~~::,,       ~:??NN??==?$$8ONNII~~,,  
   MMO8ZZ$$$$II+OOMM77~~::,,       :~??NN??=+?77OONNII~~,,  
   ?+DD88OO$$II?++778877==::,,,, ~~NNOO7I++++?OONNII==::,,  
   ::MMDD88$$77I~~?+77DDMM77???IINNZZ77??==??7DDMM==~~,,    
     ==NNDDOO$$7~~~~==77ZZOO888OO$ZII++==++77ZMM++~~::,,    
       MMNN88OO$??~~~~==++??IIIII??=+++++??Z$D77~~::,,      
         ++NNNNDZZ$$77~~::::,,,::~~++??$$NDMM7~~::,,        
         ++NNDD8ZZ$$I7~~:::::::~~:~+=??$$DDMM7~~::,,        
         , MMNNN88OOZZ77II+?==+++++I7ZZDDMM++~::,,          
           , ==MDDDD88OOZZ$$$$Z$$ZZ88DDNN??:::,,            
               :MMMMNNDDDD8DDDDDDDDNNMM++::,,,              
                ::==??7777$$$$77777++~~,,,,                 
                          ,,,,,,,,,,,,,                     
                                               
""", """
                                                            
                      ,,,,,,,,,,,,,,,                       
                +?77$$OOMMMMZZZ$$++::,,,,                   
             ,,?OO$Z7$II????III$7DDII==::,,                 
           ,:MM8II??++~~::::~~=++7$OOMM==::,,,              
         ::NMOO$?+==:~,,, ,,~~=++??IIOOMM=+::,              
         ,:NMOO$++~~::,,,,,:~~=+++?7IOOMM==::,              
         ??OO77?==::,,::::==77$$$$$$$$$OO77~~:,,            
       ==88=+==+:::,::77OZ88DDD8888888888D8II~::,,          
     ::NN77++==~:~~~==OO8888888DDNNNNDD8DOONN+~~:,          
     MMOO??++++:~~==77DDDDMNMMMNND8DNNNDN8888M==::,,        
   :~NN7$++++++~==?IZZNNMM+?===MMNN8888NMDD88N??~~,:        
   :~DN77++++++~~~IIZZNNMM??===MMMMOO88MM8D88N??~~,:,        
   II77==~=II++~IIOODD77==::,,,,,IIMMNNOODN888ZZ==::,,      
   $$II====II==~7788NN??~~::,,     ==MMDDDN888OO==:~,,,      
   MM??==++II===ZZ88$$==:~,,       ::MMNNDD888MM++~~::,      
 ,,MM??==II?I++=OODD77==::,,         ++NN8888ONNI?~~::,      
 :~NN??I?II77++=ZONNII==::,,         ~~NNZZOZZDD77==::,,    
 :~NN????II77++=ZONNII==::,,         ~~NNZZOOZDD77==::,,    
 ~~NNIIII7777??+ZONNII==::,,         ::NN$7ZZZDD77==::,,    
 ~~NN777777$$II?ZZNNII==::,,         ~~NNII$$$DD77==::,,    
 ::MMZZ$$777$77?ZZ8877==::,,         ==88++7I7NDII==::,,    
 ,,MMOO$$$$7777IZZ8877==:~,,         MMZZ+=IIINNI?~~::,      
   MMOOZZZZ7777I$$OOMM++~~,:       ~~NN77==??IMM++~~::,      
   $$88OOZO$$$$777ZZ8DII~=::,,   ++MM88II==??7OO==~~,,,      
   7$88OOZO$$$$777ZZ8D??~~::,,   +=MM88??+=??788==:~,,      
   ++DD8888$$ZZ$??77$$NM??==::,++DDZ$II++++II877==::,,      
   ~~NNDDDDZZZZZIIII77ZZDDMMIIMNN$$II??++??$$N??~~,,        
     MMNNDDOOZZZI7II++77$$OO88O$$??++~~~~77DD7~~::,,        
     ~:MMNN88OOZ$$IIII??III?7I?++==~~~~==OOMM+~:,,          
       ::IINNNNDOO88$7II=~~~~~~~~~~==I7OOZZ++~,:            
       ::I?NNNNDOO8877II==~=~~=~~~~=+IIOO$$++~::,          
         ::MMNMN88ZZOO777$II++~==??77OONNII~~:,,            
           ::MMMDD8888ZZ$$$$77777ZZ88NNMM==::,              
             ::MNNNNDD8888OOOOOOODDNNMM~~::,,               
               ,??77Z$MMMMMMMMMMM77?+::,,,,                 
                      ~~~~====~::,,,,,,                     
                                         
""", """
                                                            
                      ::~~==~~,,,,,,,                       
                :~??$$MMNNNDNNO$$==::,,,,                   
               :DNOO77????????7ZZNN?+~~::,,                 
               IZZII+?==~~~~==?77OONN??~~::,,               
             ==D?I?+==::,,::??I77$$88NN+?~~::,              
             ==DII++==::,,::??I$7ZZ88NN+?~~::,              
           ++DDZ====~=,,,:::II$ZZZZOO88MM==::,              
         ++OOII===::  ::~~IIZZZOOD8888888$$~~: ,            
         7I$$++=~=::  ~~++Z$OO8NDDNDD88DDZZ==:,,            
         Z$??~=~~~,,,,++$$OZMMNNNDDNNDDDDMM==~,,            
       ::MN++~~~~~::,,??OODDMMMMMD8DDNNDDMN++~,:            
       ::MM++~~~~~::,,IIOODDMMMMM8DNDNNDDMM??~,:,           
       ++OO~~~~?~~::~~OONN77+++I?MMOODDNNDD77~::,,          
     ,,MMZZ~~==?~~::~~88MM++::,++MMDD88NNDDMM=::,,          
     ::NN$7~~++?==~~==DD77==::,~~MMNNOONNDDMM+~~,,          
     ~~NN$$==??I++~~++DD77==::,::MMNNOO88DDNN?~~,,          
     ~~DD$$??II7??++??DDII==::,::MMD8OOOOOODDI~~,:          
     ~~DD$$??II7??++??DDII==::,::MM88OOOOOODDI~~,:          
     ~~ND$$II777?I++??DDII==:: ::NMOO$$Z$OODDI~~::          
     ~~NNZZ77$7777?IIIDDII==::,::NNZZ??77ZZDDI~~::          
     ~~NNOO$$$$7$77777DD77==::,::NN77==??$7DDI~~,:          
     ~~NN8O$Z$$777$77788$$==::,~~NN77++++$$NN?~~,,          
     ::MM88ZZZZ$$$$$$$88MM++~:,==DDII++++ZZMM+~~,,          
     ,,MM8DOOOOO$$$$$$OOD8II~~:??8OII++++OOMM=::,,          
     ,,MMDDOOOOZ$$$$77OODDII::,+?88?I??++ZOMM=::,,          
       ==NN88OOZZZ$Z$$$$OO8D???NN77??===+NDII=::,,          
       ::MM8888OZZZZ$$$$ZZZZNNDOO++??==++MM?+~,:            
         MMDD88OZOZZ$$77$$ZZZZ$II==++==IIOO==~,,            
         77DDDD8OOZZZZ777777???++?+++??$$ZZ==:,,            
         ::MMNND8888OO$$$$777$???II$7OONNI?~~:              
         :~MMNND8888OO$$$$7777???II$$OONN?I~~: ,            
           ==MNNDD8888ZZ$$$$II7II77OODDMM==::,              
             ++MNNNDDDZZZZ$$77777OODDMM=+::,,               
             ,,MNNNNDD88OOZO$$$ZZDDMM++::,:                 
               :77MMMMMMNNNNNNNMM77==::,,,,                 
                  :,==MMMMMMMM?==::,,,,                     
                                       
""", """
                              ,,,,,                         
                        ==II77I++::,,,,                     
                    ::MMDDOOZZOND?I~~::,,                   
                  ,,MM$$??+?++?77DNII~~::,,                 
                  ++88??====~~+IIOOMM++~~,,                 
                =~ND$$==~~~~::=??OO8D77==::,,               
                :~DN$$==~~~~::=??OODD77==::,,               
               ,MMZZII==~~:~,,~IIZODDMM++~~,,               
               ?ZZ??~~~~~~,,,,~IIZZDDNN77~~::               
               777==::~~::,   ~IID8NNDD$$==::,              
               Z??~~::~~::  ,,+IIDDDDDD$$==::,              
             ,,M++~::,~~::  ,,+IIDDNNDNZZ=+~~,              
             ,,M++::::~~,:  ,,+IINDNDDDZZ==~~,              
             ~~N~~,::,==,, ,,,+77OODNDDZZ==~~,              
             ~~N~~::::++::,,::?77ZZDDDDOO=+~~,              
             ~=D==~~==??~~,,::?77ZZDDDDOO++~~,              
             ==D==~=??II==::~~I77ZZ8DDDOO++~~,              
             =+D++++II77??~~==I7I$7OO88OO++~~,              
             =+D++++IIII??~~==I77$$OO88OO=+~~,              
             ++D????7777I7++++I??77ZZOOOO++~~,              
             ++D7I77$$7777II???==II7$$ZOO++~~,              
             ++D$$$$77777777III~~==++IIOO++~~,              
             ++DZZZ$$$ZZ$$77III~~==++IIOO++~~,              
             ==DOOZZ$$ZZ$$$$777++~=++IIOO=+~~,              
             ==NOOOOZZ$ZZZ$$77$??==++77ZZ=+::,              
             ==NOOOOZZZZ$$ZZ77$??==++77ZZ=+::,              
             ::M88OOOOZZZZ$$$$$??=~??ZZ$$==::,              
               M888888OOOOZZ$$7I7+=77O8$$==::,              
               $888888OOOOZZ$$7$$I?ZZ8877==::,              
               7D8888888OOZO$$7$$IIZODDII~~::               
               =NNDDDD8888OO$$$7$I7OONM??~~,,               
               =NNDDDD8888OO$$$7$77OOMM??~~,,               
               :MMNNDDDDDD88ZZZ$$ZZDDMM==:~,,               
                ==NNDNNNDD88ZZZZZOONNII~~::                 
                ,,MMNNNNDDDDO8OZODDMM++:~,,                 
                  ,,??MMNNNNNNDNN$$==::,, ,                 
                      ??77ZZOOZ77::::,,,,                   
                                         
""", """
                              ,,, ,                         
                        ?I$$ZZ?::::,,                       
                      ??ZZ$$778MM==::,,                     
                    ==DD??++==IOOMM==::,,                   
                  ,,MMOO++==~~?Z$DDII~~:: ,                 
                  ~~DD$$==~~~~=7IOOZ$==::,,                 
                  ==DD$$==~~~~+IIOO$$==::,,                 
                  +?88II~~~~:~=?+ZZZZ==~~,,                 
                ::NNZZ++::~~~::~~II88++~~,,                 
                ~~NN$$==~:::~::::IIMM++~~::                 
                ~~NN$$==,,::~::::++MM??~=::                 
                ~~NN$$==,,::~~:,,++MM??==::                 
                ~~NN$$==,,~:~~:,,++MM??==::                 
                ~~NN77==,,~~++,::++NNII==::                 
                ~~NN77==::==++:::++NNII==::,,               
                ~~NN$$==~~++??~::++NNII==::,,               
                ~~NN$$++==????~::++NNII==::,,               
                ==DDZZ????IIII+++??NNII==::,,               
                ==DDZZ???+IIII+++??NNII==::,,               
                ==DDZZIIII7777???IINNII==::,,               
                ==NDZZ7777$7$$III77NNII==::,,               
                ==NNOO$$$$77777$$$$NNII==::,,               
                ==NNOOZZ$$$$$$$ZZZZNNII==::,,               
                =~NNOOZZ$$ZZ$$ZZZZZNNII==::,,               
                ~~NNOOZZZZZZZZZZZZZNNII==::,,               
                ~~NNOOZZZZZZZZZZZZZNNII==::                 
                ~~NN88OOOOZZZZOZZOOMM??==::                 
                ~~NN88OO8OOOOOOZZOOMM??~=::                 
                ::NN88OO88OOOOOOOOOMM??~=::                 
                ::NM88OO88OOOOOOOOOMM++~~,,                 
                ,,MMDDOO888D888O8888O++~~,,                 
                ,,MMDDOO8ODD888OO8888++~~,,                 
                  MMND888ODDDDD88DDOO==~~,,                 
                  ==NNDDDDDDDDDDDND$$==::,,                 
                  ::MMDDDDNNNNDNNNNII~~,,                   
                    ::MMNNNNDDNMMII~~::,,                   
                      ::77ZZZZI==::,,,,                     
                                           
""", """
                                ,,,,,,,                     
                          ~~II$7$II::::,,,,                 
                        IINNOO$Z$O8$$++::::,,               
                      II8O$$II++++?ZZNN??~~::,              
                    ,,MMZZ7I??~~~==IIZZNN+?~~,              
                    ~~NN$$?I++:::~~=+IIOO7$==:,,            
                    ~~DD$$II++:::~~++II8O$$==:,,            
                    ++DD$7??++:::::==??$$OO==~,,            
                  ~~NNDDZZII++,  ::=~:~==DDII=:: ,          
                  ++NNDDZZ77??,  :,~~~~~~OOMM=::,,          
                  MMNDNNNN77??,    ~~~=~:$$NN?~~,,          
                :,MMDDDD887$??,    ~~==::77DDI==:: ,        
                ,:MMDDDD8D77??,  , ~~=~~~IIDDI==:: ,        
                ==NNDDNNZZOOII,  ,,++==:~++OZM=+::,,        
                ++DDDDNN8888II,  ,,++++~~=+ZZM??~~,,        
                ??DD8DNN8888II:,,::????==++$$N??~~,,        
                IIDD88DD8OZZII:::~~??II++++$$NII~~,:        
                II88OOZZ$$$$II~~~++IIII????$$NII~~,:        
                II88OOZZ$$$$II~~~++IIII????$$NII~~,:        
                IIOOZZ$$II77II===??7777IIIIZZNII=~,:        
                IIOO7777==??II+??II7777$$77ZZNII=~::        
                IIZZ++++  ~~III77$$$$77$$$$OONII=~::        
                ??ZZ++==  ::III77$$$$$$$$ZZOONII~~,:        
                +?OO??==,,::II777$$$Z$$$$OO88NII~~,:        
                ==88II==::~~II777$$Z$$$Z$OO88N??~~,,        
                +=88II==~:~~II777$$ZZ$$ZZOO88N??~~,,        
                ::NN$$??~~~~II7$$ZZZZZZOO88DDM++:~,,        
                , MMOOII~:+=77$Z$ZZOOOOOO88NN7==::,,        
                  ??88$$~~??$7$ZZOZOO8888DDNNI~~::          
                  ==DDZZ==II77$ZZOOO88888DDMM+~~,,          
                  ,,NMOO7I$$77$ZZ8ODDDDD8NMII=:: ,          
                  ::NMOOI7$$77$ZZ8ODDD8D8MNII=::,,          
                    ++DD$$$Z77ZOO88DDDDDDMM++~,,            
                    ~~NNZZ$$Z$O88DDNNDNNN$$==:,,            
                      MMOOOOOZ8D8DDNNNNMM??::,              
                      ~~MMNNNNNNNNNMM77++::,,               
                        ::++II77777~=::,,,,                 
                                         
""", """
                                                            
                              ~====::,,,,,,,,               
                        ++77ZZNDDDDMMZZ77~~::, ,            
                      ++88ZZ77?+++?II$$Z$MM==:,,,,          
                    ::NN$$77++=~~~~==++IIOOMM=:~:, ,        
                  ::NN88$$7III~::,,~~~~++77OOM==~~,,        
                  ::MNOO$$77??~::,,~:~~++77OOM~=~~,,        
                  MMD8OO$$$$Z$=~~ ,,,,,~=??778$$~~::,,      
                +?D888OO88O8ZZZII=~,,,,,,====?ZZ$$~~::,,    
                77DD8888DDDDDDZZZII,,  ,,==+==77OO==~~,,    
                $$DD8DNN88NDNNDZO$$::, ,,=====?+MM++~~::    
               ,MMDDNDDDDDNMMMNDDOO~~,,,,====~==DDII==::,,  
               ,MMDDNNDDDNMMMMN8DOO==,,,,====~+=DDII==::,,  
               ~NNNNNN88MM77??+IINN7I~~:~==??==~$$MM++~~,,  
               =DNMN88DD77~~::,,,MM$$==~~==II+=~77NNII~~::  
               MDDNN88NNII~~::,  $$ZZ++~~++II?==IIDD77==::,,
             ,,MDDDDO8NNII~~::   $$OO??==??III++IIO8$$==:~,,
             ~~N88ZOOODD77~=::,  77OO77++III77?II?OZNN??~~,,
             ~~N88ZOOODD77~=::,  77OO77++IIII7?IIIOONN??~~,,
             ~~NOO$$$$88$$==::,  77OOII++II777IIIIOONN??~~,,
             ~=DZZ77??OO$$==::,  77OOI7??II$$77777OONNII~~,,
             ==D77??++$$ZZ==::,  $$OOZZ7777777$$ZZ88NNII~~,,
             ==D77??++7$ZZ==::,  $$OO$$7I$$$$7$$OZ88MM??~~,,
             ~~N77?+++77ZZ==::,  ZZZZ7777ZZZZ$$$OODDMM++~~,,
             ::MZ$++++IIOO??::,~~MMZZII$$ZZZ$ZZZ88DDMM==::,,
             ,,MZ$++++IIOO++::,~~NMZZII$$ZZZ$ZZZ88DDMM==::,,
               =8D===+++O8NM??+NNOO$$77$$ZZZZOOODDMM??~~::  
               :MN++~=++IIZZNNNZZZZ$$$$$$OZZZO88ND$$==~~,,  
                ZZI?====++7I77$$$$7$$$$Z$OOOO8D8NNII==::,,  
                77$$??++++++III$$77$$$$ZZOOOODDDMM+?~~,,    
                :~NNOO77??II???7777ZZZZOODDDDDNN$$~=::,,    
                ~:NNOO77??II???7777ZZZZOODDDDDNNZ$==::,,    
                  ==DDOO77II77777$$ZZOO88NNNNNMM??~~,,      
                    MMDD$$$777$$$$$OO88DDNNNNM??~~::,,      
                    ,,MM88OOZZZOZO8DDDDNNMNMM+~~::,,        
                      ::$7MMNNNNNNNMMMMMM77++:,,,,          
                          ::++MMMMM??++~~::,,,              
                                        
""", """
                                                            
                            ,,,,,,,,,,,,,,,                 
                      ??7I$$OOMMMZOZZ$$+=::,,,              
                  ,,MMOO77II?????77$$$$DDII==:,,,,          
                ::MMOO??++==:::::==++??$$OONN+::,,,,        
               :MNOZII++++~~~~,,,,,::~=??$7ZZN++~~::,,      
               ,MNOZII++++=~~~:,,,,:,~~?+$$OON++~~::,,      
               +OZ77I7$$$$$$II+~~,,  ,:==++77Z$$==~~,,      
             ==8OOOO8888DDDD888OO++~~:,::??=~+OO77==::,,    
           ~~DDOD888DDDD8888DD8O8Z$??::::~~++=77DDII~~::,,  
         ,,MM888D8MNNDDDNNMNMMNDD88$$++:,~~+++??ZZNM++~~,,  
         ~~DD888NND8OOMMMMII++=MM88ZZ$$::~:=++++77DDII~=::  
         ~~DDOO8NN88OOMMMMII+++MM88OZ$7:::~=++++IIDDII~=::  
       ~~NN8888NOODNMM77++::,,,:,MMD8OO==~~=+I+=++$$ZZ==::,,
       ==DD8888D88MMMM++~~,:,,   ~~NNOO??~~=+7++==IIOO=+~~,,
       ??888888DDDNNII~~::,,       MM88II==++7?I++??OO++~~,,
       II88OO88ODDMM++~~,,         ==DD77++++I7I+???MM+?~~::,
       77OOZZOZ$DD77==::,,         ,,MM$$++++I77IIIINNII=~::,
       77OOZZOO$DD77==::,,         ,,MM$$++++I77IIIINNII==::,
       77OOZZZZ7DD77==::,,         ,,MM$$++??777IIIINNII==::,
       77ZZZZZZ?DD77==::,,         ,,MM$$??II7$$7777NNII==::,
       77ZZ77II=OOMM==~~,,         ~~NNI7??II7$$$$ZZNNII==::,
       IIZZII??=$$MM++~~,,         ==D8II??II7$$$$OZMMII==::,
       ??OOII+?+77DDII~~::,,       ?+OOIIII777$$$ZOOMM??~=::,
       ==DD77??+?I88MM==~~,:,,   ++MNZZIIII$$$ZZZZ88MM++~~,,
       ==8877??+I?OOMM==~~::,,   ++MNZZIIII$$$ZZZZ88MM++~~,,
         MM88II=++IIZZ$$+=::,,,++88ZZ77II77ZZZOOOODDZZ=+~~,,
         ::NNZZ+=+??II88MMII??INN$$77??77$$ZZZ8888NN77==::,,
           ==DD7~~~~++77ZZ8O88OZZ77++??$$ZZZZO88DDMM??~~,,  
           ,,MM8==~~~~??I???77I?I++++77ZZOZOOODNMNII~~::,,  
             ,,IOO77++~:::::~~~+=II77ZZOO88DDDMMII~~::,,    
             ::IOO77++:::::~~~~==7I77ZZOO88DDDMMII~~::,,    
               =NNOO77==~~~~+++7I$$OOOO88DDNNN77~~::,,      
                MMNN88$$7$77777$$OO8888NNNNMMM~~::,,        
                  MMNN88OOOOOOOOOD8DDNNMMMM??~::,,          
                    ~~77ZZMMMMMMMMMMM$$??~~::, ,            
                          ::~~===:~,,,,,,,,                 
                                          
""", """
                                                          
                              ,,,,,,,,,,,,,               
                      ~~II77$$ZZZZZ$$77??::,,,            
                  ::++DDZZ777777777$$ZZ88II==:,,,,        
                ~~NNOO$$??+++++++++??II77O8NN?:~::,,      
               ~8DZ$II??IIIIII7IIII++++?I77ZZD??~~::,,    
               ~DDZ$II??IIIIII777??++++??77ZZD??~~::,,      
             ~~I$$I7$$ZZOO88OOZ$Z$$II??????II$ZZII~~::,,    
           ~~DDZOZ88DDDDNNNNNNNDD88ZZ$$$77777?7788II~~::,,  
         ::NNZZZD8DNDDDDDD88DDD888888OOZZ77III??$$DN??~~::  
         +=OOOOOD8NNNN88NNMMMMMMMNNO88888$$77I++I?ZZMM=+~~  
         IIOZ8O8MMDDOONNMM??++===++MM8888$$$$7II++7IDDII~~  
         IIZZOO8MM8DOONNMM??==~==++MN88887$$$7I7++7IDDII~~: 
       ~~8888OO8OODNMM77~=::,,,    ==IINNZZ777??II??IIOO==:, 
       MMOOOOOO8DDMM??~~::,,           ZZOO$Z777II????88+=:, 
     ::NDOZOO888NN77==::,,             I7OOZZ7$$77I???MM??:,. 
     ==D8OOOZOOZMM??=~::,,             ?+88ZZ7777777??NNII:,. 
     MMOOOOZZ$$$MM++~~::               ~~NNZZ7$$77$$IIDD77:,. 
     MMOOOZ$$$$$MM++~~::               ~~NNZZ7$$77$$IIDD77:,. 
     MMOOZZ$$7778O+=~~,,               ~~NNZZI77$$$$77DD77:,. 
     MMOOZZ$$II7OO+=~~,,               ~~NN$$?7777ZZ$$DD77:,. 
     MM88ZZ77+=?MM++~~::               =+8877+77$$$$$$NNII:,. 
     ++DDZZII+=+NN??=~::,,             ??OOII=$7$7$$ZZNNII:,. 
     ==NNOOII++=8877==~~,,,,           77$$??+$777$$OOMM??:, 
     ,:MM88II??~$ZNN$$++::::,,     ,,++MMI7++?$7$$ZZ888O==:,
     :,NN8877??~Z$NN7$++::::,,      ,++MM77++?$$$$ZZ888O==:  
       ::MM$ZII+++IIZONN++:~,,, ,::MM88$$==++IZZOO88NN77=~:  
         I7887$?++??II$$NM77II?I?MMOO77++==II$OZ88DDMM??~~:  
         ==NNOO7====++II$$OO88888ZZ??==~~??77$88DDMN??~~::  
           MMDDO?+++++==??IIIII??++~~::~~77Z$ZDDMMII~~::,,  
             ++MOO$$??++~~:::::::~~++77$$8O8DNMMII~~::,,    
             ++MZO77??++~~:~:::~:~~++77$$OO88DMMII~~::,,    
               =NN88ZO77++++===++??$$ZZOOD8NNM??~~::,,      
                MMMNDD88ZZZZZZ$$$ZZOO88D8NNMM?::::,,        
                  ~~MMMMDDDDDDDD8DDNDNNMMMM==:,,,,          
                    ,,~~??II777$$$$77II?+::,,,              
                              ,,,,,,,,,,,,                  
                                                
"""]

def update():
    text.delete(1.0, 'end')
    text.insert('end', animation[a.count])
    text.pack()
    a.count +=1
    if a.count == 10:
        a.count = 0
    root.after(88, update)

root.after(0, update)
root.mainloop()
