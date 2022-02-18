package com.company;

/*
Two clocks, which show the time in hours and minutes using the 24-hour clock, are running at different speeds. Each
clock is an exact number of minutes per hour fast. Both clocks start showing the same time (00:00) and are checked
regularly every hour (starting after one hour) according to an accurate timekeeper. What time will the two clocks show
on the first occasion when they are checked and show the same time?

For example, suppose the first clock runs 1 minute fast (per hour) and the second clock runs 31 minutes fast (per hour).
• When the clocks are first checked after one hour, the first clock will show 01:01 and the second clock will show 01:31;
• When the clocks are checked after two hours, they will show 02:02 and 03:02;
• After 48 hours the clocks will both
 show 00:48.

 Write a program which reads in a two integers, each between 0 and 50,000 inclusive, indicating the number of minutes
 fast (per hour) of the first and second clock respectively.

 You should output the time shown on the clocks when they first match. Both the hour and the minutes should be displayed
 with two digits.

 Full marks will be granted for a time-and-memory complexity of O(1). Programs of a complexity that exceeds
 O(n) will NOT be marked.
 */

public class Clock {

    public static String alignmentTime(int c1, int c2) {
        int alignmentDifference = Math.abs(c1-c2);
        int elapsedTime = (1440/alignmentDifference);
        int displayMinutes = (c1*elapsedTime)%1440;
        String hours = String.format("%02d",(int)(displayMinutes-(displayMinutes%60))/60);
        String minutes = String.format("%02d", displayMinutes%60);
        return  hours + ":" + minutes;
    }

}
