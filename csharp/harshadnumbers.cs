using System;
using System.Linq;
using System.Collections.Generic;

class harshadnumbers
{
    static void Main(string[] args)
    {

        int Num = int.Parse(Console.ReadLine());

        Console.WriteLine(GetHarshadNumber(Num));
    }

    static int SumDigitsOfNumber(int Num)
    {
        string StrNum = Num.ToString();
        List<int> NumList = StrNum.Select(Digit => int.Parse(Digit.ToString())).ToList();
        return NumList.Sum();
    }

    static int GetHarshadNumber(int Num)
    {
        int DigitSum;

        while (true)
        {
            DigitSum = SumDigitsOfNumber(Num);

            if (Num % DigitSum != 0)
                Num++;
            else
                break;
        }

        return Num;
    }
}
