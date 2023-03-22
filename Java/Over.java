class Area{
 float b;
 float h;
 void triangle(float b,float h){
    System.out.println("Area of triangle  : "+(b+h)/2);
 }
  
}
class Area2 extends Area{
	float l;
	void rectangle(float l,float b){
	   System.out.printf("Area of rectangle : "+(l*b));
	}


public static void main(String ar[]){
Area2 s= new Area2();
s.triangle(3.09,9.89);
s.rectangle(2.34,4.5);
}

}


