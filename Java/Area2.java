class Area{
 void ar(double b,double h){
    System.out.println("Area of triangle  : "+(b+h)/2);
 }
  
}
class Area2 extends Area{
	void ar(double l,double b){
	   System.out.printf("Area of rectangle : "+(l*b)+" \n");
	}


public static void main(String ar[]){
Area2 s= new Area2();

s.ar(2.34,4.5);
Area ss= new Area();
ss.ar(3.09,9.89);
}

}


