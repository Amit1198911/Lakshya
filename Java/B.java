import java.util.*;

class Single{
         public static Scanner sc = new Scanner(System.in);
	String name;
	int age;
	void getBase(){
	 try{
	   name = sc.nextLine();
	   age = sc.nextInt();
}catch(Exception ee){
System.out.println("Invalid input entered");
System.out.println(ee);
System.exit(0);

	}
}
	void showBase(){
	 	System.out.println(name + "  " + age);
	}
}
class B extends Single{
	String branch;
	int semester;
	void getchild_data(){
	  Scanner sc = new Scanner(System.in);
	  branch = sc.nextLine();
	  semester = sc.nextInt();
	}
	void showchild_data(){
	   System.out.println(branch+ " "+ semester);
	}

public static void main(String args[]){
	   B ob = new B();
	   ob.getBase();
	   ob.showBase();
	   ob.getchild_data();
	   ob.showchild_data();
	}
	
}

