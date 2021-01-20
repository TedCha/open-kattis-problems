using System;

class hangingout
{
    static void Main(string[] args)
    {
        string[] InputLine = Console.ReadLine().Split(' ');

        int FireSafetyLimit = int.Parse(InputLine[0]);
        int NumberOfEvents = int.Parse(InputLine[1]);
        int NumOfPeopleOnTerrace = 0;
        int DeniedEntryCount = 0;

        for (int i = 0; i < NumberOfEvents; i++)
        {
            string[] EventInputLine = Console.ReadLine().Split(' ');

            string Event = EventInputLine[0];
            int NumOfPeopleInEvent = int.Parse(EventInputLine[1]);

            switch(Event)
            {
                case "enter":
                    if (NumOfPeopleOnTerrace + NumOfPeopleInEvent <= FireSafetyLimit)
                        NumOfPeopleOnTerrace += NumOfPeopleInEvent;
                    else
                        DeniedEntryCount++;
                    break;
                case "leave":
                    NumOfPeopleOnTerrace -= NumOfPeopleInEvent;
                    break;
            }
        }

        Console.WriteLine(DeniedEntryCount);
    }
}
