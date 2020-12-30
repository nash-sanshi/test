package selfTest;

public class Static {

	   public static void main(String[] args) {
	        //Person.count += 1;        
	        Person2 p1 = new Person2("p1");        
	        System.out.println(Person2.getCount());        
	        Person2 p2 = new Person2("p2");        
	        System.out.println(Person2.getCount());        
	        Person2 p3 = new Person2("p3");        
	        System.out.println(Person2.getCount());        
	        Person2 p4 = new Person2("p4");        
	        System.out.println(Person2.getCount());    
	    }
	}

	class Person2{
	    String name;    
	    static int count =0;    
	    //构造函数不能加void    
	    public Person2(String name){
	        count+=1;    
	    }

	    public static int getCount(){
	        return count;    
	    }
	}