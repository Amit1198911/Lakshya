//Over loading
import java.util.Scanner;
class V{
	double w,h,d;
	Box(){
		w = 10;
		h=20;
		d=30; 
	}
	void vol(){
		System.out.println(w*h*d);
	}
	Box(double len){
		w=h=d=len;
	}
	Box(double w1,double w2,double w3){
		this.w = w;
		this.h =h;
 		this.d = d;
		
	}
	public static void main(String a[]){
	 Box b = new Box();
	 b.
	 Box b1 = new Box(3);
	 Box b2 = new Box(5.6,8.9,7,8);
	     
	}
}