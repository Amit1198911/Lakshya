import java.util.*;

class Single{
	String name;
	int age;
	void getBase(){
	 Scanner sc = new Scanner(System.in);
	   name = sc.nextLine();
	   age = sc.nextInt();
	}
	void showBase(){
	 	System.out.println(name + age);
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

