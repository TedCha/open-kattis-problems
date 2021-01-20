using System;
using System.Linq;
using System.Collections.Generic;

class zanzibar
{
    static void Main(string[] args)
    {
        int NumberOfTestCases = int.Parse(Console.ReadLine());

        for (int i = 0; i < NumberOfTestCases; i++)
        {
            int LowerBoundOfImported = 0;

            List<int> TotalPerYearList = Console.ReadLine()
                .Split(' ')
                .Select(x => int.Parse(x))
                .ToList();

            for (int j = 1; j <= TotalPerYearList.Count() - 1; j++)
            {
                int CurrentYearTotal = TotalPerYearList[j];
                int PreviousYearTotal = TotalPerYearList[j - 1];
                int CurrentYearPotential = PreviousYearTotal * 2;

                if (CurrentYearTotal > CurrentYearPotential)
                    LowerBoundOfImported += (CurrentYearTotal - CurrentYearPotential);
            }

            Console.WriteLine(LowerBoundOfImported);

        }
    }
}
