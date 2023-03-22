import java.util.*;
class Cons{
int a,b;	
	Cons(){
Scanner sc = new Scanner(System.in);
		a = sc.nextInt();
		b = sc.nextInt();
		System.out.println(a+b);
	}
    Cons(int a,int b){
		
		System.out.println(a+b);
	}
	public static void main(String ayy[]){
		Scanner sc = new Scanner(System.in);
		int a,b;
		Cons ob1 = new Cons();
         	   a = sc.nextInt();
			b = sc.nextInt();
		Cons ob2 = new Cons(a,b);


	}
}