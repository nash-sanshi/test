package selfTest;

import java.util.Random;
import java.util.Scanner;

public class SwitchTest {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Random random = new Random();
		int num = random.nextInt(3);
		System.out.println("请输入你要出的手势（石头、剪刀、布）：");
		String chioce = scanner.nextLine();

		switch (chioce) {
		case "石头":
			if (num == 0) {
				System.out.println("系统出了石头，平局");
			} else if (num == 1) {
				System.out.println("系统出了剪刀，你赢了");
			} else {
				System.out.println("系统出了布，你输了");
			}
			break;
		case "剪刀":
			if (num == 0) {
				System.out.println("系统出了石头，你输了");
			} else if (num == 1) {
				System.out.println("系统出了剪刀，平局");
			} else {
				System.out.println("系统出了布，你赢了");
			}
			break;
		case "布":
			if (num == 0) {
				System.out.println("系统出了石头，你赢了");
			} else if (num == 1) {
				System.out.println("系统出了剪刀，你输了");
			} else {
				System.out.println("系统出了布，平局");
			}
			break;
		default:
			System.out.println("你的输入有误，请输入石头、剪刀、布，其中一个。");
			break;
		}
	}
}
