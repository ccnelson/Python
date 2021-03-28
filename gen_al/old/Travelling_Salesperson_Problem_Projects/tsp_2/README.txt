~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TO CALCULATE DISTANCES:
https://ncalculators.com/geometry/length-between-two-points-calculator.htm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
favicon.ico is a .bmp renamed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
in circular random mode, if the path between any two points is greater than
 apprx 2*ext (extent)- (or maybe 1.5*) of circle drawing - then route is inefficient
 - maybe save the extent when drawing and compare later -
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kinda works, but interface doesnt update per iteration. Gen algo has to complete
before UI shows progress, this is because of how things are isolated into classes
 and modules. Tried moving modules into one main file, but it seems the functions
 are buried too deep in classes, making the UI freeze following a button press, 
 and user unable to stop algorithm. One solution would be to store all data as 
class variables (like first version), make all the functions and UI top level / no 
 indentation. It seems if called from this namespace the UI remains interactive.
 So next thing is to reformat / start over. Problem is; we want the algorithm to
 have low coupling, to be able to make them parallel / multiply later.