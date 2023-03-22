class sup{
void child(){
System.out.printf(" HEllo");
}
}
class sup2 extends sup{
void child(){
super.child();
System.out.printf(" HEllo kjasdljasd");
}


public static void main(){


sup2 s= new sup2();
s.child();
}

}


