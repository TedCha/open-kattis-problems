using System;
using System.Linq;
using System.Collections.Generic;

class numberfun
{
    static void Main(string[] args)
    {
        string Result = "";
        int NumberOfTestCases = int.Parse(Console.ReadLine());
        List<int> NumberList = new List<int>();

        for (int i=0; i < NumberOfTestCases; i++)
        {
            NumberList = Console.ReadLine()
                        .Split(' ')
                        .Select(x => int.Parse(x))
                        .ToList();

            Result = DetermineThirdNumberPlausability(NumberList);

            Console.WriteLine(Result);
        }
    }

    static string DetermineThirdNumberPlausability(List<int> NumberList)
    {
        int Num1 = NumberList[0];
        int Num2 = NumberList[1];
        int Num3 = NumberList[2];

        if (Num1 + Num2 == Num3)
            return "Possible";
        else if (Num1 - Num2 == Num3)
            return "Possible";
        else if (Num2 - Num1 == Num3)
            return "Possible";
        else if (Num1 * Num2 == Num3)
            return "Possible";
        else if (Num1 / (float) Num2 == (float) Num3)
            return "Possible";
        else if (Num2 / (float) Num1 == (float) Num3)
            return "Possible";
        else
            return "Impossible";
    }
}
