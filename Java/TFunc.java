import java.util.Scanner;
class TFunc{
	int x,y;
	public void f1(){
		System.out.println("Yes..");
 		this.f1();
	   	this.f1();
		
	}
	public static void main(String a[]){
	   TFunc t = new TFunc();

		t.f1();  
	   
	}
}