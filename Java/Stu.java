import java.util.Scanner;

class Stu{
	int age;
	String name;
	float cgpa;
	
	Stu(int age,String name,float cgpa){
		System.out.println(name+" "+age+" "+cgpa);
		
	 
	}
	public static void main(String a[]){
	 int age1;
	 String name1;
	 float cgpa1;
	 Scanner sc = new Scanner(System.in);
	 System.out.println("Enter name : ");
	 name1 = sc.nextLine();
         System.out.println("Enter age : ");
	 age1 = sc.nextInt();
	 
	 System.out.println("Enter cgpa : ");
	 cgpa1 = sc.nextFloat();
	 Stu ob = new Stu(age1, name1, cgpa1);

	
	 
	 
	}
}