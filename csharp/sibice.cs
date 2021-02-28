using System;
using System.Linq;
using System.Collections.Generic;

class sibice
{
    static void Main(string[] args)
    {
        List<int> CaseInputList = Console.ReadLine()
            .Split(' ')
            .Select(x => int.Parse(x))
            .ToList();

        int NumberOfMatches = CaseInputList[0];
        int Width = CaseInputList[1];
        int Height = CaseInputList[2];
        double MaxLength = Math.Sqrt(Math.Pow(Width, 2) + Math.Pow(Height, 2));
        
        for (int i = 0; i < NumberOfMatches; i++)
        {
            int MatchLength = int.Parse(Console.ReadLine());

            if (MatchLength <= MaxLength)
            {
                Console.WriteLine("DA");
            }
            else
            {
                Console.WriteLine("NE");
            }
        }
    }
}