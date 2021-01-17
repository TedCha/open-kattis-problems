using System;
using System.Linq;
using System.Collections.Generic;

class cetvrta
{
    static void Main(string[] args)
    {
        List<int> RectangleCoordXList = new List<int>();
        List<int> RectangleCoordYList = new List<int>();

        for (int i=0; i < 3; i++)
        {
            string[] Coordinates = Console.ReadLine().Split(' ');

            int PointX = int.Parse(Coordinates[0]);
            int PointY = int.Parse(Coordinates[1]);

            RectangleCoordXList.Add(PointX);
            RectangleCoordYList.Add(PointY);
        }

        int LeastFrequentXNum = FindLeastCommonNum(RectangleCoordXList);

        int LeastFrquentYNum = FindLeastCommonNum(RectangleCoordYList);

        Console.WriteLine(LeastFrequentXNum + " " + LeastFrquentYNum);
    }

    static int FindLeastCommonNum(List<int> NumList)
    {
        int LeastCommonNum = NumList.GroupBy(x => x)
            .OrderByDescending(Group => Group.Count())
            .Select(Group => Group.Key)
            .Last();

        return LeastCommonNum;
    }
}
