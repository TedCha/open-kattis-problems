using System;

class ofugsnuid
{
    static void Main(string[] args)
    {
        int NumberOfNums = int.Parse(Console.ReadLine());
        string[] NumStrArray = new string [NumberOfNums];

        for (int i = 0; i < NumberOfNums; i++)
        {
            NumStrArray[i] = Console.ReadLine();
        }

        int j = 0;
        int k = NumStrArray.Length - 1;

        while(j < k)
        {
            string temp = NumStrArray[j];
            NumStrArray[j] = NumStrArray[k];
            NumStrArray[k] = temp;
            j++;
            k--;
        }

        Console.WriteLine(string.Join("\n", NumStrArray));
    }
}