package selfTest;

public class Interface {
    // 给一个有工资收入和稿费收入的小伙伴算税。
    // 启动方法
    public static void main(String[] args) {
        totalTax();
    }

    public static double totalTax() {
        Salary s = new Salary(8000);
        Royalty r = new Royalty(2000);
        return s.getTax() + r.getTax();
    }
}

interface Income2 {
    // 子类必须实现的规范
    public abstract double getTax();   
}

// 工资收入
class Salary1 implements Income2 {
    protected double income;

    // 初始化收入金额
    public Salary1(double income) {
        this.income = income;
    }

    public double getTax() {
        return income <= 5000 ? 0 : (income - 5000) * 0.2;
    }
}

// 稿费收入
class Royalty1 implements Income2 {
    public double income;

    public Royalty1(double income) {
        this.income = income;
    }

    public double getTax() {
        return income < 1000 ? 0 : (income - 1000) * 0.1;
    }
}