package selfTest;

public class ReloadName {
	public static void main(String[] args) {
		Person1 ming = new Person1();
		Person1 hong = new Person1();
		ming.setName("Xiao Ming");
		// TODO: 给Person增加重载方法setName(String, String):
		hong.setName("Xiao", "Hong");
		System.out.println(ming.getName());
		System.out.println(hong.getName());
	}
}

class Person1 {
	private String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setName(String name1,String name2) {
		this.name = name1  + ' ' +  name2;
	}
}
