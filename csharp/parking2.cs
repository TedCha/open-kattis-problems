using System;
using System.Linq;
using System.Collections.Generic;

class parking2
{
    static void Main(string[] args)
    {
        int NumOfTestCases = int.Parse(Console.ReadLine());

        int NumOfStores = 0;
        int DistanceSum = 0;
        string StorePositionStr = "";
        List<int> StorePositionList = new List<int>();

        for (int i = 0; i < NumOfTestCases; i++)
        {
            NumOfStores = int.Parse(Console.ReadLine());
            StorePositionStr = Console.ReadLine();

            StorePositionList = StorePositionStr
                                .Split(' ')
                                .Select(x => int.Parse(x))
                                .OrderBy(x => x)
                                .ToList();

            StorePositionList.Add(StorePositionList[0]);

            DistanceSum = SumDistanceOfPositionList(StorePositionList);

            Console.WriteLine(DistanceSum);
        }
    }
    static int SumDistanceOfPositionList(List<int> PositionList)
    {
        int PositionDiff;
        List<int> DistanceList = new List<int>();

        for (int i = 0; i < PositionList.Count() - 1; i++)
        {
            PositionDiff = Math.Abs(PositionList[i] - PositionList[i + 1]);
            DistanceList.Add(PositionDiff);
        }

        return DistanceList.Sum();
    }
}