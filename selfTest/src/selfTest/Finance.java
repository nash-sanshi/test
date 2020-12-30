package selfTest;

public class Finance {
    // 给一个有工资收入和稿费收入的小伙伴算税。
    // 启动方法
    public static void main(String[] args) {
        // 所有的类都是 Income 的子类
        Income[] incomes = new Income[] { new Salary(8000), new Royalty(2000) };
        totalTax(incomes);
    }

    public static double totalTax(Income... incomes) {
        double total = 0;
        for (Income income : incomes) {
            total += income.getTax();
        }

        return total;
    }
}

// 普通工资
class Income {
    protected double income;

    // 初始化收入金额
    public Income(double income) {
        this.income = income;
    }

    // 通用税率计算
    public double getTax() {
        return income * 0.1;
    }
}

// 工资收入
class Salary extends Income {
    public Salary(double income) {
        // 必须显示调用父类构造方法
        super(income);
    }

    @Override
    public double getTax() {
        return income <= 5000 ? 0 : (income - 5000) * 0.2;
    }
}

// 稿费收入
class Royalty extends Income {
    public Royalty(double income) {
        super(income);
    }

    public double getTax() {
        return income < 1000 ? 0 : (income - 1000) * 0.1;
    }
}